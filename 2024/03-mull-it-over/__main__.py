import argparse
import re
from importlib.resources import files

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")

_re_mul = re.compile(r"mul\((?P<left>\d{0,3}),(?P<right>\d{0,3})\)")
_re_do = re.compile(r"don\'t\(\)|do\(\)")


def part_one(data):
    groups = _re_mul.findall(data)
    total = 0
    for g in groups:
        total += int(g[0]) * int(g[1])

    return total


def part_two(data):
    modes = _re_do.finditer(data)
    just_do = True

    strings = []
    pivot = 0
    for m in modes:
        if m.group() == "don't()":
            if just_do:
                strings.append(data[pivot : m.start()])
                pivot = m.end()
                just_do = False
            else:
                pivot = m.end()
        if m.group() == "do()":
            if just_do:
                strings.append(data[pivot : m.start()])
                pivot = m.end()
            else:
                pivot = m.end()
                just_do = True

    strings.append(data[pivot:])

    total = 0
    for s in strings:
        for g in _re_mul.findall(s):
            total += int(g[0]) * int(g[1])

    return total


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
