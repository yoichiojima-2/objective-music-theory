class Note:
    def __init__(self, note: str = None, number: int = None):
        if note is not None and number is not None:
            raise ValueError("Cannot specify both note and number")

        if note is not None:
            self.note = note

            match note:
                case "c":
                    self.number = 0
                case "c#":
                    self.number = 1
                case "d":
                    self.number = 2
                case "d#":
                    self.number = 3
                case "e":
                    self.number = 4
                case "f":
                    self.number = 5
                case "f#":
                    self.number = 6
                case "g":
                    self.number = 7
                case "g#":
                    self.number = 8
                case "a":
                    self.number = 9
                case "a#":
                    self.number = 10
                case "b":
                    self.number = 11

        if number is not None:
            self.number = number

            match number:
                case 0:
                    self.note = "c"
                case 1:
                    self.note = "c#"
                case 2:
                    self.note = "d"
                case 3:
                    self.note = "d#"
                case 4:
                    self.note = "e"
                case 5:
                    self.note = "f"
                case 6:
                    self.note = "f#"
                case 7:
                    self.note = "g"
                case 8:
                    self.note = "g#"
                case 9:
                    self.note = "a"
                case 10:
                    self.note = "a#"
                case 11:
                    self.note = "b"

    @property
    def major(self):
        return self.intervals_to_chords([0, 4, 7])

    @property
    def minor(self):
        return self.intervals_to_chords([0, 3, 7])

    @property
    def sus2(self):
        return self.intervals_to_chords([0, 2, 7])

    @property
    def sus4(self):
        return self.intervals_to_chords([0, 5, 7])

    @property
    def seventh(self):
        return Note(number=(self.number + 10) % 12)

    @property
    def major_seventh(self):
        return Note(number=(self.number + 11) % 12)

    @property
    def ninth(self):
        return Note(number=(self.number + 2) % 12)

    @property
    def eleventh(self):
        return Note(number=(self.number + 5) % 12)

    def intervals_to_chords(self, intervals):
        notes = []
        for i in intervals:
            notes.append(Note(number=(self.number + i) % 12))
        return notes


def test_note():
    assert Note(note="c").number == 0
    assert Note(note="c").note == "c"
    assert Note(number=0).number == 0
    assert Note(number=0).note == "c"


def test_major():
    assert [i.note for i in Note(note="c").major] == ["c", "e", "g"]


def test_minor():
    assert [i.note for i in Note(note="c").minor] == ["c", "d#", "g"]


def test_sus2():
    assert [i.note for i in Note(note="c").sus2] == ["c", "d", "g"]


def test_sus4():
    assert [i.note for i in Note(note="c").sus4] == ["c", "f", "g"]


def test_seventh():
    assert Note(note="c").seventh.note == "a#"


def test_major_seventh():
    assert Note(note="c").major_seventh.note == "b"


def test_ninth():
    assert Note(note="c").ninth.note == "d"


def test_eleventh():
    assert Note(note="c").eleventh.note == "f"
