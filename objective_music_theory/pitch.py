from __future__ import annotations

import itertools
import typing as t
from dataclasses import dataclass


@dataclass
class Pitch:
    number: int
    octave: int = 0

    def rel(self, n) -> Pitch:
        return Pitch(
            number=(self.number + n) % 12, octave=self.octave + (self.number + n) // 12
        )

    @staticmethod
    def new_from_str(s) -> Pitch:
        match s:
            case "C":
                return Pitch(0)
            case "C#" | "Db":
                return Pitch(1)
            case "D":
                return Pitch(2)
            case "D#" | "Eb":
                return Pitch(3)
            case "E":
                return Pitch(4)
            case "F":
                return Pitch(5)
            case "F#" | "Gb":
                return Pitch(6)
            case "G":
                return Pitch(7)
            case "G#" | "Ab":
                return Pitch(8)
            case "A":
                return Pitch(9)
            case "A#" | "Bb":
                return Pitch(10)


class Pitches:
    pitches: list[Pitch]

    def __init__(self, pitches: list[Pitch]):
        self.pitches = pitches

    def __iter__(self) -> Pitch:
        self._iter = iter(self.pitches)
        return self._iter

    def __next__(self) -> Pitch:
        return next(self._iter)

    def cycle(self, n) -> t.Iterable[Pitch]:
        cnt = 0
        for i in itertools.cycle(self.pitches):
            if cnt == n:
                break
            cnt += 1
            yield i

    def reset_octave(self) -> Pitches:
        for p in self.pitches:
            p.octave = 0
        return self

    def sort(self) -> Pitches:
        self.pitches.sort(key=lambda p: (p.number, p.octave))
        return self


def test_pitches():
    ps = Pitches([Pitch(0), Pitch(1), Pitch(2)])
    ps.pitches[0].number == 0
    ps.pitches[1].number == 1

    for i, p in enumerate(ps):
        print("iterate:", i, p)

    for i, p in enumerate(ps.cycle(6)):
        print("cycle:", i, p)
