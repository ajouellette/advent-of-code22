import sys


def get_ranges(pair_str):
    pair = pair_str.split(',')
    return [list(map(int, elf.split('-'))) for elf in pair]


def part1(input_txt):
    total = 0
    for line in input_txt.splitlines():
        elf1, elf2 = get_ranges(line)
        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            total += 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            total += 1
    return total


def part2(input_txt):
    total = 0
    for line in input_txt.splitlines():
        elf1, elf2 = get_ranges(line)
        if elf1[0] <= elf2[1] and elf1[0] >= elf2[0]:
            total += 1
        elif elf2[0] <= elf1[1] and elf2[0] >= elf1[0]:
            total += 1
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
