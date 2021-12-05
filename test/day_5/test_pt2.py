import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_5.pt2 import main

TEST_INPUT = """
"""


class TestDay5Part2(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "\n")


if __name__ == '__main__':
    unittest.main()
