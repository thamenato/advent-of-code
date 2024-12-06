import argparse
import re
from dataclasses import astuple, dataclass
from enum import Enum
from importlib.resources import files

from IPython import embed

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int)
parser.add_argument("filename")


class Orientation(Enum):
    UP = "^"
    DOWN = "V"
    LEFT = "<"
    RIGHT = ">"


@dataclass
class Position:
    row: int
    col: int


@dataclass
class Guard:
    orientation: Orientation
    position: Position

    def get_next_step(self) -> Position:
        match self.orientation:
            case Orientation.UP:
                return Position(col=self.position.col, row=self.position.row - 1)
            case Orientation.DOWN:
                return Position(col=self.position.col, row=self.position.row + 1)
            case Orientation.LEFT:
                return Position(col=self.position.col - 1, row=self.position.row)
            case Orientation.RIGHT:
                return Position(col=self.position.col + 1, row=self.position.row)

    def move_to(self, position: Position):
        self.position = position

    def rotate(self):
        match self.orientation:
            case Orientation.UP:
                self.orientation = Orientation.RIGHT
            case Orientation.RIGHT:
                self.orientation = Orientation.DOWN
            case Orientation.DOWN:
                self.orientation = Orientation.LEFT
            case Orientation.LEFT:
                self.orientation = Orientation.UP


def _find_guard(data):
    _re_guard = re.compile(r"[\^><V]")

    for i, line in enumerate(data.split("\n")):
        match = _re_guard.search(line)
        if match:
            return Guard(
                orientation=Orientation(match.group()),
                position=Position(col=match.start(), row=i),
            )


def part_one(data):
    guard = _find_guard(data)

    the_map = data.split("\n")
    visited = {astuple(guard.position)}

    max_row = len(the_map)
    max_col = len(the_map[0])

    def _is_out_of_bounds(position: Position):
        if position.row < 0 or position.col < 0:
            return True

        if position.row > max_row or position.col > max_col:
            return True

        return False

    next_step = guard.get_next_step()
    while not _is_out_of_bounds(next_step):
        spot = the_map[next_step.row][next_step.col]
        if spot == "#":
            guard.rotate()
        else:
            visited.add(astuple(next_step))
            guard.move_to(next_step)

        next_step = guard.get_next_step()

    return len(visited)


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
