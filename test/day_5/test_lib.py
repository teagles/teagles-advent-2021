import unittest

from teagles_advent_2021.day_5.lib import Line, Point, horizontal, points_from_line, parse_line


class TestDay5Lib(unittest.TestCase):
    def test_horizontal(self):
        expectation = True
        reality = horizontal(Line(9, 7, 7, 7))
        self.assertEqual(expectation, reality)
        expectation = False
        reality = horizontal(Line(1, 1, 1, 3))
        self.assertEqual(expectation, reality)

    def test_points_from_line(self):
        expectation = set([Point(9, 7), Point(8, 7), Point(7, 7)])
        reality = set(points_from_line(Line(9, 7, 7, 7)))
        self.assertEqual(expectation, reality)
        expectation = set([Point(1, 1), Point(1, 2), Point(1, 3)])
        reality = set(points_from_line(Line(1, 1, 1, 3)))
        self.assertEqual(expectation, reality)

    def test_parse_line(self):
        expectation = Line(0, 9, 5, 9)
        reality = parse_line('0,9 -> 5,9')
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
