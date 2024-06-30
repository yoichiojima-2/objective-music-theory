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
    # start with c
    cof = CircleOfFifth(Pitch.new_from_str("C"))
    assert cof.cursor.number == 0
    assert cof.cursor.octave == 0

    # shift clockwise 2 times
    cof.shift(2)

    # should be d + 1 octave
    assert cof.cursor.number == 2
    assert cof.cursor.octave == 1

    # shift counter clockwise 3 times
    cof.shift(-3)

    # should be f - 1 octave
    assert cof.cursor.number == 5
    assert cof.cursor.octave == -1
