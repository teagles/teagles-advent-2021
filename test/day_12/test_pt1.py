import unittest

from test.std_test_utils import STDIOTest
from teagles_advent_2021.day_12.pt1 import main

TEST_INPUT = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


class TestDay12Part1(STDIOTest):
    def test_with_sample_input(self):
        self.assert_stdin_n_out(main, TEST_INPUT, "226\n")


if __name__ == '__main__':
    unittest.main()
