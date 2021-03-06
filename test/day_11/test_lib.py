import unittest

from io import StringIO

from teagles_advent_2021.day_11.lib import parse_input, step, CumulativeState


class TestDay11Lib(unittest.TestCase):
    def test_expectations(self):
        expectation = [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
                       [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
                       [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
                       [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
                       [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
                       [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
                       [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
                       [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
                       [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
                       [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]
        reality = parse_input(StringIO("""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""))
        self.assertEqual(expectation, reality)

    def test_step(self):
        expectation = CumulativeState([[3, 4, 5, 4, 3],
                                       [4, 0, 0, 0, 4],
                                       [5, 0, 0, 0, 5],
                                       [4, 0, 0, 0, 4],
                                       [3, 4, 5, 4, 3]], 9, 9)
        reality = step(CumulativeState([[1, 1, 1, 1, 1],
                                        [1, 9, 9, 9, 1],
                                        [1, 9, 1, 9, 1],
                                        [1, 9, 9, 9, 1],
                                        [1, 1, 1, 1, 1]], 0, None))
        self.assertEqual(expectation, reality)
        expectation = CumulativeState([[4, 5, 6, 5, 4],
                                       [5, 1, 1, 1, 5],
                                       [6, 1, 1, 1, 6],
                                       [5, 1, 1, 1, 5],
                                       [4, 5, 6, 5, 4]], 9, 0)
        reality = step(reality)
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
