from __future__ import annotations
from dataclasses import dataclass
import itertools


@dataclass
class Pitch:
    number: int
    octave: int = 0

    def rel(self, n) -> Pitch:
        return Pitch(
            number = (self.number + n) % 12,
            octave = self.octave + (self.number + n) // 12
        )


def test_pitch():
    p = Pitch(0)
    assert p.number == 0
    assert p.octave == 0

    p2 = p.rel(2)
    assert p2.number == 2
    assert p2.octave == 0

    p3 = p.rel(13)
    assert p3.number == 1
    assert p3.octave == 1

    p4 = p.rel(-7)
    assert p4.number == 5
    assert p4.octave == -1

    ps = Pitches([Pitch(0), Pitch(1), Pitch(2)])
    ps.pitches[0].number == 0
    ps.pitches[1].number == 1

    for i, p in enumerate(ps):
        print("iterate:", i, p)

    for i, p in enumerate(ps.cycle(6)):
        print("cycle:", i, p)
