import sys
from functools import reduce

from .dive_lib import instruction_tuples2, SubPosition2, move_sub


def main():
    position = reduce(move_sub, instruction_tuples2(sys.stdin), SubPosition2(0, 0, 0))
    print(
        f'horizontal position of {position.horizontal} and a depth of {position.depth} ({position.horizontal * position.depth})')


if __name__ == '__main__':
    main()
