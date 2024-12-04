import argparse
import re
from importlib.resources import files

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")

_re_xmas = re.compile(r"XMAS")


def _check_line(line: str) -> int:
    found = 0
    found += len(_re_xmas.findall(line))
    found += len(_re_xmas.findall(line[::-1]))
    return found


def part_one(data):
    total = 0

    break_line = data.index("\n")
    num_of_lines = len(data.split("\n"))

    # check horizontal
    for line in data.split("\n"):
        total += _check_line(line)

    # check vertical
    for i in range(0, break_line):
        line = "".join([data[c] for c in range(i, len(data), break_line + 1)])
        total += _check_line(line)

    # check diagonal
    for i in range(0, len(data) - num_of_lines * len("XMAS"), num_of_lines + 1):
        for j in range(0, break_line - len("XMAS") + 1):
            line = ""
            for c in range(i + j, len(data), break_line + 2):
                if data[c] == "\n":
                    break
                line += data[c]

            print(line)
            print(f"new_column {j}")

        print(f"new_line {i}")
        # line = "".join([data[c] for c in range(i + j, len(data), break_line + 2)])

    return total


def part_two(data):
    pass


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
