from __future__ import annotations
from pitch import Pitch, Pitches
from circle_of_fifth import CircleOfFifth


class Scale:
    @property
    def build(root: Pitch, feeling: int = 0, length: int = 7) -> Pitches:
        cof = CircleOfFifth(root)

        scale = []
        cof.shift(feeling - 1)
        for _ in range(length):
            scale.append(cof.shift(1))

        return Pitches(scale).reset_octave().sort()


def test_scale():
    c_ionian = Scale.build(Pitch.new_from_str("C"), 0, 7)
    c_ionian_nums = [p.number for p in c_ionian.pitches]
    assert c_ionian_nums == [0, 2, 4, 5, 7, 9, 11]

    c_aeolian = Scale.build(Pitch.new_from_str("C"), -3, 7)
    c_aeolian_nums = [p.number for p in c_aeolian.pitches]
    assert c_aeolian_nums == [0, 2, 3, 5, 7, 8, 10]
