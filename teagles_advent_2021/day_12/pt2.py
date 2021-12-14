import sys

from .lib import parse_input, CaveSystem, START_STR


def main():
    cs = CaveSystem()
    cs.populate(parse_input(sys.stdin))
    print(len(cs.traverse_2(START_STR, [], frozenset(), None)))


if __name__ == '__main__':
    main()
