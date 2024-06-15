from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Pitch:
    name: str
    number: int
    octave: int

    hash = [
        (0, "c"),
        (1, "c#"),
        (2, "d"),
        (3, "d#"),
        (4, "e"),
        (5, "f"),
        (6, "f#"),
        (7, "g"),
        (8, "g#"),
        (9, "a"),
        (10, "a#"),
        (11, "b"),
    ]

    num_to_name = {num: name for num, name in hash}
    name_to_num = {name: num for num, name in hash}

    @classmethod
    def new_with_number(cls, number):
        return Pitch(name=cls.num_to_name[number], number=number, octave=0)

    @classmethod
    def new_with_name(cls, name):
        return Pitch(
            name=name,
            number=cls.name_to_num[name],
            octave=0,
        )


def test_pitch():
    c = Pitch.new_with_name("c")
    print(c)
    assert c.number == 0
    assert c.name == "c"

    a = Pitch.new_with_number(9)
    print(a)
    assert a.number == 9
    assert a.name == "a"