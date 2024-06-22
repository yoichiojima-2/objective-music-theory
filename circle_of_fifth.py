from __future__ import annotation
from dataclasses import dataclass


@dataclass
class CircleOfFifth:
    cursor: Pitch

    def __init__(self, cursor: Pitch):
        self.curosr = Pitch
        
    def next(self) -> CIrcleOfFifth:
        self.cursor = self.cursor.rel(7)
        return self

    def prev(self) -> CIrcleOfFifth:
        self.cursor = self.cursor.rel(-7)
        return self
