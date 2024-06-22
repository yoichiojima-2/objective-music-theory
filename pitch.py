from dataclasses import dataclass
import itertools

@dataclass
class Pitch:
    number: int
    octave: int


class Pitches:
    pitches: list[Pitch]

    def __iter__(self) -> Pitch:
        pass

    def __next__(self) -> Pitch:
        pass

    def cycle(self, n: int) -> Pitch:
        for i in itertools.cycle(self.pitches):
            yield i