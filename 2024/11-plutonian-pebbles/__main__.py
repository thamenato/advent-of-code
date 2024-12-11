import argparse
from dataclasses import dataclass
from importlib.resources import files

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


def _process_stone(value):
    if int(value) == 0:
        return ["1"]

    if len(value) % 2 == 0:
        size = int(len(value))
        half = int(size / 2)
        left = value[:half]
        right = str(int(value[half:]))  # remove trailing zeroes
        return [left, right]

    value = str(int(value) * 2024)
    return [value]


# def _process_blink(stone_list):
#     after_blink = {}
#     for value in stone_list:
#         if value in after_blink:
#             after_blink[value] += 1

#         stones = _process_stone(value)
#         after_blink += processed

#     result = after_blink.copy()


def part_one(data):
    blinks = 25

    result = data.split()
    for i in range(0, blinks):
        after_blink = []
        for stone in result:
            processed = _process_stone(stone)
            after_blink += processed

        result = after_blink.copy()

    return len(result)


def part_two(data):
    blinks = 25

    result = data.split()
    for i in range(0, blinks):
        after_blink = []
        for stone in result:
            processed = _process_stone(stone)
            after_blink += processed

        result = after_blink.copy()
    return len(result)


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
