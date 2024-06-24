from __future__ import annotations
from dataclasses import dataclass
from pitch import Pitch


@dataclass
class CircleOfFifth:
    cursor: Pitch

    def __init__(self, cursor: Pitch):
        self.cursor = cursor

    def shift(self, n) -> CircleOfFifth:
        self.cursor = self.cursor.rel(n * 7)
        return self


def test_circle_of_fifth():
    cof = CircleOfFifth(Pitch(0))
    assert cof.cursor.number == 0
    cof.shift(2)
    assert cof.cursor.number == 14
    cof.shift(-3)
    assert cof.cursor.number == -7
