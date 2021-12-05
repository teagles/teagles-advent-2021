from collections import namedtuple
from re import compile

Line = namedtuple('Line', ['x1', 'y1', 'x2', 'y2'])
Point = namedtuple('Point', ['x', 'y'])
LINE_PATTERN = compile(r'(\d+),(\d+) -> (\d+),(\d+)')
HORIZONTAL = 'h'
VERTICAL = 'v'
POS_DIAGONAL = '+d'
NEG_DIAGONAL = '-d'


def orientation(line):
    if line.y1 == line.y2:
        return HORIZONTAL
    elif line.x1 == line.x2:
        return VERTICAL
    else:
        slope = (line.y2 - line.y1) / (line.x2 - line.x1)
        if slope > 0:
            return POS_DIAGONAL
        else:
            return NEG_DIAGONAL


def points_from_line(line):
    o = orientation(line)
    if o is POS_DIAGONAL:
        for s in range(abs(line.x1 - line.x2) + 1):
            yield Point(min(line.x1, line.x2) + s, min(line.y1, line.y2) + s)
    elif o is NEG_DIAGONAL:
        for s in range(abs(line.x1 - line.x2) + 1):
            yield Point(max(line.x1, line.x2) - s, min(line.y1, line.y2) + s)
    elif o is HORIZONTAL:
        for x in range(abs(line.x1 - line.x2) + 1):
            yield Point(min(line.x1, line.x2) + x, line.y1)
    else:
        for y in range(abs(line.y1 - line.y2) + 1):
            yield Point(line.x1, min(line.y1, line.y2) + y)


def parse_line(string):
    return Line(*map(int, LINE_PATTERN.match(string).groups()))
