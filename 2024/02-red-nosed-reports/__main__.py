import argparse
from dataclasses import dataclass
from importlib.resources import files

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


@dataclass
class LineSafe:
    is_safe: bool
    err_index: int | None


def _is_line_safe(line, index_removal=None) -> LineSafe:
    prev_char = None
    ascend = None
    numbers = line.split()
    if index_removal is not None:
        numbers.pop(index_removal)

    for index, char in enumerate(numbers):
        if not prev_char:
            prev_char = char
        else:
            dist = int(prev_char) - int(char)
            if ascend is None:
                if dist < 0:
                    ascend = True
                else:
                    ascend = False

            if abs(dist) > 3 or abs(dist) < 1:
                return LineSafe(False, index)

            if dist > 0 and ascend:
                return LineSafe(False, index)

            if dist < 0 and not ascend:
                return LineSafe(False, index)

            prev_char = char

    return LineSafe(True, None)


def part_one(data):
    safe_count = 0
    for line in data.split("\n"):
        if _is_line_safe(line).is_safe:
            safe_count += 1

    return safe_count


def part_two(data):
    safe_count = 0
    for line in data.split("\n"):
        result = _is_line_safe(line)
        if result.is_safe:
            safe_count += 1
        else:
            retrial = range(0, len(line.split()))

            for r in retrial:
                if _is_line_safe(line, r).is_safe:
                    safe_count += 1
                    break

    return safe_count


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
