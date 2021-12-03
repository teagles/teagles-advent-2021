import sys

from .lib import binput_lines, cursive_filter, intify_binary_tuple


def main():
    values = list(binput_lines(sys.stdin))
    o2 = intify_binary_tuple(cursive_filter(values, True))
    co2 = intify_binary_tuple(cursive_filter(values, False))
    print(o2 * co2)


if __name__ == '__main__':
    main()
