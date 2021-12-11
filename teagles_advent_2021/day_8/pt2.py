import sys

from functools import reduce
from operator import add

from .lib import parse_line, decode, determine_mapping


def main():
    print(reduce(add, map(lambda line: decode(determine_mapping(line.unique_patterns), line.output),
                          map(parse_line, sys.stdin))))


if __name__ == '__main__':
    main()
