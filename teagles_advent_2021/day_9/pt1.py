import sys

from functools import reduce
from operator import add

from .lib import parse_input, points_with_neighbors, risk


def main():
    matrix = parse_input(sys.stdin)
    print(reduce(add, map(risk, points_with_neighbors(matrix))))


if __name__ == '__main__':
    main()
