from __future__ import annotations
from dataclasses import dataclass
import itertools


@dataclass
class Pitch:
    number: int
    octave: int = 0

    def rel(self, n) -> Pitch:
        return Pitch(
            number = self.number + n % 12,
            octave = self.octave + n // 12
        )


class Pitches:
    pitches: list[Pitch]

    def __init__(self, pitches: list[Pitch]):
        self.pitches = pitches

    def __iter__(self) -> Pitch:
        self._iter = iter(self.pitches)
        return self._iter

    def __next__(self) -> Pitch:
        return next(self._iter)

    def cycle(self, n) -> Pitch:
        cnt = 0
        for i in itertools.cycle(self.pitches):
            if cnt == n:
                break
            cnt += 1
            yield i


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
