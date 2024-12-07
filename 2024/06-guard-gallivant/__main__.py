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


class Visited:
    def __init__(self):
        self._visited = set()
        self._row = dict()
        self._col = dict()

    def append(self, position):
        self._visited.add(astuple(position))

        if position.row in self._row:
            self._row[position.row].append(position.col)
        else:
            self._row[position.row] = [position.col]

        if position.col in self._col:
            self._col[position.col].append(position.row)
        else:
            self._col[position.col] = [position.row]

    def visited_rows_at_col(self, col):
        return self._col.get(col, [])

    def visited_cols_at_row(self, row):
        return self._row.get(row, [])

    @property
    def visited(self):
        return self._visited

    @property
    def total_visited(self):
        return len(self._visited)


def _find_guard(data):
    _re_guard = re.compile(r"[\^><V]")

    for i, line in enumerate(data.split("\n")):
        match = _re_guard.search(line)
        if match:
            return Guard(
                orientation=Orientation(match.group()),
                position=Position(col=match.start(), row=i),
            )


class Map:
    def __init__(self, data):
        self._the_map = data.split("\n")
        self._max_row = len(self._the_map)
        self._max_col = len(self._the_map[0])

    @property
    def matrix(self):
        return self._the_map

    def is_out_of_bounds(self, position: Position):
        if position.row < 0 or position.row >= self._max_row:
            return True

        if position.col < 0 or position.col >= self._max_col:
            return True

        return False

    def get_spot(self, pos: Position):
        return self._the_map[pos.row][pos.col]

    def has_obstruction(self, guard, mode, idx):
        found = False
        match mode:
            case "row":
                if guard.orientation == Orientation.UP:
                    start = guard.position.col + 1
                    end = self._max_col
                else:
                    start = 0
                    end = guard.position.col - 1

                if "#" in self._the_map[idx][start:end]:
                    found = True
            case "col":
                if guard.orientation == Orientation.LEFT:
                    start = 0
                    end = guard.position.row - 1
                else:
                    start = guard.position.row + 1
                    end = self._max_row

                for row in range(start, end):
                    if "#" in self._the_map[row][idx]:
                        found = True

        return found


def part_one(data, visited=False):
    guard = _find_guard(data)
    the_map = Map(data)
    visited = Visited()

    visited.append(guard.position)

    next_step = guard.get_next_step()
    while not the_map.is_out_of_bounds(next_step):
        spot = the_map.get_spot(next_step)
        if spot == "#":
            guard.rotate()
        else:
            visited.append(next_step)
            guard.move_to(next_step)

        next_step = guard.get_next_step()

    return visited.total_visited


def part_two(data):
    guard = _find_guard(data)
    the_map = Map(data)
    visited = Visited()

    visited.append(guard.position)

    def _check_possibilities():
        next_step = guard.get_next_step()

        if guard.orientation in [Orientation.UP, Orientation.DOWN]:
            i = next_step.row
            if guard.orientation == Orientation.UP:
                check = next_step.col + 1
                offset = -1
            else:
                check = next_step.col - 1
                offset = 1
            if (i, check) in visited.visited:
                if the_map.has_obstruction(guard, mode="row", idx=i):
                    print(f"trying_at={i + offset},{guard.position.col}")
                    if the_map.matrix[i + offset][guard.position.col] != "#":
                        print("\tcorrect")
                        return 1
        else:
            i = next_step.col
            if guard.orientation == Orientation.LEFT:
                check = next_step.row - 1
                offset = -1
            else:
                check = next_step.row + 1
                offset = 1
            if (check, i) in visited.visited:
                if the_map.has_obstruction(guard, mode="col", idx=i):
                    print(f"trying_at={guard.position.row},{i + offset}")
                    if the_map.matrix[guard.position.row][i + offset] != "#":
                        print("\tcorrect")
                        return 1

        return 0

    rotated = 0
    next_step = guard.get_next_step()
    obstructions = 0
    while not the_map.is_out_of_bounds(next_step):
        print(guard.orientation)
        if rotated >= 3:
            obstructions += _check_possibilities()

        spot = the_map.get_spot(next_step)
        if spot == "#":
            guard.rotate()
            rotated += 1
        else:
            visited.append(next_step)
            guard.move_to(next_step)

        next_step = guard.get_next_step()

    return obstructions


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
