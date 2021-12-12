import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_11.pt2 import main

TEST_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


class TestDay11Part2(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "195\n")


if __name__ == '__main__':
    unittest.main()
