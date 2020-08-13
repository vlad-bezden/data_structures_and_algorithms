"""Generates prime numbers up to the specified number."""

from math import sqrt
from typing import Generator


def gen(max_val: int) -> Generator[int, None, None]:
    yield from (
        i
        for i in range(2, max_val)
        if all(i % x != 0 for x in range(2, int(sqrt(i) + 1)))
    )


if __name__ == "__main__":
    for x in gen(600):
        print(x, end=", ")
