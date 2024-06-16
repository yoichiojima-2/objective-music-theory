from __future__ import annotations
from pitch import Pitch


class CircleOfFifth:
    def __init__(self, root: Pitch):
        self.root: Pitch = root
        self.pitches: list[Pitch] = [Pitch(root.number + i * 7) for i in range(12)]

    def __getitem__(self, index: int) -> Pitch:
        return self.pitches[index]


def test_circle_of_fifth():
    c = CircleOfFifth(Pitch("c"))
    print([n.name for n in c.pitches])
    assert [n.name for n in c.pitches] == [
        "c",
        "g",
        "d",
        "a",
        "e",
        "b",
        "f#",
        "c#",
        "g#",
        "d#",
        "a#",
        "f",
    ]
    assert c[1].name == "g"

    a = CircleOfFifth(Pitch("a"))
    print([n.name for n in a.pitches])
    assert [n.name for n in a.pitches] == [
        "a",
        "e",
        "b",
        "f#",
        "c#",
        "g#",
        "d#",
        "a#",
        "f",
        "c",
        "g",
        "d",
    ]
    assert a[2].name == "b"
