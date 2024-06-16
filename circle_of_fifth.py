from dataclasses import dataclass
from pitch import Pitch


@dataclass
class CircleOfFifth:
    @staticmethod
    def next(pitch: Pitch):
        return pitch.rel(7).round()

    @staticmethod
    def prev(pitch: Pitch):
        return pitch.rel(-7).round()


def test_circle_of_fiftth():
    p = Pitch(0)
    assert CircleOfFifth.next(p).root == 7
    assert CircleOfFifth.prev(p).root == 5
    print(CircleOfFifth.next(p).root)
    print(CircleOfFifth.prev(p).root)
