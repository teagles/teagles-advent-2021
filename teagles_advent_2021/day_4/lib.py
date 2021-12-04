from functools import reduce
from operator import add


class BingoBoard:
    def __init__(self, numeral_source, dimension=5):
        self.board_numbers = {}
        columns = [set() for i in range(dimension)]
        for row in numeral_source:
            numbers_from_this_row = set()
            n = 0
            for numeral in row:
                numbers_from_this_row.add(numeral)
                columns[n].add(numeral)
                self.board_numbers[numeral] = (numbers_from_this_row, columns[n])
                n += 1

    def play_numeral(self, numeral):
        popped = self.board_numbers.pop(numeral, None)
        if popped:
            for row_or_col in popped:
                row_or_col.remove(numeral)
                if len(row_or_col) == 0:
                    return reduce(add, self.board_numbers.keys()) * numeral
        return None


def numerals_from_input(stream, dimension=5):
    rows = []
    for line in stream:
        if len(line) > 1:
            rows.append(map(int, line.split()))
            if len(rows) == dimension:
                return rows
    return rows
