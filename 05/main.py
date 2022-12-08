import sys
from string import ascii_uppercase


def read_initial(initial):
    lines = initial.splitlines()
    n_cols = len(lines[-1].split())
    cols = [[] for i in range(n_cols)]
    for line in lines[-2::-1]:
        for i, c in enumerate(line):
            if c in ascii_uppercase:
                col_i = (i-1) // 4
                cols[col_i].append(c)
    return cols


def get_top_crates(cols):
    return ''.join([col[-1] for col in cols])


def part1(input_txt):
    initial, moves = input_txt.split("\n\n")
    cols = read_initial(initial)
    for move in moves.splitlines():
        move = move.split()
        num, src, dest = map(int, [move[1], move[3], move[5]])
        for i in range(num):
            cols[dest-1].append(cols[src-1].pop())
    return get_top_crates(cols)


def part2(input_txt):
    initial, moves = input_txt.split("\n\n")
    cols = read_initial(initial)
    for move in moves.splitlines():
        move = move.split()
        num, src, dest = map(int, [move[1], move[3], move[5]])
        cols[dest-1] += cols[src-1][-num:]
        del cols[src-1][-num:]
    return get_top_crates(cols)


def main():
    test = "test" in sys.argv
    if test:
        with open("input_test") as f:
            answers = f.readline().split()
            input_txt = f.read()
    else:
        with open("input") as f:
            input_txt = f.read()

    if test:
        print("Correct answers:", *answers)

    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()
