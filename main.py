from pitch import Pitch
from scale import Scale
from chord import Chord


def main():
    # start witth c major
    print("building c major scale")
    c = Pitch("c")
    scale = Scale(root=c, feeling=0)
    print(scale)

    # make it a lot sadder
    print("get sadder scale")
    scale_shifted = scale.shift_mood(-3)
    print(scale_shifted)

    # c major 9th
    print("building c major 9th chord")
    print(Chord(c).major().add_nineth())


if __name__ == "__main__":
    main()
