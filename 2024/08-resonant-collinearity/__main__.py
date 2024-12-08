import argparse
import re
from importlib.resources import files

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


class Map:
    _re_antennas = re.compile(r"[^\.]")

    def __init__(self, data):
        self._chart = data.split("\n")
        self._edge = len(self._chart)
        self.antennas = self._find_antennas()

    @property
    def edge(self):
        return self._edge

    @property
    def chart(self):
        return self._chart

    def _find_antennas(self):
        antennas = {}
        for i, line in enumerate(self.chart):
            for m in self._re_antennas.finditer(line):
                if m.group() in antennas:
                    antennas[m.group()].append((i, m.start()))
                else:
                    antennas[m.group()] = [(i, m.start())]

        return antennas


def part_one(data):
    my_map = Map(data)
    print(my_map.antennas)


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
