import argparse
from importlib.resources import files
from itertools import product

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


def part_one(data):
    result = 0
    _operators = ["+", "*"]

    for line in data.split("\n"):
        total, numbers = line.split(":")
        numbers = numbers.split()

        for attempt in product(_operators, repeat=len(numbers) - 1):
            test = int(numbers[0])
            for i in range(1, len(numbers)):
                match attempt[i - 1]:
                    case "+":
                        test += int(numbers[i])
                    case "*":
                        test *= int(numbers[i])

            if int(total) == test:
                print(f"\tadding={total}")
                result += int(total)
                break

    return result


def part_two(data):
    result = 0
    _operators = ["+", "*", "||"]

    for line in data.split("\n"):
        total, numbers = line.split(":")
        numbers = numbers.split()

        for attempt in product(_operators, repeat=len(numbers) - 1):
            test = int(numbers[0])
            for i in range(1, len(numbers)):
                match attempt[i - 1]:
                    case "+":
                        test += int(numbers[i])
                    case "*":
                        test *= int(numbers[i])
                    case "||":
                        test = int(str(test) + numbers[i])

            if int(total) == test:
                print(f"\tadding={total}")
                result += int(total)
                break

    return result


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
