import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_3.pt1 import main

TEST_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


class TestDay3Part1(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "198\n")


if __name__ == '__main__':
    unittest.main()
