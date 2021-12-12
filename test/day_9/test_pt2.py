import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_9.pt2 import main

TEST_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678
"""


class TestDay9Part2(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "1134\n")


if __name__ == '__main__':
    unittest.main()
