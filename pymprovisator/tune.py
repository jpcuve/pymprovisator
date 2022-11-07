from typing import List, Tuple

from pymprovisator.chord import Chord


class Tune:
    def __init__(self, title: str, tempo: int, key: str, chords: List[Tuple[int, Chord]],
                 bar_count: int, chorus_count: int):
        self.title = title
        self.tempo = tempo
        self.key = key
        self.chords = chords
        self.bar_count = bar_count
        self.chorus_count = chorus_count

    def to_abc(self):
        lines = ['<score lang="ABC">']
        lines.extend([f'{k}:{v}' for k, v in {
            'X': 1,
            'T': self.title,
            'M': self.genre.meter,
            'L': f'1/{self.genre.tempo_unit}',
            'Q': f'1/{self.genre.tempo_unit}={self.tempo}',
            'R': self.genre.name,
            'K': self.key,
        }.items()])
        # append tune
        lines.append('</score>')
        return '\n'.join(lines)


if __name__ == '__main__':
    tune = Tune('Some test', 120, 'G', [], 20, 4)
    print(tune.to_abc())