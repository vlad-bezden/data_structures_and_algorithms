"""Different solution for Fizz Buzz Problem.

    All examples are inspired or provided by "Ten Essays on Fizz Buzz"
    book by Joel Grus
    https://leanpub.com/fizzbuzz


    Outputs:
    fizz_buzz_classic(3003). Exec time = 0.0022 sec
    fizz_buzz_one_line(3003). Exec time = 0.0066 sec
    fizz_buzz_dict(3003). Exec time = 0.0077 sec
    fizz_buzz_cycle(3003). Exec time = 0.0071 sec
    fizz_buzz_euclid(3003). Exec time = 0.0115 sec
    fizz_buzz_iterables(3003). Exec time = 11.8436 sec

    fizz_buzz_classic(5005). Exec time = 0.0038 sec
    fizz_buzz_one_line(5005). Exec time = 0.0065 sec
    fizz_buzz_dict(5005). Exec time = 0.0076 sec
    fizz_buzz_cycle(5005). Exec time = 0.0071 sec
    fizz_buzz_euclid(5005). Exec time = 0.0121 sec
    fizz_buzz_iterables(5005). Exec time = 19.8997 sec

    fizz_buzz_classic(15000). Exec time = 0.0017 sec
    fizz_buzz_one_line(15000). Exec time = 0.0061 sec
    fizz_buzz_dict(15000). Exec time = 0.0074 sec
    fizz_buzz_cycle(15000). Exec time = 0.0071 sec
    fizz_buzz_euclid(15000). Exec time = 0.0096 sec
    fizz_buzz_iterables(15000). Exec time = 59.6678 sec
"""

from math import gcd
from timeit import repeat
from dataclasses import dataclass
from typing import Callable, Sequence
from itertools import cycle, count


@dataclass
class Test:
    data: int
    expected: str


TESTS = [Test(3_003, "fizz"), Test(5_005, "buzz"), Test(15_000, "fizzbuzz")]


def fizz_buzz_iterables(n: int) -> str:
    """Using itertools cycle function."""
    fizz_buzz = (
        (fizz + buzz) or str(i)
        for i, fizz, buzz in zip(
            count(1), cycle(["", "", "fizz"]), cycle(["", "", "", "", "buzz"])
        )
    )
    return [next(fizz_buzz) for _ in range(n)][-1]


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
    ]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = repeat(
                stmt=f"f({test.data})", repeat=3, number=10_000, globals=globals(),
            )
            print(f"{f.__name__}({test.data}). Exec time = {min(t):.4f} sec")
        print()
