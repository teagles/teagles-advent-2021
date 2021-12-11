import unittest

from teagles_advent_2021.day_8.lib import parse_line, Line, is_unique_digit, unique_segment_counts, NUMBER_COMPOSITION,\
    determine_mapping, decode


class TestDay8Lib(unittest.TestCase):
    def test_unique_segment_counts(self):
        expectation = {2: 1, 3: 7, 4: 4, 7: 8}
        reality = unique_segment_counts(NUMBER_COMPOSITION)
        self.assertEqual(expectation, reality)

    def test_parse_line(self):
        expectation = Line(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'],
                           ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'])
        reality = parse_line('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf')
        self.assertEqual(expectation, reality)

    def test_determine_mapping(self):
        expectation = {'d': 'a', 'e': 'b', 'a': 'c', 'f': 'd', 'g': 'e', 'b': 'f', 'c': 'g'}
        reality = determine_mapping(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb',
                                     'ab'])
        self.assertEqual(expectation, reality)

    def test_decode(self):
        expectation = 5353
        reality = decode({'d': 'a', 'e': 'b', 'a': 'c', 'f': 'd', 'g': 'e', 'b': 'f', 'c': 'g'},
                         ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'])
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
