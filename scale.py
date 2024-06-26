from __future__ import annotations
from pitch import Pitch, Pitches
from circle_of_fifth import CircleOfFifth


class Scale:
    def __init__(self, root: Pitch, feeling: int = 0, length: int = 7) -> Pitches:
        cof = CircleOfFifth(root)

        counter_clockwise = feeling + 1

        notes_to_add = []

        cof.shift(-counter_clockwise)
        for _ in range(counter_clockwise):
            notes_to_add.append(cof.cursor)
            cof.shift(1)

        scale = []
        for _ in range(length - counter_clockwise):
            scale.append(cof.cursor)
            cof.shift(1)

        self.pitches = Pitches(scale + notes_to_add)


def test_scale():
    cionian = Scale(Pitch(0), 0, 7)