import unittest

from teagles_advent_2021.day_6.lib import parse_initial_state, decrement_one_day, reduce_state


class TestDay6Lib(unittest.TestCase):
    def test_parse_initial_state(self):
        expectation = {4: 1, 3: 2, 2: 1, 1: 1}
        reality = parse_initial_state('3,4,3,1,2')
        self.assertEqual(expectation, reality)

    def test_decrement_one_day(self):
        expectation = {6: 1, 8: 1}
        reality = decrement_one_day({0: 1})
        self.assertEqual(expectation, reality)
        expectation = {2: 2, 3: 1, 1: 1, 0: 1}
        reality = decrement_one_day(parse_initial_state('3,4,3,1,2'))
        self.assertEqual(expectation, reality)

    def test_reduce_state(self):
        expectation = 2
        reality = reduce_state({6: 1, 8: 1})
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
