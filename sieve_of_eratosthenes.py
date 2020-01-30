"""The Sieve of Eratosthenes.
In mathematics, the Sieve of Eratosthenes is a ancient algorithm for finding all prime
numbers up to any given limit.

It does so by iteratively marking as composite (i.e., not prime) the multiples of
each prime, starting with the first prime number, 2.
The multiples of a given prime are generated as a sequence of numbers starting
from that prime, with constant difference between them that is equal to that prime.
This is the sieve's key distinction from using trial division to sequentially test
each candidate number for divisibility by each prime.

OUTPUT:
    calc_1(10000000) took: 5.224216 seconds
    calc_2(10000000) took: 3.481331 seconds
    calc_3(10000000) took: 2.711713 seconds
    calc_4(10000000) took: 0.142741 seconds
"""

from timeit import timeit
import numpy as np  # type: ignore
from typing import List, Callable, Sequence


def calc_1(n: int) -> List[int]:
    """Classical example to check for each number."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, n // 2):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]


def calc_2(n: int) -> List[int]:
    """Eliminate even numbers and iterate over odd only numbers."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    # eliminate even numbers
    for i in range(4, n + 1, 2):
        sieve[i] = False
    # go through odd only numbers
    for i in range(3, n // 2, 2):
        if sieve[i]:
            for j in range(i * 3, n + 1, i * 2):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]


def calc_3(n: int) -> List[int]:
    """Using square root to reduce number of checks for prime number."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    # eliminate even numbers
    for i in range(4, n + 1, 2):
        sieve[i] = False
    # go through odd only numbers, up to sqrt of all numbers
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            for j in range(i * i, n + 1, i * 2):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]


def calc_4(n: int) -> List[int]:
    """Using numpy."""
    sieve = np.ones(n + 1, dtype=np.bool)
    sieve[0] = sieve[1] = 0
    sieve[4::2] = 0
    for i in range(3, int(np.sqrt(n)) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = 0
    return list(np.nonzero(sieve)[0])


def validate(funcs: Sequence[Callable[[int], List[int]]]) -> None:
    number = 31
    for f in funcs:
        result = f(number)
        assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31], "Failed Validation"
    print("PASSED!!!")


if __name__ == "__main__":
    funcs = [calc_1, calc_2, calc_3, calc_4]
    validate(funcs)
    number = 10_000_000
    for f in funcs:
        t = timeit(stmt=f"f({number})", number=1, globals=globals())
        print(f"{f.__name__}({number}) took: {t:.6f} seconds")
