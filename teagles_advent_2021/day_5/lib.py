from collections import namedtuple
from re import compile

Line = namedtuple('Line', ['x1', 'y1', 'x2', 'y2'])
Point = namedtuple('Point', ['x', 'y'])
LINE_PATTERN = compile(r'(\d+),(\d+) -> (\d+),(\d+)')


def horizontal(line):
    if line.y1 == line.y2:
        return True
    elif line.x1 == line.x2:
        return False
    else:
        return None


def points_from_line(line):
    orientation = horizontal(line)
    if orientation is None:
        pass
    elif orientation:
        for x in range(abs(line.x1 - line.x2) + 1):
            yield Point(min(line.x1, line.x2) + x, line.y1)
    else:
        for y in range(abs(line.y1 - line.y2) + 1):
            yield Point(line.x1, min(line.y1, line.y2) + y)


def parse_line(string):
    return Line(*map(int, LINE_PATTERN.match(string).groups()))
