"""Different solution for Fizz Buzz Problem.

    All examples are inspired or provided by "Ten Essays on Fizz Buzz"
    book by Joel Grus
    https://leanpub.com/fizzbuzz
"""

from math import gcd


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


if __name__ == "__main__":
    for i in range(1, 101):
        assert (
            fizz_buzz_classic(i)
            == fizz_buzz_one_line(i)
            == fizz_buzz_dict(i)
            == fizz_buzz_cycle(i)
            == fizz_buzz_euclid(i)
            == fizz_buzz_gcd(i)
        )
    print("PASSED!!!")
