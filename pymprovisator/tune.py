from dataclasses import dataclass
from time import sleep
from typing import List

import mido

from pymprovisator.chord import Chord
from pymprovisator.music import PATTERNS
from pymprovisator.track import Track


@dataclass
class Sample:
    duration: int
    chord: Chord


class Tune:
    def __init__(self, title: str, tempo: int, key: str, samples: List[Sample],
                 bar_count: int, chorus_count: int):
        self.title = title
        self.tempo = tempo
        self.key = key
        self.samples = samples
        self.bar_count = bar_count
        self.chorus_count = chorus_count

    def walking_pattern(self, sample_position: int, meter: int) -> List[int]:
        sample = self.samples[sample_position % len(self.samples)]
        next_sample = self.samples[(sample_position + 1) % len(self.samples)]
        pattern = PATTERNS[sample.chord.get_distance(next_sample.chord)]
        if sample.duration == 1:
            return [sample.chord.root]
        elif 2 <= sample.duration <= 10:
            return [sample.chord.scale[i - 1] for i in pattern[sample.duration - 2]]
        else:
            raise NotImplementedError
            # aux = ''
            # multiplier, parts2 = split_long_chord(parts, meter)
            # aux += multiplier * (
            #     ' '.join([notes_abc[base_note + escale_notes[chord.type][i - 1]] for i in pattern[meter - 2]]))
            # if parts2 == 1:
            #     aux += notes_abc[base_note] + ' '
            # elif 2 <= parts2 <= 10:
            #     aux += ' '.join([notes_abc[base_note + escale_notes[chord.type][i - 1]] for i in pattern[parts2 - 2]])
            # return aux

    def play_samples(self, midi_outport, channel: int):
        track = Track()
        time = 0
        for sample in self.samples:
            track.punch_chord(sample.chord.arpeggio, time, sample.duration)
            time += sample.duration
        # then we play the track
        tempo = 0.3
        midi = track.to_midi(channel)
        for tick in range(time):
            for message in midi[tick]:
                midi_outport.send(message)
            sleep(tempo)

    def play_walking_pattern(self, midi_outport, channel: int):
        track = Track()
        time = 0




if __name__ == '__main__':
    tune = Tune('Some test', 120, 'G',  [
        Sample(4, Chord(60, '7')),
        Sample(2, Chord(62, 'm7')),
        Sample(2, Chord(67, '7alt')),
        Sample(4, Chord(60, 'm7')),
        Sample(4, Chord(65, '7')),
        Sample(8, Chord(70, 'maj7#11')),
    ], 20, 4)
    output_names = mido.get_output_names()
    outport = mido.open_output(output_names[0])
    tune.play_samples(outport, 1)
