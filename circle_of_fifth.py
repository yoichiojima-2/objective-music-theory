from dataclasses import dataclass
from pitch import Pitch


@dataclass
class CircleOfFifth:
    cursor: Pitch

    def next(self):
        self.cursor = self.cursor.rel(7).round()
        return self.cursor

    def prev(self):
        self.cursor = self.cursor.rel(-7).round()
        return self.cursor


def test_circle_of_fiftth():
    p = Pitch(0)
    cof = CircleOfFifth(cursor=p)
    print(cof.cursor)
    assert cof.cursor.number == 0
    cof.next()
    print(cof.cursor)
    assert cof.cursor.number == 7
    cof.prev()
    print(cof.cursor)
    assert cof.cursor.number == 0
    cof.prev()
    print(cof.cursor)
    assert cof.cursor.number == 5
