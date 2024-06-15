from __future__ import annotations
from pitch import Pitch


class Chord:
    def __init__(self, root: Pitch):
        self.root: Pitch = root
        self.pitches: list[Pitch] = [root]

    def major(self) -> Chord:
        self.pitches = self.interval_to_pitches([0, 4, 7])
        return self.sort()

    def minor(self) -> Chord:
        self.pitches = self.interval_to_pitches([0, 3, 7])
        return self.sort()

    def add_n(self, n: int) -> Chord:
        pitch_to_add = Pitch(self.root.number + n)
        self.pitches.append(pitch_to_add)
        return self.sort()

    def add_seventh(self) -> Chord:
        self.add_n(10)
        return self.sort()

    def add_major_seventh(self) -> Chord:
        self.add_n(11)
        return self.sort()

    def add_nineth(self) -> Chord:
        self.add_n(14)
        return self.sort()

    def add_eleventh(self) -> Chord:
        self.add_n(17)
        return self.sort()

    def interval_to_pitches(self, interval: list[int]) -> list[Pitch]:
        pitches = []
        for i in interval:
            pitches.append(Pitch(self.root.number + i))
        return pitches

    def sort(self) -> Pitch:
        self.pitches = sorted(self.pitches, key=lambda x: x.number + x.octave * 12)
        return self


def test_chord():
    c = Chord(Pitch("c"))
    c.major().add_nineth().add_eleventh()
    print(c.pitches)
    assert [n.name for n in c.pitches] == ["c", "e", "g", "d", "f"]

    a = Chord(Pitch("a"))
    a.minor().add_seventh()
    print(a.pitches)
    assert [n.name for n in a.pitches] == ["a", "c", "e", "g"]

    e = Chord(Pitch("e"))
    e.major()
    assert [n.name for n in e.pitches] == ["e", "g#", "b"]
