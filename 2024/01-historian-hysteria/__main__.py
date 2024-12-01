import argparse
from importlib.resources import files

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("part", type=int)


def _split_input(data: str) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for i, v in enumerate(data.split()):
        if i % 2 == 0:
            left.append(int(v))
        else:
            right.append(int(v))

    return left, right


def part_one(left: list[int], right: list[int]) -> int:
    left = sorted(left)
    right = sorted(right)

    distance = 0
    for i in range(len(left)):
        distance += abs(left[i] - right[i])

    return distance


def part_two(left: list[int], right: list[int]) -> int:
    left = sorted(left)
    right = sorted(right)

    def _get_frequency(my_list: list[int]) -> dict[int, int]:
        frequency = {}
        for value in my_list:
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1

        return frequency

    score = 0

    left_freq = _get_frequency(left)
    right_freq = _get_frequency(right)

    for k, v in left_freq.items():
        if k in right_freq:
            score += v * k * right_freq[k]

    return score


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()
    left, right = _split_input(data)

    if args.part == 1:
        print(part_one(left, right))
    if args.part == 2:
        print(part_two(left, right))


if __name__ == "__main__":
    main()
