import sys


def part1(input_txt):
    return 


def part2(input_txt):
    return


def main():
    test = "test" in sys.argv
    if test:
        with open("input_test") as f:
            answers = list(map(int, f.readline().split()))
            input_txt = f.read()
    else:
        with open("input") as f:
            input_txt = f.read()

    if test:
        print("Correct answers:", answers)

    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()
