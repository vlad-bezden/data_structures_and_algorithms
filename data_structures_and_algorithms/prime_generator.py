"""Generates prime numbers up to the specified number.

    Output:

    classical_prime_gen(1000). Exec time = 0.000208 sec
    sieve_prime_gen(1000). Exec time = 0.000162 sec

    classical_prime_gen(100000). Exec time = 0.000112 sec
    sieve_prime_gen(100000). Exec time = 0.000115 sec
"""

from math import sqrt
from typing import Callable, Generator, Sequence
from timeit import repeat
from dataclasses import dataclass


@dataclass
class Test:
    data: int
    expected: int


TESTS = [Test(1_000, 168), Test(1_000_000, 78498)]


def sieve_prime_gen(num: int) -> Generator[int, None, None]:
    """Based on Sieve algorithm."""
    candidates = [False, False] + [True] * (num - 1)
    for p in range(2, int(sqrt(num) + 1)):
        # if we haven't already eliminated p as a prime
        if candidates[p]:
            # eliminate all multiples of p, starting at p ** 2
            for m in range(p * p, num + 1, p):
                candidates[m] = False
    # return the indices that weren't eliminated
    yield from (n for n, prime in enumerate(candidates) if prime)


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
            result = len([*f(test.data)])
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!\n")


if __name__ == "__main__":
    funcs = [classical_prime_gen, sieve_prime_gen]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = repeat(
                stmt=f"{len([*f(test.data)])}",
                repeat=5,
                number=100_000,
                globals=globals(),
            )
            print(f"{f.__name__}({test.data}). Exec time = {min(t):.6f} sec")
        print()
