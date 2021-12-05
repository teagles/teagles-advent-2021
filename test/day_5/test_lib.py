import unittest

from teagles_advent_2021.day_5.lib import Line, Point, orientation, points_from_line, parse_line, HORIZONTAL, VERTICAL, POS_DIAGONAL, NEG_DIAGONAL


class TestDay5Lib(unittest.TestCase):
    def test_orientation(self):
        expectation = HORIZONTAL
        reality = orientation(Line(9, 7, 7, 7))
        self.assertEqual(expectation, reality)
        expectation = VERTICAL
        reality = orientation(Line(1, 1, 1, 3))
        self.assertEqual(expectation, reality)
        expectation = POS_DIAGONAL
        reality = orientation(Line(1, 1, 3, 3))
        self.assertEqual(expectation, reality)

    def test_points_from_line(self):
        expectation = {Point(9, 7), Point(8, 7), Point(7, 7)}
        reality = set(points_from_line(Line(9, 7, 7, 7)))
        self.assertEqual(expectation, reality)
        expectation = {Point(1, 1), Point(1, 2), Point(1, 3)}
        reality = set(points_from_line(Line(1, 1, 1, 3)))
        self.assertEqual(expectation, reality)
        expectation = {Point(1, 1), Point(2, 2), Point(3, 3)}
        reality = set(points_from_line(Line(1, 1, 3, 3)))
        self.assertEqual(expectation, reality)
        expectation = {Point(9, 7), Point(8, 8), Point(7, 9)}
        reality = set(points_from_line(Line(9, 7, 7, 9)))
        self.assertEqual(expectation, reality)

    def test_parse_line(self):
        expectation = Line(0, 9, 5, 9)
        reality = parse_line('0,9 -> 5,9')
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
