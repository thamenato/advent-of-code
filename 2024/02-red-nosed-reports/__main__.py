import argparse
from importlib.resources import files

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


def part_one(data):
    safe_count = 0
    for line in data.split("\n"):
        prev_char = None
        ascend = None
        for char in line.split():
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
                    break

                if dist > 0 and ascend:
                    break

                if dist < 0 and not ascend:
                    break

                prev_char = char
        else:
            print(f"Got a safe line: {line}")
            safe_count += 1

    return safe_count


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
