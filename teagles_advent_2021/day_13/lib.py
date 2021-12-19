from collections import namedtuple
from re import compile
from functools import reduce

from teagles_advent_2021.day_5.lib import Point
POINT_PATTERN = compile(r'(\d+),(\d+)')
PageAndFolds = namedtuple('PageAndFolds', ['page', 'folds'])
Fold = namedtuple('Fold', ['orientation', 'index'])
FOLD_PATTERN = compile(r'fold along ([xy])=(\d+)')


def parse_input(stream):
    points = set()
    folds = []
    bounding_point = Point(0, 0)
    for line in stream:
        if (match := FOLD_PATTERN.match(line)) is not None:
            folds.append((Fold(match.group(1), int(match.group(2)))))
        elif(match := POINT_PATTERN.match(line)) is not None:
            point = Point(*map(int, match.groups()))
            points.add(point)
            bounding_point = Point(*map(max, bounding_point, point))
    page = [[Point(x, y) in points for x in range(bounding_point.x + 1)] for y in range(bounding_point.y + 1)]
    return PageAndFolds(page, folds)


def new_dimension(page, fold_t):
    if fold_t.orientation == 'x':
        return Point(reduce(max, map(len, page)) - fold_t.index - 1, len(page))
    else:
        return Point(reduce(max, map(len, page)), len(page) - fold_t.index - 1)


def valid(p, page):
    if 0 <= p.y < len(page) and 0 <= p.x < len(page[p.y]):
        return page[p.y][p.x]
    return None


def get_folded_point(page, fold_t, p):
    if fold_t.orientation == 'x':
        index = p.x - fold_t.index
        return valid(Point(fold_t.index - index, p.y), page) or valid(Point(fold_t.index + index, p.y), page)
    else:
        index = p.y - fold_t.index
        return valid(Point(p.x, fold_t.index - index), page) or valid(Point(p.x, fold_t.index + index), page)


def fold(page, fold_t):
    new_page_dimension = new_dimension(page, fold_t)
    return [[get_folded_point(page, fold_t, Point(x, y)) for x in range(new_page_dimension.x)] for y in
            range(new_page_dimension.y)]
