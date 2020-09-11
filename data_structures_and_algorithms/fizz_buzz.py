"""Different solution for Fizz Buzz Problem.

    All examples are inspired or provided by "Ten Essays on Fizz Buzz"
    book by Joel Grus
    https://leanpub.com/fizzbuzz


    Outputs:
    fizz_buzz_classic(303). Exec time = 0.0003 sec
    fizz_buzz_one_line(303). Exec time = 0.0012 sec
    fizz_buzz_dict(303). Exec time = 0.0016 sec
    fizz_buzz_cycle(303). Exec time = 0.0014 sec
    fizz_buzz_euclid(303). Exec time = 0.0019 sec
    fizz_buzz_iterables(303). Exec time = 0.1371 sec
    fizz_buzz_random(303). Exec time = 0.6533 sec

    fizz_buzz_classic(505). Exec time = 0.0003 sec
    fizz_buzz_one_line(505). Exec time = 0.0007 sec
    fizz_buzz_dict(505). Exec time = 0.0008 sec
    fizz_buzz_cycle(505). Exec time = 0.0014 sec
    fizz_buzz_euclid(505). Exec time = 0.0022 sec
    fizz_buzz_iterables(505). Exec time = 0.2697 sec
    fizz_buzz_random(505). Exec time = 1.0847 sec

    fizz_buzz_classic(555). Exec time = 0.0002 sec
    fizz_buzz_one_line(555). Exec time = 0.0007 sec
    fizz_buzz_dict(555). Exec time = 0.0008 sec
    fizz_buzz_cycle(555). Exec time = 0.0007 sec
    fizz_buzz_euclid(555). Exec time = 0.0010 sec
    fizz_buzz_iterables(555). Exec time = 0.2494 sec
    fizz_buzz_random(555). Exec time = 1.2257 sec
"""

from math import gcd
from timeit import repeat
from typing import Callable, Iterator, NamedTuple, Sequence
from itertools import cycle, count
from random import seed, choice
import numpy as np


class Test(NamedTuple):
    data: int
    expected: str


TESTS = [
    Test(1, "1"),
    Test(2, "2"),
    Test(3, "fizz"),
    Test(4, "4"),
    Test(5, "buzz"),
    Test(6, "fizz"),
    Test(7, "7"),
    Test(8, "8"),
    Test(9, "fizz"),
    Test(10, "buzz"),
    Test(11, "11"),
    Test(12, "fizz"),
    Test(13, "13"),
    Test(14, "14"),
    Test(15, "fizzbuzz"),
    Test(303, "fizz"),
    Test(505, "buzz"),
    Test(555, "fizzbuzz"),
]


def fizz_buzz_matrix(n: int) -> str:
    """Using matrix multiplication."""
    w = np.array([[1, 0, 0], [2, -2, 0], [2, 0, -2], [3, -3, -3]])
    v = np.array([1, n % 3, n % 5])
    return [str(n), "fizz", "buzz", "fizzbuzz"][np.argmax(w @ v)]


def fizz_buzz_random(n: int) -> str:
    """Using random module for generating pseudo-random numbers. Very slow."""
    result: str = ""

    def gen() -> Iterator[str]:
        counts = [count(1)] * 15
        for group in zip(*counts):
            seed(23_977_775)
            for n in group:
                # Just pick at random
                yield choice(["fizzbuzz", "fizz", str(n), "buzz"])

    fizz_buzz = gen()
    for _ in range(n):
        result = next(fizz_buzz)
    return result


def fizz_buzz_iterables(n: int) -> str:
    """Using itertools cycle function. Very slow."""
    result = ""
    fizz_buzz = (
        (fizz + buzz) or str(i)
        for i, fizz, buzz in zip(
            count(1), cycle(["", "", "fizz"]), cycle(["", "", "", "", "buzz"])
        )
    )
    for _ in range(n):
        result = next(fizz_buzz)
    return result


def fizz_buzz_gcd(n: int) -> str:
    """Using math.gcd function."""
    return {1: str(n), 3: "fizz", 5: "buzz", 15: "fizzbuzz"}[gcd(n, 15)]


def fizz_buzz_one_line(n: int) -> str:
    """One liner solution."""
    return ("fizzbuzz", "buzz", "fizz", str(n))[(n % 15, n % 5, n % 3, 0).index(0)]


def fizz_buzz_dict(n: int) -> str:
    """Classsic example by using functions for check."""
    return {
        (True, True): "fizzbuzz",
        (True, False): "fizz",
        (False, True): "buzz",
        (False, False): str(n),
    }[n % 3 == 0, n % 5 == 0]


def fizz_buzz_cycle(n: int) -> str:
    """Using modulo for cycling."""
    DICT_OF_15 = {
        3: "fizz",
        6: "fizz",
        9: "fizz",
        12: "fizz",
        5: "buzz",
        10: "buzz",
        0: "fizzbuzz",
    }
    return DICT_OF_15.get(n % 15, str(n))


def fizz_buzz_euclid(n: int) -> str:
    """Based on Euclid's solution."""
    hi, lo = max(n, 15), min(n, 15)
    while 0 < (r := hi % lo):
        hi, lo = lo, r
    return {1: str(n), 3: "fizz", 5: "buzz", 15: "fizzbuzz"}[lo]


def fizz_buzz_classic(n: int) -> str:
    """Classic example."""
    if n % 15 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    return str(n)


def validate(funcs: Sequence[Callable[[int], str]]) -> None:
    for test in TESTS:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test.data}), {result = }"

    for i in range(1, 1_000):
        assert 1 == len({f(i) for f in funcs})
    print("PASSED!!!\n")


if __name__ == "__main__":
    funcs = [
        fizz_buzz_classic,
        fizz_buzz_one_line,
        fizz_buzz_dict,
        fizz_buzz_cycle,
        fizz_buzz_euclid,
        fizz_buzz_iterables,
        fizz_buzz_random,
        fizz_buzz_matrix,
    ]
    validate(funcs)
    for test in TESTS[-3:]:
        for f in funcs:
            t = repeat(
                stmt=f"f({test.data})", repeat=3, number=1_000, globals=globals(),
            )
            print(f"{f.__name__}({test.data}). Exec time = {min(t):.4f} sec")
        print()
