from dataclasses import dataclass


@dataclass
class Pitch:
    root: int

    def rel(self, shift):
        return Pitch(self.root + shift)

    def round(self):
        pitch = self.root
        while pitch < 0:
            pitch += 12
        return Pitch(pitch % 12)


def test_pitch():
    p = Pitch(0)
    assert p.root == 0
    print(p.root)

    p2 = p.rel(7)
    assert p2.root == 7
    print(p2.root)
