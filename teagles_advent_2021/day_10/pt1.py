import sys

from functools import reduce
from operator import add

from .lib import validate, Bracket


def main():
    print(reduce(add, map(lambda b: b.score if type(b) == Bracket else 0, map(validate, sys.stdin))))


if __name__ == '__main__':
    main()
