"""Different solution for Fizz Buzz Problem.

    All examples are inspired or provided by "Ten Essays on Fizz Buzz"
    book by Joel Grus
    https://leanpub.com/fizzbuzz
"""

from typing import Callable


by3: Callable[[int], bool] = lambda n: n % 3 == 0
by5: Callable[[int], bool] = lambda n: n % 5 == 0


def fizz_buzz(n: int) -> str:
    """One liner solution."""
    return ("fizzbuzz", "buzz", "fizz", str(n))[(n % 15, n % 5, n % 3, 0).index(0)]


def fizz_buzz_functional(n: int) -> str:
    """Classsic example by using functions for check."""
    return {
        (True, True): "fizzbuzz",
        (True, False): "fizz",
        (False, True): "buzz",
        (False, False): str(n),
    }[by3(n), by5(n)]


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
        assert fizz_buzz_classic(i) == fizz_buzz(i) == fizz_buzz_functional(i)
    print("PASSED!!!")
