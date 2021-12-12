from collections import namedtuple
from functools import reduce
from operator import add, and_

TargetAndNeighbors = namedtuple('TargetAndNeighbors', ['target', 'neighbors', 'co_ords'])
Point = namedtuple('Point', ['row', 'col'])
_ADJACENCIES = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)]


def parse_input(stream):
    matrix = []
    for line in stream:
        matrix.append(list(map(int, line.strip())))
    return matrix


def valid(point, matrix):
    return 0 <= point.row < len(matrix) and 0 <= point.col < len(matrix[point.row])


def neighbors(matrix, point):
    targets_neighbors = []
    for direction in _ADJACENCIES:
        p = Point(*map(add, direction, point))
        if valid(p, matrix):
            targets_neighbors.append(matrix[p.row][p.col])
    return TargetAndNeighbors(matrix[point.row][point.col], frozenset(targets_neighbors), point)


def low_point(target_and_neighbors):
    return reduce(and_, map(lambda n: target_and_neighbors.target < n, target_and_neighbors.neighbors))


def risk(target_and_neighbors):
    if low_point(target_and_neighbors):
        return target_and_neighbors.target + 1
    else:
        return 0


def points_with_neighbors(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            yield neighbors(matrix, Point(row, col))


def flood_fill_from_point(matrix, point, basin, seen):
    for direction in _ADJACENCIES:
        p = Point(*map(add, direction, point))
        if valid(p, matrix):
            if p not in seen:
                seen.add(p)
                if matrix[p.row][p.col] != 9:
                    basin.add(p)
                    flood_fill_from_point(matrix, p, basin, seen)


def get_basin(matrix, point):
    basin = set([point])
    seen = set([point])
    flood_fill_from_point(matrix, point, basin, seen)
    return basin
