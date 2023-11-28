from util import models


def main():
    Puzzle = models.Puzzle("01")
    print(Puzzle.data)


if __name__ == "__main__":
    main()