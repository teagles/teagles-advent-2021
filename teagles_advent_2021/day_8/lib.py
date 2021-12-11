from collections import namedtuple

Line = namedtuple('Line', ['unique_patterns', 'output'])
NUMBERS = {0: set('abcefg'), 1: set('cf'), 2: set('acdeg'), 3: set('acdfg'), 4: set('bcdf'),
           5: set('abdfg'), 6: set('abdefg'), 7: set('acf'), 8: set('abcdefg'), 9: set('abcdfg')}
UNIQUE_NUMBERS = {1: 2, 4: 4, 7: 3, 8: 7}


def unique_segment_counts(number_mappings):
    segment_counts = {}
    for number, segments in number_mappings.items():
        segment_c = len(segments)
        current_segments = segment_counts.get(segment_c, list())
        current_segments.append(number)
        segment_counts[segment_c] = current_segments
    return {count: numbers[0] for (count, numbers) in segment_counts.items() if len(numbers) == 1}


def parse_line(line):
    unique_patterns, output = line.split('|')
    return Line(unique_patterns.split(), output.split())


def is_unique_digit(string):
    return len(string) in UNIQUE_NUMBERS.values()
