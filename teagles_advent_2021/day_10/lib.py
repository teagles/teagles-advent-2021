from collections import namedtuple
from functools import reduce

Bracket = namedtuple('Bracket', ['opener', 'closer', 'score', 'autocomplete_score'])

BRACKETS = frozenset([Bracket('(', ')', 3, 1),
                      Bracket('[', ']', 57, 2),
                      Bracket('{', '}', 1197, 3),
                      Bracket('<', '>', 25137, 4)])
OPENERS = {b.opener: b for b in BRACKETS}
CLOSERS = {b.closer: b for b in BRACKETS}


def validate(string):
    stack = []
    for c in string:
        if c in OPENERS.keys():
            stack.append(OPENERS[c])
        elif c in CLOSERS.keys():
            closer = CLOSERS[c]
            if closer is not stack.pop():
                return closer
    return reversed(stack)


def score_autocomplete(closer_stack):
    return reduce(lambda x, y: x*5+y, map(lambda b: b.autocomplete_score ,closer_stack), 0)
