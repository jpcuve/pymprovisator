from typing import List, Tuple

from pymprovisator.chord import Chord
from pymprovisator.rhythm import Rhythm


class Tune:
    def __init__(self, rhythm: Rhythm, id: str, title: str, tempo: int, key: str, chords: List[Tuple[int, Chord]], bar_count: int):
        self.rhythm = rhythm
        self.id = id
        self.title = title
        self.tempo = tempo
        self.key = key
        self.chords = chords
        self.bar_count = bar_count


