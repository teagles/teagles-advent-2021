import unittest

from io import StringIO

from teagles_advent_2021.day_9.lib import parse_input, valid, Point, neighbors, TargetAndNeighbors, low_point, risk,\
    points_with_neighbors


class TestDay9Lib(unittest.TestCase):
    def test_expectations(self):
        expectation = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                       [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                       [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                       [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                       [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
        reality = parse_input(StringIO("""2199943210
3987894921
9856789892
8767896789
9899965678
"""))
        self.assertEqual(expectation, reality)

    def test_valid(self):
        test_matrix = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                       [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                       [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                       [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                       [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
        self.assertEqual(True, valid(Point(0, 0), test_matrix))
        self.assertEqual(True, valid(Point(4, 9), test_matrix))
        self.assertEqual(False, valid(Point(-1, 0), test_matrix))
        self.assertEqual(False, valid(Point(0, -1), test_matrix))
        self.assertEqual(False, valid(Point(-1, -1), test_matrix))
        self.assertEqual(False, valid(Point(5, 9), test_matrix))
        self.assertEqual(False, valid(Point(4, 10), test_matrix))
        self.assertEqual(False, valid(Point(5, 10), test_matrix))

    def test_neighbors(self):
        test_matrix = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                       [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                       [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                       [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                       [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
        expectation = TargetAndNeighbors(2, frozenset([1, 3]))
        reality = neighbors(test_matrix, Point(0, 0))
        self.assertEqual(expectation, reality)
        expectation = TargetAndNeighbors(8, frozenset([7, 9]))
        reality = neighbors(test_matrix, Point(4, 9))
        self.assertEqual(expectation, reality)
        expectation = TargetAndNeighbors(3, frozenset([2, 9]))
        reality = neighbors(test_matrix, Point(1, 0))
        self.assertEqual(expectation, reality)
        expectation = TargetAndNeighbors(9, frozenset([6, 8, 9]))
        reality = neighbors(test_matrix, Point(4, 2))
        self.assertEqual(expectation, reality)

    def test_low_point(self):
        self.assertEqual(True, low_point(TargetAndNeighbors(0, frozenset([1, 9]))))
        self.assertEqual(False, low_point(TargetAndNeighbors(9, frozenset([1, 8, 9]))))

    def test_risk(self):
        self.assertEqual(1, risk(TargetAndNeighbors(0, frozenset([1, 9]))))
        self.assertEqual(0, risk(TargetAndNeighbors(9, frozenset([1, 8, 9]))))

    def test_points_with_neighbors(self):
        test_matrix = [[0, 1],
                       [1, 0]]
        expectation = [TargetAndNeighbors(target=0, neighbors=frozenset({1})),
                       TargetAndNeighbors(target=1, neighbors=frozenset({0})),
                       TargetAndNeighbors(target=1, neighbors=frozenset({0})),
                       TargetAndNeighbors(target=0, neighbors=frozenset({1}))]
        reality = list(points_with_neighbors(test_matrix))
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
