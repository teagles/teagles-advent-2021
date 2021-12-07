import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_6.pt1 import main

TEST_INPUT = """3,4,3,1,2
"""


class TestDay6Part1(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "5934\n")


if __name__ == '__main__':
    unittest.main()
