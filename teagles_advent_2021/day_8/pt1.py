import sys

from .lib import parse_line, is_unique_digit


def main():
    outputs = []
    for line in sys.stdin:
        outputs.extend(parse_line(line).output)
    print(len(list(filter(is_unique_digit, outputs))))


if __name__ == '__main__':
    main()
