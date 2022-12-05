import sys


def part1(input_txt):
    return 


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
