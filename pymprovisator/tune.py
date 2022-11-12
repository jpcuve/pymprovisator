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

    def compute_chord_track(self) -> Track:
        track = Track()
        time = 0
        for sample in self.samples:
            track.punch_chord(sample.chord.arpeggio, time, sample.duration)
            time += sample.duration
        return track

    def compute_walking_track(self) -> Track:
        track = Track()
        time = 0
        for sample_index in range(len(self.samples)):
            walking_pattern = self.walking_pattern(sample_index, 0)
            for pitch in walking_pattern:
                track.punch_chord([pitch], time, 1)
                time += 1
        return track

    def play_tracks(self, tracks: List[Track], midi_outport, channel: int):
        tempo = 0.3
        midis = [track.to_midi(channel) for track in tracks]
        for tick in range(max([track.total_duration for track in tracks])):
            for midi in midis:
                for message in midi[tick]:
                    midi_outport.send(message)
            sleep(tempo)


if __name__ == '__main__':
    tune = Tune('Some test', 120, 'G', [
        Sample(4, Chord(60, '7')),
        Sample(2, Chord(62, 'm7')),
        Sample(2, Chord(67, '7alt')),
        Sample(4, Chord(60, 'm7')),
        Sample(4, Chord(65, '7')),
        Sample(8, Chord(70, 'maj7#11')),
    ], 20, 4)
    tracks = [tune.compute_chord_track(), tune.compute_walking_track()]
    output_names = mido.get_output_names()
    outport = mido.open_output(output_names[0])
    tune.play_tracks(tracks, outport, 1)
