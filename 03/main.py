import sys
from string import ascii_letters


def get_dup(*strings):
    return set.intersection(*[set(string) for string in strings]).pop()


def part1(input_txt):
    total = 0
    for line in input_txt.splitlines():
        comp1 = line[:len(line)//2]
        comp2 = line[len(line)//2:]
        dup = get_dup(comp1, comp2)
        total += ascii_letters.index(dup) + 1
    return total


def part2(input_txt):
    total = 0
    lines = input_txt.splitlines()
    for group in range(len(lines)//3):
        dup = get_dup(*lines[3*group:3*(group+1)])
        total += ascii_letters.index(dup) + 1
    return total


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
