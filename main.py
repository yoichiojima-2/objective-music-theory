import time
from note import Note

def main():
    c = Note(note = "c")
    d = Note(note = "d")
    e = Note(note = "e")
    f = Note(note = "f")
    g = Note(note = "g")
    a = Note(note = "a")
    b = Note(note = "b")

    print([n.note for n in c.major])
    time.sleep(1)
    print([n.note for n in a.minor])
    time.sleep(1)
    print([n.note for n in f.major])
    time.sleep(1)
    print([n.note for n in f.minor] + [f.seventh.note])
    time.sleep(1)


main()