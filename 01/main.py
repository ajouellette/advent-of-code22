import sys


def calories(input_txt):
    cals = []
    for elf in input_txt.split("\n\n"):
        total = 0
        for cal in elf.split():
            total += int(cal)
        cals.append(total)
    return cals


def part1(input_txt):
    return max(calories(input_txt))


def part2(input_txt):
    cals = calories(input_txt)
    maxs = []
    for i in range(3):
        top = max(cals)
        maxs.append(top)
        cals.remove(top)
    return sum(maxs)


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "input"
    with open("input") as f:
        input_txt = f.read()

    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()
