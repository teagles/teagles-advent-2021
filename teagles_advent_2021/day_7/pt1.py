import sys

from .lib import parse_input, fuel_consumed


def main():
    line = sys.stdin.readlines()[0]
    print(fuel_consumed(parse_input(line)))


if __name__ == '__main__':
    main()
