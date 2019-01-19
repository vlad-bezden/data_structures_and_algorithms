"""
List allocation with teh same value using different techniques
"""

from timeit import timeit
from itertools import repeat


SIZE = 10_000
INIT_VALUE = 0


def first():
    """Using itertools.repeat"""
    return [x for x in repeat(INIT_VALUE, SIZE)]


def second():
    """Using range"""
    return [INIT_VALUE for x in range(SIZE)]


def third():
    return [INIT_VALUE] * SIZE


for x in [first, second, third]:
    t = timeit(stmt=x, number=1_000)
    print(f"{x.__name__}: {t}")
