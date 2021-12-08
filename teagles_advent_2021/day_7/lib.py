from statistics import median
from functools import reduce
from operator import add


def ideal(nums):
    return median(nums)


def parse_input(line):
    return list(map(int, line.split(',')))


def fuel_consumed(nums):
    target = round(ideal(nums))
    return reduce(add, map(lambda n: abs(n-target), nums))
