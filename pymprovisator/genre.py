from typing import List

from pymprovisator.track import Track
from pymprovisator.tune import Tune


class Genre:
    def __init__(self, name: str, meter: str, tempo_unit: str):
        self.name = name
        self.meter = meter  # mesure
        self.tempo_unit = tempo_unit

    def piano_line(self, tune: Tune) -> Track:
        raise NotImplemented

    def bass_line(self, tune: Tune) -> Track:
        raise NotImplemented

    def drum_line(self, tune: Tune) -> Track:
        raise NotImplemented
