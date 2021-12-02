import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_1.sonar_sweep_pt2 import main

TEST_INPUT = """199
200
208
210
200
207
240
269
260
263
"""


class TestSonarSweepPart1(STDIOTest):

    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "5\n")


if __name__ == '__main__':
    unittest.main()
