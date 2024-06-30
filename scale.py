from __future__ import annotations
from pitch import Pitch, Pitches
from circle_of_fifth import CircleOfFifth


class Scale:
    def __init__(self, root: Pitch, feeling: int = 0, length: int = 7):
        cof = CircleOfFifth(root)

        # set defauult scale to ionian which needs to
        # shift 1 counter clockwise on the circle of fifth
        counter_clockwise = feeling - 1

        cof.shift(counter_clockwise)
        for _ in range(counter_clockwise):
            cof.shift(1)

        scale = []
        for _ in range(length):
            scale.append(cof.cursor)
            cof.shift(1)

        self.pitches = Pitches(scale).reset_octave().sort().pitches


def test_scale():
    c_ionian = Scale(Pitch.new_from_str("C"), 0, 7)
    c_ionian_nums = [p.number for p in c_ionian.pitches]
    assert c_ionian_nums == [0, 2, 4, 5, 7, 9, 11]

    c_aeolian = Scale(Pitch.new_from_str("C"), -3, 7)
    c_aeolian_nums = [p.number for p in c_aeolian.pitches]
    assert c_aeolian_nums == [0, 2, 3, 5, 7, 8, 10]
