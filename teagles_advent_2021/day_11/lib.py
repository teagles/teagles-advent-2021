from collections import namedtuple
from operator import add

from teagles_advent_2021.day_9.lib import parse_input, Point, valid

CumulativeState = namedtuple('CumulativeState', ['matrix', 'flashes'])
_ADJACENCIES = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1), Point(1, 1), Point(-1, -1), Point(1, -1),
                Point(-1, 1)]


def _flash(matrix, point, flashed):
    flashed.add(point)
    for direction in _ADJACENCIES:
        p = Point(*map(add, direction, point))
        if valid(p, matrix) and p not in flashed:
            matrix[p.row][p.col] += 1
            if matrix[p.row][p.col] > 9:
                _flash(matrix, p, flashed)


def step(cumulative_state):
    flashes = cumulative_state.flashes
    # increment
    for row in range(len(cumulative_state.matrix)):
        for col in range(len(cumulative_state.matrix[row])):
            cumulative_state.matrix[row][col] += 1
    # flash_fill
    flashed = set()
    for row in range(len(cumulative_state.matrix)):
        for col in range(len(cumulative_state.matrix[row])):
            p = Point(row, col)
            if cumulative_state.matrix[row][col] > 9 and p not in flashed:
                _flash(cumulative_state.matrix, p, flashed)
    # reconcile
    for row in range(len(cumulative_state.matrix)):
        for col in range(len(cumulative_state.matrix[row])):
            if cumulative_state.matrix[row][col] > 9:
                cumulative_state.matrix[row][col] = 0
                flashes += 1
    return CumulativeState(cumulative_state.matrix, flashes)
