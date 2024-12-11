import argparse
from dataclasses import dataclass
from importlib.resources import files

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


@dataclass
class Stone:
    value: str
    count: int


def _process_stone(stone):
    if int(stone.value) == 0:
        return [Stone("1", stone.count)]

    if len(stone.value) % 2 == 0:
        size = int(len(stone.value))
        half = int(size / 2)
        left = Stone(stone.value[:half], stone.count)
        right = Stone(
            str(int(stone.value[half:])), stone.count
        )  # remove trailing zeroes
        return [left, right]

    value = Stone(str(int(stone.value) * 2024), stone.count)
    return [value]


def _process_blink(stone_list):
    after_blink = []
    for stone in stone_list:
        after_blink += _process_stone(stone)

    seen = {}
    for stone in after_blink:
        if stone.value in seen:
            seen[stone.value] += stone.count
        else:
            seen[stone.value] = stone.count

    return [Stone(k, v) for k, v in seen.items()]


def part_one(data):
    blinks = 25

    stone_list = [Stone(v, 1) for v in data.split()]
    for i in range(0, blinks):
        stone_list = _process_blink(stone_list)

    total = 0
    for stone in stone_list:
        total += stone.count

    return total


def part_two(data):
    blinks = 75

    stone_list = [Stone(v, 1) for v in data.split()]
    for i in range(0, blinks):
        stone_list = _process_blink(stone_list)

    total = 0
    for stone in stone_list:
        total += stone.count

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
