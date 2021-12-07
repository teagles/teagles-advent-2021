import sys

from .lib import parse_initial_state, decrement_one_day, reduce_state


def main():
    line = sys.stdin.readlines()[0]
    state = parse_initial_state(line)
    for i in range(80):
        state = decrement_one_day(state)
    print(reduce_state(state))


if __name__ == '__main__':
    main()
