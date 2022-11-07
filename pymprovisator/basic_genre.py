from pymprovisator.abc import NOTES
from pymprovisator.genre import Genre
from pymprovisator.track import Track
from pymprovisator.tune import Tune


class BasicGenre(Genre):
    def __init__(self):
        super().__init__('basic', '4/4', '4')

    def piano_line(self, tune: Tune) -> Track:
        return super().piano_line()

    def bass_line(self, tune: Tune) -> Track:
        temp = [
            '%bass line',
            'V:1',  # voice 1 ?
            '%%MIDI channel 1',  # midi channel
            '%%MIDI program 1 99',  # midi channel & program ?
            'I:clef=bass octave=-2',
            '%%MIDI control 10 1',  # ?
            '%%MIDI control 7 90',  # midi volume
            'z8',
        ]
        temp2 = []
        for ch in self.song.chord_item_collection:
            bass_note = NOTES[ch.chord.root]
            temp2 += [bass_note] * int(ch.parts)
        for x in range(int(self.song.n_choruses)):
            temp.append(" ".join(temp2))
        temp.append(NOTES[self.song.chord_item_collection[0].chord.root] + self.meter)
        return temp

    def drum_line(self, tune: Tune) -> Track:
        return super().drum_line()

