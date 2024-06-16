from __future__ import annotations
from pitch import Pitch


class CircleOfFifth:
    def __init__(self, root: Pitch):
        self.root = root
        self.pitches = [Pitch(root.number + i * 7) for i in range(12)]


def test_circle_of_fifth():
    c = CircleOfFifth(Pitch("c"))
    print([n.name for n in c.pitches])
    assert [n.name for n in c.pitches] == ["c", "g", "d", "a", "e", "b", "f#", "c#", "g#", "d#", "a#", "f"]

    a = CircleOfFifth(Pitch("a"))
    print([n.name for n in a.pitches])
    assert [n.name for n in a.pitches] == ["a", "e", "b", "f#", "c#", "g#", "d#", "a#", "f", "c", "g", "d"]