import unittest
from io import StringIO

from teagles_advent_2021.day_2.dive_lib import Instruction, instruction_tuples, sub_d, sub_u, sub_f


class TestDiveLib(unittest.TestCase):
    def test_instruction_tuples(self):
        expectation = [Instruction(sub_f, 5), Instruction(sub_d, 6), Instruction(sub_u, 3)]
        reality = list(instruction_tuples(StringIO("""forward 5
down 6
up 3
""")))
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
