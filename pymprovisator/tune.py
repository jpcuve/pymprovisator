from dataclasses import dataclass
from typing import List

from pymprovisator.chord import Chord
from pymprovisator.music import PATTERNS


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

    def walking_pattern(self, sample_position: int, parts: int, meter: int) -> List[int]:
        sample = self.samples[sample_position % len(self.samples)]
        next_sample = self.samples[(sample_position + 1) % len(self.samples)]
        pattern = PATTERNS[sample.chord.get_distance(next_sample.chord)]
        if parts == 1:
            return [sample.chord.root]
        elif 2 <= parts <= 10:
            return [sample.chord.scale[i - 1] for i in pattern[parts - 2]]
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


if __name__ == '__main__':
    tune = Tune('Some test', 120, 'G', [], 20, 4)
    print(tune.to_abc())
