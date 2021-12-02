import unittest
from io import StringIO

from teagles_advent_2021.day_1.sonar_sweep_lib import stream_to_ints, find_depth_increments


class TestSonarSweepLib(unittest.TestCase):
    def test_stream_to_ints(self):
        expectation = [1, 2, 3]
        reality = list(stream_to_ints(StringIO("""1
2
3
""")))
        self.assertEqual(expectation, reality)

    def test_find_depth_increments(self):
        expectation = 7
        reality = find_depth_increments([199,
                                         200,
                                         208,
                                         210,
                                         200,
                                         207,
                                         240,
                                         269,
                                         260,
                                         263])
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
