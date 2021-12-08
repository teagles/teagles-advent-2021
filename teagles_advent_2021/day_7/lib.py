from statistics import median, mean
from functools import reduce
from operator import add
from math import ceil, floor


def ideal(nums):
    return round(median(nums))


def ideal_2(nums):
    return mean(nums)


def parse_input(line):
    return list(map(int, line.split(',')))


def fuel_consumed(nums):
    target = ideal(nums)
    return reduce(add, map(lambda n: abs(n-target), nums))


def ap_fuel(n):
    return round(n/2*(2 + (n - 1) * 1))


def fuel_consumed_2(nums):
    target = ideal_2(nums)
    return min(reduce(add, map(lambda n: ap_fuel(abs(n-ceil(target))), nums)),
               reduce(add, map(lambda n: ap_fuel(abs(n-floor(target))), nums)))
