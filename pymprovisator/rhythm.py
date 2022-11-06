from typing import List


class Rhythm:
    def __init__(self, name, meter, tempo_unit):
        self.name = name
        self.meter = meter
        self.tempo_unit = tempo_unit

    def piano_line(self) -> List[str]:
        raise NotImplemented

    def bass_line(self) -> List[str]:
        raise NotImplemented

    def drum_line(self) -> List[str]:
        raise NotImplemented
