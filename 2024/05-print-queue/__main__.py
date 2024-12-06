import argparse
from importlib.resources import files

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


def _process_input(data):
    data_split = data.split("\n")
    empty_line_index = data_split.index("")

    rules = data_split[0:empty_line_index]
    page_numbers = [p for p in data_split[empty_line_index + 1 :] if p]

    return _process_rules(rules), page_numbers


def _process_rules(rules: list[str]) -> dict[str, str]:
    rules_dict = {}
    for r in rules:
        k, v = r.split("|")
        if k in rules_dict:
            rules_dict[k].append(v)
        else:
            rules_dict[k] = [v]

    return rules_dict


def _get_lines(data, good_ones=True):
    rules, page_numbers = _process_input(data)

    good_lines = []
    bad_lines = []
    for page in page_numbers:
        number_list = page.split(",")
        for i, number in enumerate(number_list):
            before = number_list[:i]
            num_rules = rules.get(number, [])

            if before and before[-1] in num_rules:
                bad_lines.append(number_list)
                break
        else:
            good_lines.append(number_list)
        continue

    return good_lines if good_ones else bad_lines


def _get_total(lines):
    total = 0
    for line in lines:
        idx = int(len(line) / 2)
        total += int(line[idx])

    return total


def part_one(data):
    proper_lines = _get_lines(data)

    return _get_total(proper_lines)


def part_two(data):
    bad_lines = _get_lines(data, good_ones=False)
    rules, _ = _process_input(data)

    ordered_list = []
    for line in bad_lines:
        unordered = True
        while unordered:
            for i in range(0, len(line)):
                number = line[i]
                before = line[:i]
                num_rules = rules.get(number, [])

                if before and before[-1] in num_rules:
                    tmp = line[i - 1]
                    line[i - 1] = number
                    line[i] = tmp
                    break
            else:
                unordered = False
                ordered_list.append(line)

    return _get_total(ordered_list)


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
