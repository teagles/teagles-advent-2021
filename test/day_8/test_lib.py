import unittest

from teagles_advent_2021.day_8.lib import parse_line, Line, is_unique_digit, unique_segment_counts, NUMBERS


class TestDay8Lib(unittest.TestCase):
    def test_unique_segment_counts(self):
        expectation = {2: 1, 3: 7, 4: 4, 7: 8}
        reality = unique_segment_counts(NUMBERS)

    def test_parse_line(self):
        expectation = Line(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'],
                           ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'])
        reality = parse_line('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf')
        self.assertEqual(expectation, reality)

    def test_is_unique_digit(self):
        expectation = True
        reality = is_unique_digit('abc')
        self.assertEqual(expectation, reality)
        expectation = True
        reality = is_unique_digit('fg')
        self.assertEqual(expectation, reality)
        expectation = True
        reality = is_unique_digit('gbdfcae')
        self.assertEqual(expectation, reality)
        expectation = True
        reality = is_unique_digit('cefg')
        self.assertEqual(expectation, reality)
        expectation = False
        reality = is_unique_digit('bagce')
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
