from dataclasses import dataclass


@dataclass
class Pitch:
    root: int

    def rel(self, shift):
        return Pitch(self.root + shift)

    def round(self):
        if self.root >= 0:
            return Pitch(self.root % 12)
        else:
            return Pitch((self.root + 12) % 12)


def test_pitch():
    p = Pitch(0)
    assert p.root == 0
    print(p.root)

    p2 = p.rel(7)
    assert p2.root == 7
    print(p2.root)
