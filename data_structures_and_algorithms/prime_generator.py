"""Generates prime numbers up to the specified number."""

from math import sqrt
from typing import Generator


def classical_prime_gen(num: int) -> Generator[int, None, None]:
    """Classical prime generator."""
    if 2 <= num:
        yield 2
    yield from (
        i
        for i in range(3, num + 1, 2)
        if all(i % x != 0 for x in range(3, int(sqrt(i) + 1)))
    )


for x in classical_prime_gen(1000):
    print(x, end=", ")
