"""Generates prime numbers up to the specified number.

    Output:

    classical_prime_gen(1000). Exec time = 0.002481 sec
    sieve_prime_gen(1000). Exec time = 0.002761 sec

    classical_prime_gen(100000). Exec time = 0.002602 sec
    sieve_prime_gen(100000). Exec time = 0.002768 sec
"""

from math import sqrt
from typing import Callable, Generator, Sequence
from timeit import repeat
from dataclasses import dataclass


@dataclass
class Test:
    data: int
    expected: int


TESTS = [Test(1_000, 168), Test(100_000, 9592)]


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


def validate(funcs: Sequence[Callable[[int], Generator[int, None, None]]]) -> None:
    for test in TESTS:
        for f in funcs:
            result = list(f(test.data))
            assert len(result) == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!\n")


if __name__ == "__main__":
    funcs = [classical_prime_gen, sieve_prime_gen]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = repeat(
                stmt=f"f({test.data})", repeat=10, number=10_000, globals=globals()
            )
            print(f"{f.__name__}({test.data}). Exec time = {min(t):.6f} sec")
        print()
