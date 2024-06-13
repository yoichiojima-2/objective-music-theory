from dataclasses import dataclass

class Note:
    def __init__(self, note: str):
        match note:
            case "c":
                self.note = "c"
            case "c#":
                self.note = "c#"
            case "d":
                self.note = "d"
            case "d#":
                self.note = "d#"
            case "e":
                self.note = "e"
            case "f":
                self.note = "f"
            case "f#":
                self.note = "f#" 
            case "g":
                self.note = "g"
            case "g#":
                self.note = "g#"
            case "a":
                self.note = "a"
            case "a#":
                self.note = "a#"
            case "b":
                self.note = "b"
            case _:
                raise ValueError(f"Invalid note: {note}")

    def to_number(self):
        match self.note:
            case "c":
                return 0
            case "c#":
                return 1
            case "d":
                return 2
            case "d#":
                return 3
            case "e":
                return 4
            case "f":
                return 5
            case "f#":
                return 6
            case "g":
                return 7
            case "g#":
                return 8
            case "a":
                return 9
            case "a#":
                return 10
            case "b":
                return 11
            case _:
                raise ValueError(f"Invalid note: {self.note}")
    
    def triad(self):
        return [
            self.to_number(), 
            (self.to_number() + 4) % 12, 
            (self.to_number() + 7) % 12
        ]

def test_note():
    assert Note("a").to_number() == 9
    assert Note("c").triad() == [0, 4, 7]
