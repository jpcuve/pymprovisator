from collections import defaultdict
from dataclasses import dataclass
from typing import List, DefaultDict

import mido


@dataclass
class Note:
    pitch: int
    duration: int


class Track:
    def __init__(self):
        self.notes = defaultdict(list)
        self.total_duration = 0

    def punch_note(self, pitch: int, when: int, duration: int):
        self.punch_chord([pitch], when, duration)

    def punch_chord(self, pitches: List[int], when: int, duration: int):
        for pitch in pitches:
            self.notes[when].append(Note(pitch, duration))
            if when + duration > self.total_duration:
                self.total_duration = when + duration

    def to_midi(self, channel: int) -> DefaultDict[int, List[mido.Message]]:
        messages = defaultdict(list)
        for when, notes in self.notes.items():
            for note in notes:
                messages[when].append(mido.Message('note_on', channel=channel, note=note.pitch, velocity=100))
                messages[when + note.duration].append(mido.Message('note_off', channel=channel, note=note.pitch))
        return messages

    def to_abc(self):
        raise NotImplementedError
