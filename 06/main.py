import sys


def find_marker(text, n_chars):
    for i in range(len(text)-n_chars):
        chars = set(text[i:i+n_chars])
        if len(chars) == n_chars:
            break
    return i+n_chars


def part1(input_txt):
    return find_marker(input_txt, 4)


def part2(input_txt):
    return find_marker(input_txt, 14)


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
