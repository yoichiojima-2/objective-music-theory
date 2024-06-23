from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Pitch:
    number: int
    octave: int = 0

    def rel(self, shift) -> Pitch:
        shifted_num = self.number + shift
        if shifted_num >= 0:
            return Pitch(
                number=shifted_num % 12, octave=self.octave + (shifted_num // 12)
            )
        else:
            octave_shift = 0
            while shifted_num <= 0:
                shifted_num += 12
                octave_shift -= 1

            return Pitch(number=shifted_num, octave=self.octave + octave_shift)

    def round(self) -> Pitch:
        self.ocvate = 0
        return self


class Pitches:
    pitches: list[Pitch]

    def __init__(self, pitches: list[Pitch]):
        self.pitches = pitches

   def __iter__(self):
        self._iter = iter(self.pitches)
        return self

    def __next__(self):
        return next(self._iter)



def test_pitch():
    p = Pitch(0)
    print(p)
    assert p.number == 0
    assert p.octave == 0

    p2 = p.rel(7)
    print(p2)
    assert p2.number == 7
    assert p2.octave == 0

    p3 = p2.rel(7)
    print(p3)
    assert p3.number == 2
    assert p3.octave == 1

    p4 = p.rel(-7)
    print(p4)
    assert p4.number == 5
    assert p4.octave == -1

    ps = Pitches([Pitch(0), Pitch(1)])
    print(ps)
