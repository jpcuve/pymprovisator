from typing import List


class Genre:
    def __init__(self, name: str, meter: str, tempo_unit: str):
        self.name = name
        self.meter = meter  # mesure
        self.tempo_unit = tempo_unit

    def piano_line(self) -> List[str]:
        raise NotImplemented

    def bass_line(self) -> List[str]:
        raise NotImplemented

    def drum_line(self) -> List[str]:
        raise NotImplemented
