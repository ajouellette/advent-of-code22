import sys


def score(round):
    shape = {'X': 1, 'Y': 2, 'Z': 3}
    win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    opponent, self = round.split()
    total = shape[self]
    if win[self] == opponent:
        total += 6
    elif draw[self] == opponent:
        total += 3
    return total


def part1(input_txt):
    total = 0
    for round in input_txt.splitlines():
        total += score(round)
    return total


def part2(input_txt):
   return


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "input"
    with open(file) as f:
        input_txt = f.read()

    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()
