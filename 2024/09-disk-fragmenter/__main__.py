import argparse
import math
import re
from dataclasses import dataclass
from importlib.resources import files

parser = argparse.ArgumentParser()

parser.add_argument("part", type=int)
parser.add_argument("filename")


@dataclass
class File:
    id_: int
    size: int
    start: int
    end: int


class Disk:
    def __init__(self, data):
        self._disk = []
        self._file_map = {}
        file_id = 0
        for i in range(0, len(data)):
            value = int(data[i])
            if i % 2 == 0:
                self._file_map[file_id] = File(
                    file_id, value, len(self._disk), len(self._disk) + value
                )
                self._disk += [file_id for _ in range(value)]
                file_id += 1
            elif value != 0:
                self._disk += ["." for _ in range(value)]

    @property
    def disk(self):
        return "".join([str(c) for c in self._disk])

    @property
    def file_map(self):
        return self._file_map

    def defrag(self):
        pivot = len(self._disk) - 1
        i = 0

        while i < pivot:
            if self._disk[i] == ".":
                if self._disk[pivot] != ".":
                    value = self._disk[pivot]
                    self._disk[i] = value
                    self._disk[pivot] = "."

                    pivot -= 1
                else:
                    pivot -= 1
            else:
                i += 1

    def defrag_chunky(self):
        _re = re.compile(r"\.+")
        file_id = math.inf

        for i in range(1, len(self._disk)):
            value = self._disk[-i]
            if value != ".":
                file_id = value
                break

        for i in range(file_id, 0, -1):
            file_ = self._file_map[i]
            for empty_spaces in _re.finditer(self.disk[: file_.start]):
                if len(empty_spaces.group()) >= file_.size:
                    for j in range(
                        empty_spaces.start(), empty_spaces.start() + file_.size
                    ):
                        self._disk[j] = i

                    for j in range(file_.start, file_.end):
                        self._disk[j] = "."
                    break

    def get_checksum(self, chunky=False):
        checksum = 0

        if chunky:
            end = len(self._disk)
        else:
            end = self._disk.index(".")

        for i, value in enumerate(self._disk[:end]):
            if value != ".":
                checksum += i * int(value)

        return checksum


def part_one(data):
    disk = Disk(data)
    disk.defrag()

    return disk.get_checksum()


def part_two(data):
    disk = Disk(data)
    disk.defrag_chunky()

    return disk.get_checksum(chunky=True)


def main():
    args = parser.parse_args()
    data = files("files").joinpath(args.filename).read_text()

    if args.part == 1:
        print(part_one(data))
    if args.part == 2:
        print(part_two(data))


if __name__ == "__main__":
    main()
