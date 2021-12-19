import unittest

from io import StringIO

from teagles_advent_2021.day_13.lib import parse_input, PageAndFolds, Fold, fold, new_dimension, Point


class TestDay13Lib(unittest.TestCase):
    def test_parse_input(self):
        expectation = PageAndFolds([[False, False, False, True, False, False, True, False, False, True, False],
                                    [False, False, False, False, True, False, False, False, False, False, False],
                                    [False, False, False, False, False, False, False, False, False, False, False],
                                    [True, False, False, False, False, False, False, False, False, False, False],
                                    [False, False, False, True, False, False, False, False, True, False, True],
                                    [False, False, False, False, False, False, False, False, False, False, False],
                                    [False, False, False, False, False, False, False, False, False, False, False],
                                    [False, False, False, False, False, False, False, False, False, False, False],
                                    [False, False, False, False, False, False, False, False, False, False, False],
                                    [False, False, False, False, False, False, False, False, False, False, False],
                                    [False, True, False, False, False, False, True, False, True, True, False],
                                    [False, False, False, False, True, False, False, False, False, False, False],
                                    [False, False, False, False, False, False, True, False, False, False, True],
                                    [True, False, False, False, False, False, False, False, False, False, False],
                                    [True, False, True, False, False, False, False, False, False, False, False]],
                                   [Fold('y', 7), Fold('x', 5)])
        reality = parse_input(StringIO("""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""))
        self.assertEqual(expectation, reality)

    def test_fold(self):
        test_page_1 = [[False, False, False, True, False, False, True, False, False, True, False],
                       [False, False, False, False, True, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [True, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, True, False, False, False, False, True, False, True],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, True, False, False, False, False, True, False, True, True, False],
                       [False, False, False, False, True, False, False, False, False, False, False],
                       [False, False, False, False, False, False, True, False, False, False, True],
                       [True, False, False, False, False, False, False, False, False, False, False],
                       [True, False, True, False, False, False, False, False, False, False, False]]
        expectation = Point(11, 7)
        reality = new_dimension(test_page_1, Fold('y', 7))
        self.assertEqual(expectation, reality)
        test_page_2 = [[True, False, True, True, False, False, True, False, False, True, False],
                       [True, False, False, False, True, False, False, False, False, False, False],
                       [False, False, False, False, False, False, True, False, False, False, True],
                       [True, False, False, False, True, False, False, False, False, False, False],
                       [False, True, False, True, False, False, True, False, True, True, True],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False]]
        expectation = Point(5, 7)
        reality = new_dimension(test_page_2, Fold('x', 5))
        self.assertEqual(expectation, reality)

    def test_new_dimension(self):
        test_page_1 = [[False, False, False, True, False, False, True, False, False, True, False],
                       [False, False, False, False, True, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [True, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, True, False, False, False, False, True, False, True],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, False, False, False, False, False, False, False, False, False, False],
                       [False, True, False, False, False, False, True, False, True, True, False],
                       [False, False, False, False, True, False, False, False, False, False, False],
                       [False, False, False, False, False, False, True, False, False, False, True],
                       [True, False, False, False, False, False, False, False, False, False, False],
                       [True, False, True, False, False, False, False, False, False, False, False]]
        expectation_1 = [[True, False, True, True, False, False, True, False, False, True, False],
                         [True, False, False, False, True, False, False, False, False, False, False],
                         [False, False, False, False, False, False, True, False, False, False, True],
                         [True, False, False, False, True, False, False, False, False, False, False],
                         [False, True, False, True, False, False, True, False, True, True, True],
                         [False, False, False, False, False, False, False, False, False, False, False],
                         [False, False, False, False, False, False, False, False, False, False, False]]
        reality = fold(test_page_1, Fold('y', 7))
        self.assertEqual(expectation_1, reality)
        expectation_2 = [[True, True, True, True, True],
                         [True, False, False, False, True],
                         [True, False, False, False, True],
                         [True, False, False, False, True],
                         [True, True, True, True, True],
                         [False, False, False, False, False],
                         [False, False, False, False, False]]
        reality = fold(reality, Fold('x', 5))
        self.assertEqual(expectation_2, reality)


if __name__ == '__main__':
    unittest.main()
