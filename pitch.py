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

    def __init__(self, arg):
        match arg:
            case int():
                self.name = self.num_to_name[arg % 12]
                self.number = arg % 12
                self.octave = arg // 12
            case str():
                self.name = arg
                self.number = self.name_to_num[arg]
                self.octave = 0
            case _:
                raise ValueError("Invalid argument")


def test_pitch():
    c = Pitch("c")
    print(c)
    assert c.number == 0
    assert c.name == "c"

    a = Pitch(9)
    print(a)
    assert a.number == 9
    assert a.name == "a"
