from functools import reduce
from operator import add
from numpy import array, arange


def binput_lines(stream):
    for line in stream:
        yield binput_line(line.strip())


def binput_line(string):
    return tuple(map(lambda c: c == '1', string))


def digify(binary_tuple):
    return tuple(map(lambda b: 1 if b else -1, binary_tuple))


def undigify(numeric_tuple):
    return tuple(map(lambda d: d > 0, numeric_tuple))


def tuplewise_add(a, b):
    return tuple(map(add, a, b))


def common_bits(binary_tuples):
    return undigify(reduce(tuplewise_add, map(digify, binary_tuples)))


def tuplewise_not(b_tuple):
    return tuple(map(lambda b: not b, b_tuple))


def intify_binary_tuple(b_tuple):
    b = array(b_tuple, dtype=bool)
    return b.dot(2**arange(b.size)[::-1])
