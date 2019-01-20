"""
List allocation with teh same value using different techniques

Output:
first: 0.717055
second: 1.021743
third: 0.046112
forth: 0.005384
"""

from timeit import timeit
from itertools import repeat

import numpy


SIZE = 10000
INIT_VALUE = 0


def first():
    """Using itertools.repeat"""
    return [x for x in repeat(INIT_VALUE, SIZE)]


def second():
    """Using range"""
    return [INIT_VALUE for x in range(SIZE)]


def third():
    return [INIT_VALUE] * SIZE


def forth():
    """Using numpy"""
    return numpy.zeros(SIZE, numpy.int)


for x in [first, second, third, forth]:
    t = timeit(stmt=x, number=1000)
    print(f"{x.__name__}: {t:.6f}")
