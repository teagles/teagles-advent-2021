import unittest

from teagles_advent_2021.day_8.lib import noop


class TestDay8Lib(unittest.TestCase):
    def test_expectations(self):
        expectation = None
        reality = noop()
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
