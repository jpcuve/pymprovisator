from collections import defaultdict
from typing import List


class Track:
    def __init__(self):
        self.note_on = defaultdict(list)
        self.note_off = defaultdict(list)

    def punch_note(self, note: int, when: int, duration: int):
        self.punch_chord([note], when, duration)

    def punch_chord(self, notes: List[int], when: int, duration: int):
        for note in notes:
            self.note_on[when].append(note)
            self.note_off[when + duration].append(note)



