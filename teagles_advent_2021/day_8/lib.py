from collections import namedtuple
from functools import reduce
from operator import and_, getitem

Line = namedtuple('Line', ['unique_patterns', 'output'])
NUMBER_COMPOSITION = {0: frozenset('abcefg'), 1: frozenset('cf'), 2: frozenset('acdeg'), 3: frozenset('acdfg'),
                      4: frozenset('bcdf'), 5: frozenset('abdfg'), 6: frozenset('abdefg'), 7: frozenset('acf'),
                      8: frozenset('abcdefg'), 9: frozenset('abcdfg')}
NUMBERS_FROM_SEGMENTS = {v: k for k, v in NUMBER_COMPOSITION.items()}


def unique_segment_counts(number_mappings):
    segment_counts = {}
    for number, segments in number_mappings.items():
        segment_c = len(segments)
        current_segments = segment_counts.get(segment_c, list())
        current_segments.append(number)
        segment_counts[segment_c] = current_segments
    return {count: numbers[0] for (count, numbers) in segment_counts.items() if len(numbers) == 1}


UNIQUE_NUMBERS = unique_segment_counts(NUMBER_COMPOSITION)


def parse_line(line):
    unique_patterns, output = line.split('|')
    return Line(unique_patterns.split(), output.split())


def is_unique_digit(string):
    return len(string) in UNIQUE_NUMBERS.keys()


def set_as_char(s):
    return ''.join(s)


def determine_mapping(digit_strings):
    segment_counts = {}
    for string in digit_strings:
        segments = frozenset(string)
        segment_c = len(segments)
        current_segments = segment_counts.get(segment_c, list())
        current_segments.append(segments)
        segment_counts[segment_c] = current_segments
    six_segment_numbers = reduce(and_, segment_counts[6])
    five_segment_numbers = reduce(and_, segment_counts[5])
    seven = segment_counts[3][0]
    one = segment_counts[2][0]
    a = seven - one
    four = segment_counts[4][0]
    b_or_d = four - one
    c_or_f = one
    d_or_g = five_segment_numbers - a
    b_or_g = six_segment_numbers - a - c_or_f
    b = b_or_d & b_or_g
    d = b_or_d & d_or_g
    g = b_or_g & d_or_g
    f = six_segment_numbers - a - b - g
    c = c_or_f - f
    eight = segment_counts[7][0]
    e = eight - a - b - c - c - d - f - g
    return {set_as_char(a): 'a', set_as_char(b): 'b', set_as_char(c): 'c', set_as_char(d): 'd',
            set_as_char(e): 'e', set_as_char(f): 'f', set_as_char(g): 'g'}


def decode(mapping, output_digits):
    result = 0
    order = 0
    for digit in reversed(output_digits):
        numeric_form = NUMBERS_FROM_SEGMENTS[frozenset(''.join(map(lambda c: mapping[c], digit)))]
        result += numeric_form * 10 ** order
        order += 1
    return result
