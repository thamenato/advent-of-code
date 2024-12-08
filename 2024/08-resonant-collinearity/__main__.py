import argparse
import itertools
import math
import re
from dataclasses import astuple, dataclass
from importlib.resources import files

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


@dataclass
class Point:
    row: int
    col: int

    def __add__(self, other):
        return Point(row=self.row + other.row, col=self.col + other.col)

    def __sub__(self, other):
        return Point(row=self.row - other.row, col=self.col - other.col)


class Map:
    _re_antennas = re.compile(r"[^\.]")

    def __init__(self, data):
        self._chart = data.split("\n")
        self._max_row = len(self._chart)
        self._max_col = len(self._chart[0])
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
                point = Point(row=i, col=m.start())
                if m.group() in antennas:
                    antennas[m.group()].append(point)
                else:
                    antennas[m.group()] = [point]

        return antennas

    def out_of_bounds(self, point):
        if point.row < 0 or point.col < 0:
            return True

        if point.row >= self._max_row or point.col >= self._max_col:
            return True

        return False


def part_one(data):
    my_map = Map(data)

    locations = set()
    for points in my_map.antennas.values():
        line_list = list(itertools.combinations(points, 2))
        for line in line_list:
            slope = line[1] - line[0]

            attempt = line[0] - slope

            if not my_map.out_of_bounds(attempt):
                locations.add(astuple(attempt))

            attempt = line[1] + slope

            if not my_map.out_of_bounds(attempt):
                locations.add(astuple(attempt))

    return len(locations)


def part_two(data):
    my_map = Map(data)

    locations = set()

    for points in my_map.antennas.values():
        line_list = list(itertools.combinations(points, 2))
        for line in line_list:
            locations.add(astuple(line[0]))
            locations.add(astuple(line[1]))
            slope = line[1] - line[0]

            attempt = line[0] - slope
            while not my_map.out_of_bounds(attempt):
                print(attempt)
                locations.add(astuple(attempt))
                attempt = attempt - slope

            attempt = line[1] + slope
            while not my_map.out_of_bounds(attempt):
                print(attempt)
                locations.add(astuple(attempt))
                attempt = attempt + slope

    return len(locations)


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
