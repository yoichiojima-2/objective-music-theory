from __future__ import annotations
from pitch import Pitch, Pitches
from circle_of_fifth import CircleOfFifth


class Scale:
    @staticmethod
    def generate(root: Pitch, feeling: int) -> Pitches:
        'ionian will be returned when called with feeling = 0'
        cof = CircleOfFifth(root)
        cof.shift(feeling - 2)
        while True:
            yield cof.shift(1).cursor

    @classmethod
    def generate_up_to_n(cls, root: Pitch, feeling: int, n: int) -> Pitches:
        cof = CircleOfFifth(root)
        cof.shift(feeling - 1)

        cnt = 0
        for p in cls.generate(root, feeling):
            if cnt > (n - 1):
                break
            yield p
            cnt += 1


def test_scale():
    c_ionian = (
        Pitches(list(Scale.generate_up_to_n(Pitch.new_from_str("C"), 0, 7)))
        .sort()
        .reset_octave()
    )
    assert c_ionian.numbers == [0, 2, 4, 5, 7, 9, 11]

    c_aeolian = (
        Pitches(list(Scale.generate_up_to_n(Pitch.new_from_str("C"), -3, 7)))
        .sort()
        .reset_octave()
    )
    assert c_aeolian.numbers == [0, 2, 3, 5, 7, 8, 10]
