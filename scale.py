from pitch import Pitch
from circle_of_fifth import CircleOfFifth


class Scale:
    def __init__(self, root: Pitch, feeling: int, length: int = 7):
        cof = CircleOfFifth(cursor=root)

        for _ in range(feeling * -1 + 1):
            cof.prev()

        notes = [cof.cursor.round().number]
        for _ in range(length - 1):
            cof.next()
            notes.append(cof.cursor.round().number)

        self.root = root
        self.notes = sorted(notes)


def test_scale():
    p = Pitch(0)
    ionian = Scale(root=p, feeling=0, length=7)
    print("ionian:", ionian.notes)
    assert ionian.notes == [0, 2, 4, 5, 7, 9, 11]

    aeolian = Scale(root=p, feeling=-3, length=7)
    print("aeolian:", aeolian.notes)
    assert aeolian.notes == [0, 2, 3, 5, 7, 8, 10]

    pentatonic = Scale(root=p, feeling=1, length=5)
    print("pentatonic:", pentatonic.notes)
    assert pentatonic.notes == [0, 2, 4, 7, 9]