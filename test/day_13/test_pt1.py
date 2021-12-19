import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_13.pt1 import main

TEST_INPUT = """6,10
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
"""


class TestDay13Part1(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "17\n")


if __name__ == '__main__':
    unittest.main()
