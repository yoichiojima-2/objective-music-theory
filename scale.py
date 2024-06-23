from pitch import Pitch, Pitches
from circle_of_fifth import CircleOfFifth
from dataclasses import dataclass


@dataclass
class Scale:
    root: Pitch
    pitches: Pitches
    feeling: int
    length: int

    def __init__(self, root: Pitch, feeling: int, length: int = 7):
        self.root = root
        self.feeling = feeling
        self.length = length

        cof = CircleOfFifth(cursor=root)

        for _ in range(feeling * -1 + 1):
            cof.prev()

        notes = [cof.cursor]
        for _ in range(length - 1):
            cof.next()
            notes.append(cof.cursor)

        self.pitches = Pitches(notes)


def test_scale():
    s = Scale(Pitch(0), feeling=0)
    print([i.number for i in s.pitches])
