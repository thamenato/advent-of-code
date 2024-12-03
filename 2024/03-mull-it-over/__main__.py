import argparse
import re
from importlib.resources import files

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


def part_one(data):
    groups = re.findall(r"mul\((?P<left>\d{0,3}),(?P<right>\d{0,3})\)", data)
    total = 0
    for g in groups:
        total += int(g[0]) * int(g[1])

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
