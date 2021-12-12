import unittest

from teagles_advent_2021.day_10.lib import validate, Bracket, CLOSERS, score_autocomplete


class TestDay10Lib(unittest.TestCase):
    def test_expectations(self):
        expectation = [CLOSERS['}'], CLOSERS['}'], CLOSERS[']'], CLOSERS[']'], CLOSERS[')'], CLOSERS['}'],
                       CLOSERS[')'], CLOSERS[']']]
        reality = list(validate('[({(<(())[]>[[{[]{<()<>>'))
        self.assertEqual(expectation, reality)
        expectation = [CLOSERS[')'], CLOSERS['}'], CLOSERS['>'], CLOSERS[']'], CLOSERS['}'], CLOSERS[')']]
        reality = list(validate('[(()[<>])]({[<{<<[]>>('))
        self.assertEqual(expectation, reality)
        expectation = Bracket('{', '}', 1197, 3)
        reality = validate('{([(<{}[<>[]}>{[]{[(<()>')
        self.assertEqual(expectation, reality)

    def test_score_autocomplete(self):
        expectation = 288957
        reality = score_autocomplete([CLOSERS['}'], CLOSERS['}'], CLOSERS[']'], CLOSERS[']'], CLOSERS[')'], CLOSERS['}'],
                       CLOSERS[')'], CLOSERS[']']])
        self.assertEqual(expectation, reality)


if __name__ == '__main__':
    unittest.main()
