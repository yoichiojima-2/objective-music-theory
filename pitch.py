from dataclasses import dataclass


@dataclass
class Pitch:
    number: int

    def rel(self, shift):
        return Pitch(self.number + shift)

    def round(self):
        pitch = self.number
        while pitch <= 0:
            pitch += 12
        return Pitch(pitch % 12)


def test_pitch():
    p = Pitch(0)
    assert p.number == 0
    print(p.number)

    p2 = p.rel(7)
    assert p2.number == 7
    print(p2.number)
