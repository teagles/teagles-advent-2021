import unittest
from io import StringIO

from teagles_advent_2021.day_4.lib import BingoBoard, numerals_from_input

TEST_STRING = """
14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

TEST_NUMERALS = [[14, 21, 17, 24, 4],
                 [10, 16, 15, 9, 19],
                 [18, 8, 23, 26, 20],
                 [22, 11, 13, 6, 5],
                 [2, 0, 12, 3, 7]]

BOARD_INTERNALS = {0: ({0, 2, 3, 7, 12}, {0, 8, 11, 16, 21}),
                   2: ({0, 2, 3, 7, 12}, {2, 10, 14, 18, 22}),
                   3: ({0, 2, 3, 7, 12}, {3, 6, 9, 24, 26}),
                   4: ({4, 14, 17, 21, 24}, {4, 5, 7, 19, 20}),
                   5: ({5, 6, 11, 13, 22}, {4, 5, 7, 19, 20}),
                   6: ({5, 6, 11, 13, 22}, {3, 6, 9, 24, 26}),
                   7: ({0, 2, 3, 7, 12}, {4, 5, 7, 19, 20}),
                   8: ({8, 18, 20, 23, 26}, {0, 8, 11, 16, 21}),
                   9: ({9, 10, 15, 16, 19}, {3, 6, 9, 24, 26}),
                   10: ({9, 10, 15, 16, 19}, {2, 10, 14, 18, 22}),
                   11: ({5, 6, 11, 13, 22}, {0, 8, 11, 16, 21}),
                   12: ({0, 2, 3, 7, 12}, {12, 13, 15, 17, 23}),
                   13: ({5, 6, 11, 13, 22}, {12, 13, 15, 17, 23}),
                   14: ({4, 14, 17, 21, 24}, {2, 10, 14, 18, 22}),
                   15: ({9, 10, 15, 16, 19}, {12, 13, 15, 17, 23}),
                   16: ({9, 10, 15, 16, 19}, {0, 8, 11, 16, 21}),
                   17: ({4, 14, 17, 21, 24}, {12, 13, 15, 17, 23}),
                   18: ({8, 18, 20, 23, 26}, {2, 10, 14, 18, 22}),
                   19: ({9, 10, 15, 16, 19}, {4, 5, 7, 19, 20}),
                   20: ({8, 18, 20, 23, 26}, {4, 5, 7, 19, 20}),
                   21: ({4, 14, 17, 21, 24}, {0, 8, 11, 16, 21}),
                   22: ({5, 6, 11, 13, 22}, {2, 10, 14, 18, 22}),
                   23: ({8, 18, 20, 23, 26}, {12, 13, 15, 17, 23}),
                   24: ({4, 14, 17, 21, 24}, {3, 6, 9, 24, 26}),
                   26: ({8, 18, 20, 23, 26}, {3, 6, 9, 24, 26})}

WINNING_GAME = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]


class TestDay4Lib(unittest.TestCase):
    def test_parse_numerals_from_input(self):
        expectation = TEST_NUMERALS
        reality = [list(row) for row in numerals_from_input(StringIO(TEST_STRING))]
        self.assertEqual(expectation, reality)

    def test_construct_board(self):
        expectation = BOARD_INTERNALS
        reality = BingoBoard(TEST_NUMERALS).board_numbers
        self.assertEqual(expectation, reality)

    def test_play_board(self):
        expectation = 4512
        board = BingoBoard(TEST_NUMERALS)
        for number in WINNING_GAME:
            reality = board.play_numeral(number)
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
