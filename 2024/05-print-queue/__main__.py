import argparse
from importlib.resources import files

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


def _process_input(data):
    data_split = data.split("\n")
    empty_line_index = data_split.index("")

    rules = data_split[0:empty_line_index]
    page_numbers = [p for p in data_split[empty_line_index + 1 :] if p]

    return rules, page_numbers


def _process_rules(rules: list[str]) -> dict[str, str]:
    rules_dict = {}
    for r in rules:
        k, v = r.split("|")
        if k in rules_dict:
            rules_dict[k].append(v)
        else:
            rules_dict[k] = [v]

    return rules_dict


def part_one(data):
    rules, page_numbers = _process_input(data)

    rules_dict = _process_rules(rules)

    proper_lines = []
    for page in page_numbers:
        number_list = page.split(",")
        for i, number in enumerate(number_list):
            before = number_list[:i]
            num_rules = rules_dict.get(number, [])

            if before and before[-1] in num_rules:
                break
        else:
            proper_lines.append(number_list)
        continue

    total = 0
    for line in proper_lines:
        idx = int(len(line) / 2)
        total += int(line[idx])

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
