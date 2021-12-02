import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_2.dive_pt2 import main

TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


class TestDivePart2(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "horizontal position of 15 and a depth of 60 (900)\n")


if __name__ == '__main__':
    unittest.main()
