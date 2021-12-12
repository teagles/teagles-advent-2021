import sys

from .lib import parse_input, CumulativeState, step


def main():
    matrix = parse_input(sys.stdin)
    state = CumulativeState(matrix, 0)
    for i in range(100):
        state = step(state)
    print(state.flashes)


if __name__ == '__main__':
    main()
