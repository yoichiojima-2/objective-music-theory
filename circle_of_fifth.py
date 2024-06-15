from __future__ import annotations
from pitch import Pitch


class CircleOfFifths:
    def __init__(self, pitch: Pitch):
        self.pitch = pitch

    def __iter__(self):
        return self

    def __next__(self):
        self.pitch = Pitch(self.pitch.number + 7)
        return self.pitch


def test_circle_of_fifths():
    circle = CircleOfFifths(Pitch("c"))
    assert circle.pitch.name == "c"
    print(circle.pitch)
    next(circle)
    print(circle.pitch)
    assert circle.pitch.name == "g"
    next(circle)
    print(circle.pitch)
    assert circle.pitch.name == "d"