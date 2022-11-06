from pymprovisator.rhythm import Rhythm


class BasicRhythm(Rhythm):
    def __init__(self):
        super().__init__('basic', '4/4', '4')

    def piano_line(self):
        return super().piano_line()

    def bass_line(self):
        return super().bass_line()

    def drum_line(self):
        return super().drum_line()

