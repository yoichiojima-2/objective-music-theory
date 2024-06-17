from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Pitch:
    number: int
    octave: int = 0

    def rel(self, shift) -> Pitch:
        shifted_num = self.number + shift
        return Pitch(
            number = shifted_num % 12,
            octave = self.octave + (shifted_num // 12)
        )

    def round(self) -> Pitch:
        self.ocvate = 0
        return self


def test_pitch():
    p = Pitch(0)
    assert p.number == 0
    assert p.octave == 0
    print(p)

    p2 = p.rel(7)
    assert p2.number == 7
    assert p2.octave == 0
    print(p2)

    p3 = p2.rel(7)
    assert p3.number == 2
    assert p3.octave == 1
    print(p3)
