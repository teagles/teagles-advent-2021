import sys

from .lib import binput_lines, common_bits, tuplewise_not, intify_binary_tuple


def main():
    gamma = common_bits(binput_lines(sys.stdin))
    epsilon = tuplewise_not(gamma)
    print(intify_binary_tuple(gamma) * intify_binary_tuple(epsilon))


if __name__ == '__main__':
    main()
