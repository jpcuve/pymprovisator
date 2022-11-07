from unittest import TestCase

from pymprovisator.chord import Chord


class TestPymprovisator(TestCase):
    def test_chords(self):
        example_input = ['C7', 'Dm7', 'G7alt', 'Cm7', 'F7', 'Bbmaj7#11']
        for i in example_input:
            chord = Chord.parse(i)
            print(chord)
            print(chord.arpeggio)
            print(chord.scale)

