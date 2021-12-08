import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_7.pt1 import main

TEST_INPUT = """16,1,2,0,4,2,7,1,2,14
"""


class TestDay7Part1(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "37\n")


if __name__ == '__main__':
    unittest.main()
