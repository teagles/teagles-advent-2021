import unittest

from io import StringIO

from teagles_advent_2021.day_12.lib import parse_input, Connection, CaveSystem


class TestDay12Lib(unittest.TestCase):
    def test_expectations(self):
        expectation = [Connection('start', 'A'),
                       Connection('start', 'b'),
                       Connection('A', 'c'),
                       Connection('A', 'b'),
                       Connection('b', 'd'),
                       Connection('A', 'end'),
                       Connection('b', 'end')]
        reality = list(parse_input(StringIO("""start-A
start-b
A-c
A-b
b-d
A-end
b-end
""")))
        self.assertEqual(expectation, reality)

    def test_traverse(self):
        cs = CaveSystem()
        cs.populate([Connection('start', 'A'),
                     Connection('start', 'b'),
                     Connection('A', 'c'),
                     Connection('A', 'b'),
                     Connection('b', 'd'),
                     Connection('A', 'end'),
                     Connection('b', 'end')])
        expectation = set([
            ('start', 'A', 'b', 'A', 'c', 'A', 'end'),
            ('start', 'A', 'b', 'A', 'end'),
            ('start', 'A', 'b', 'end'),
            ('start', 'A', 'c', 'A', 'b', 'A', 'end'),
            ('start', 'A', 'c', 'A', 'b', 'end'),
            ('start', 'A', 'c', 'A', 'end'),
            ('start', 'A', 'end'),
            ('start', 'b', 'A', 'c', 'A', 'end'),
            ('start', 'b', 'A', 'end'),
            ('start', 'b', 'end')
        ])
        reality = set(cs.traverse('start', [], frozenset()))
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
