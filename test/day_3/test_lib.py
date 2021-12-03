import unittest

from teagles_advent_2021.day_3.lib import binput_line, common_bits, intify_binary_tuple


class TestDay3Lib(unittest.TestCase):
    def test_binput_line(self):
        expectation = (False, True, False, True)
        reality = binput_line("0101")
        self.assertEqual(expectation, reality)

    def test_common_bits(self):
        expectation = (True, False, True, True, False)
        reality = common_bits([(False, False, True, False, False),
                                (True, True, True, True, False),
                                (True, False, True, True, False)])
        self.assertEqual(expectation, reality)

    def test_intify_binary_tuple(self):
        expectation = 9
        reality = intify_binary_tuple((False, True, False, False, True))
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
