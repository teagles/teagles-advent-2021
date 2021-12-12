import sys

from .lib import parse_input, CumulativeState, step


def main():
    matrix = parse_input(sys.stdin)
    state = CumulativeState(matrix, 0, None)
    n = 0
    while state.last_flashes != 100:
        n += 1
        state = step(state)
    print(n)


if __name__ == '__main__':
    main()
