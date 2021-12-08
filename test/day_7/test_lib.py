import unittest

from teagles_advent_2021.day_7.lib import parse_input, ideal, fuel_consumed, ideal_2, ap_fuel, fuel_consumed_2


class TestDay7Lib(unittest.TestCase):
    def test_parse_input(self):
        expectation = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        reality = parse_input('16,1,2,0,4,2,7,1,2,14')
        self.assertEqual(expectation, reality)

    def test_ideal(self):
        expectation = 2
        reality = ideal([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(expectation, reality)

    def test_ideal_2(self):
        expectation = 4.9
        reality = ideal_2([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(expectation, reality)

    def test_fuel_consumed(self):
        expectation = 37
        reality = fuel_consumed([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(expectation, reality)

    def test_ap_fuel(self):
        expectation = 10
        reality = ap_fuel(4)
        self.assertEqual(expectation, reality)
        expectation = 45
        reality = ap_fuel(9)
        self.assertEqual(expectation, reality)

    def test_fuel_consumed_2(self):
        expectation = 168
        reality = fuel_consumed_2([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
