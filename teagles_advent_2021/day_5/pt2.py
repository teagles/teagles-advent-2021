import sys

from .lib import parse_line, points_from_line, orientation


def main():
    points = set()
    repeat_points = set()
    for string in sys.stdin:
        line = parse_line(string)
        for point in points_from_line(line):
            if point in points:
                repeat_points.add(point)
            else:
                points.add(point)
    print(len(repeat_points))


if __name__ == '__main__':
    main()
