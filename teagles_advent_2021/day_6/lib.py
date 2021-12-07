from functools import reduce
from operator import add


def parse_initial_state(line):
    result = {}
    for n in map(int, line.split(',')):
        result[n] = result.get(n, 0) + 1
    return result


def decrement_one_day(state):
    new_state = {}
    for counter in state.keys():
        if counter == 0:
            new_state[8] = new_state.get(8, 0) + state[0]
            new_state[6] = new_state.get(6, 0) + state[0]
        else:
            new_state[counter - 1] = new_state.get(counter - 1, 0) + state[counter]
    return new_state


def reduce_state(state):
    return reduce(add, state.values())
