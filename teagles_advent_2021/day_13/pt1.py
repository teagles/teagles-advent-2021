import sys

from functools import reduce
from operator import add
from itertools import chain

from .lib import parse_input, fold


def main():
    page, folds = parse_input(sys.stdin)
    after_first = fold(page, folds[0])
    print(reduce(add, map(lambda x: 1 if x else 0, chain(*after_first))))


if __name__ == '__main__':
    main()
