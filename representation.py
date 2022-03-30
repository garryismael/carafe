from dataclasses import dataclass


@dataclass
class Mesure:
    before_y: int
    before_h: int
    after_y: int
    after_h: int