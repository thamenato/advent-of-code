import argparse
import re
from dataclasses import dataclass
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


def _get_diagonals(text: str):
    break_line = text.index("\n")
    num_of_lines = len(text.split("\n"))

    diagonals = []
    for row in range(0, num_of_lines - 4):
        line = ""
        char_idx = row * break_line + row
        for i in range(0, break_line):
            line += text[char_idx]
            char_idx += break_line + 2
            if char_idx >= len(text):
                break

        diagonals.append(line)

    for col in range(1, break_line - 3):
        line = ""
        char_idx = col
        for i in range(0, break_line - col):
            line += text[char_idx]
            char_idx += break_line + 2
        diagonals.append(line)

    return diagonals


def part_one(data):
    total = 0

    break_line = data.index("\n")

    # check horizontal
    for line in data.split("\n"):
        total += _check_line(line)

    # check vertical
    for row in range(0, break_line):
        line = "".join([data[c] for c in range(row, len(data), break_line + 1)])
        total += _check_line(line)

    # check diagonals
    for line in _get_diagonals(data):
        total += _check_line(line)

    mirror = "\n".join([l[::-1] for l in data.split()])
    for line in _get_diagonals(mirror):
        total += _check_line(line)

    return total


def part_two(data):
    _re_mas = re.compile(r"MAS|SAM")
    matrix = data.split()

    found = 0
    for i, line in enumerate(matrix):
        if i < 1 or i > len(matrix) - 2:
            continue
        for a in re.finditer("A", line):
            try:
                left = f"{matrix[i - 1][a.start() - 1]}{matrix[i][a.start()]}{matrix[i + 1][a.start() + 1]}"
                right = f"{matrix[i + 1][a.start() - 1]}{matrix[i][a.start()]}{matrix[i - 1][a.start() + 1]}"

                if _re_mas.match(left) and _re_mas.match(right):
                    found += 1
            except IndexError:
                continue

    return found


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
