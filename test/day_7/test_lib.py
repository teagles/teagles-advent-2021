import unittest

from teagles_advent_2021.day_7.lib import parse_input, ideal, fuel_consumed


class TestDay7Lib(unittest.TestCase):
    def test_parse_input(self):
        expectation = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        reality = parse_input('16,1,2,0,4,2,7,1,2,14')
        self.assertEqual(expectation, reality)

    def test_ideal(self):
        expectation = 2
        reality = ideal([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(expectation, reality)

    def test_fuel_consumed(self):
        expectation = 37
        reality = fuel_consumed([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
