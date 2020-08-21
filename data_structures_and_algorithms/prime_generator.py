"""Generates prime numbers up to the specified number."""

from math import sqrt
from typing import Generator


def sieve_prime_gen(num: int) -> Generator[int, None, None]:
    """Based on Sieve algorithm."""
    candidates = [*range(2, num + 1)]

    while candidates and (candidate := candidates[0]):
        yield candidate
        candidates = [n for n in candidates if n % candidate != 0]


def classical_prime_gen(num: int) -> Generator[int, None, None]:
    """Classical prime generator."""
    if 2 <= num:
        yield 2
    yield from (
        i
        for i in range(3, num + 1, 2)
        if all(i % x != 0 for x in range(3, int(sqrt(i) + 1)))
    )


for func in [classical_prime_gen, sieve_prime_gen]:
    print(f"\n{func.__name__}")
    for x in func(1000):
        print(x, end=", ")
