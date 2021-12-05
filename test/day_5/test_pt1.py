import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_5.pt1 import main

TEST_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


class TestDay5Part1(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "5\n")


if __name__ == '__main__':
    unittest.main()
