import sys

from functools import reduce
from operator import mul

from .lib import parse_input, points_with_neighbors, low_point, get_basin


def main():
    matrix = parse_input(sys.stdin)
    low_points = filter(low_point, points_with_neighbors(matrix))
    basins = map(lambda p: get_basin(matrix, p.co_ords), low_points)
    print(reduce(mul, sorted(map(len, basins), reverse=True)[:3]))


if __name__ == '__main__':
    main()
