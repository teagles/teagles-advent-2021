from more_itertools import sliding_window
from functools import reduce
from operator import add


def stream_to_ints(stream):
    for line in stream:
        yield int(line)


def find_depth_increments(ints):
    last = None
    increments = 0
    for current_int in ints:
        if not last:
            pass
        elif current_int > last:
            increments += 1
        last = current_int
    return increments


def sliding_window_depth(ints):
    return map(lambda depth_tuple: reduce(add, depth_tuple), sliding_window(ints, 3))
