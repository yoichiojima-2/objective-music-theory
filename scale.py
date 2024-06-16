from __future__ import annotations
from dataclasses import dataclass
from circle_of_fifth import CircleOfFifth
from pitch import Pitch, Pitches


@dataclass
class Scale:
    root: Pitch
    name: str
    feeling: int
    pitches: Pitches

    scales = [
        ("super-lydian", 2),
        ("lydian", 1),
        ("ionian", 0),
        ("mixolydian", -1),
        ("dorian", -2),
        ("aeolian", -3),
        ("phrygian", -4),
        ("locrian", -5),
        ("super-locrian", -6),
    ]

    name_to_feeling = {name: feeling for name, feeling in scales}
    feeling_to_name = {feeling: name for name, feeling in scales}

    def __init__(self, root: Pitch, feeling: int):
        self.root = root
        self.name = self.feeling_to_name[feeling]
        self.feeling = feeling

        shift = (feeling - 1) * 7
        cof = CircleOfFifth(Pitch(root.number + shift))
        self.pitches = Pitches(cof.pitches[:7]).set_octave(0).sort()

    def __iter__(self):
        return iter(self.pitches)

    def __str__(self):
        return f"{self.root.name} {self.name} \nfeeling:{self.feeling}\npitches:{[p.name for p in self.pitches]}"

    def shift_mood(self, int) -> Scale:
        return Scale(self.root, self.feeling + int)


def test_scale():
    c = Pitch("c")
    c_major = [p.name for p in Scale(root=c, feeling=0)]
    print(c_major)
    assert c_major == ["c", "d", "e", "f", "g", "a", "b"]

    a = Pitch("a")
    a_minor = [p.name for p in Scale(root=a, feeling=-3)]
    print(a_minor)
    assert a_minor == ["c", "d", "e", "f", "g", "a", "b"]


def test_shift_mood():
    c = Pitch("c")
    c_major = [p.name for p in Scale(root=c, feeling=0)]
    print(c_major)
    assert c_major == ["c", "d", "e", "f", "g", "a", "b"]

    c_major = [p.name for p in Scale(root=c, feeling=0).shift_mood(-1)]
    print(c_major)
    assert c_major == ["c", "d", "e", "f", "g", "a", "a#"]
