from __future__ import annotations
from dataclasses import dataclass
from pitch import Pitch
from scale import Scale


@dataclass
class Chord:
    root: Pitch
    notes: list[int]
    scale: Scale

    def __init__(self, root: int, stack: int, scale: Scale) -> Chord:
        self.root = Pitch(root)
        self.scale = scale

        notes = []
        for i in range(0, stack + 2, 2):
            notes.append(scale.notes[i])

        self.notes = notes

    def add_nth(self, n: int) -> Chord:
        self.notes.append(self.scale.notes[n])
        return self


def test_chord():
    p = Pitch(0)
    ionian = Scale(root=p, feeling=0, length=7)
    major = Chord(root=0, stack=3, scale=ionian)
    print("major:", major.notes)
    assert major.notes == [0, 4, 7]

    aeolian = Scale(root=p, feeling=-3, length=7)
    minor = Chord(root=0, stack=3, scale=aeolian)
    print("minor:", minor.notes)
    assert minor.notes == [0, 3, 7]
