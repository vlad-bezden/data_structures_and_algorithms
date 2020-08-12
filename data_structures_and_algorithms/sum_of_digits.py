"""Sum of digits in a number.

Calculates the sum of digits in the number using regular while and recursion methods.

Example:
2348 = 17

Input:
n: integer >= 0

Outputs:
sum_digits_while n = 23847298420. time = 0.0041 secs
sum_digits_while n = 1. time = 0.0005 secs
sum_digits_while n = 0. time = 0.0003 secs
sum_digits_while n = 293847209384209348203984. time = 0.0108 secs
sum_digits_while n = 239847270348. time = 0.0040 secs
sum_digits_while n = 239874208. time = 0.0022 secs
sum_digits_while n = 2390842083. time = 0.0026 secs
sum_digits_while n = 23984729834723433. time = 0.0048 secs

sum_digits_recursion n = 23847298420. time = 0.0039 secs
sum_digits_recursion n = 1. time = 0.0004 secs
sum_digits_recursion n = 0. time = 0.0002 secs
sum_digits_recursion n = 293847209384209348203984. time = 0.0091 secs
sum_digits_recursion n = 239847270348. time = 0.0046 secs
sum_digits_recursion n = 239874208. time = 0.0032 secs
sum_digits_recursion n = 2390842083. time = 0.0037 secs
sum_digits_recursion n = 23984729834723433. time = 0.0068 secs
"""

from timeit import timeit
from collections import namedtuple

Input = namedtuple("Input", ["number", "expected"])

Inputs = [
    Input(23847298420, 49),
    Input(1, 1),
    Input(0, 0),
    Input(293847209384209348203984, 111),
    Input(239847270348, 57),
    Input(239874208, 43),
    Input(2390842083, 39),
    Input(23984729834723433, 81),
]


def sum_digits_recursion(n: int) -> int:
    """Using recursion."""
    if n == 0:
        return 0
    return (n % 10) + sum_digits_recursion(n // 10)


def sum_digits_while(n: int) -> int:
    """Using classical while loop."""
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum


def validation() -> None:
    """Performs functions validation."""
    for f in [sum_digits_while, sum_digits_recursion]:
        for n in Inputs:
            actual = f(n.number)
            assert n.expected == actual, f"{n = }. {actual = }"
    print("PASSED!!!")


if __name__ == "__main__":
    validation()

    for f in [sum_digits_while, sum_digits_recursion]:
        print()
        for n, _ in Inputs:
            t = timeit(f"f({n})", number=1_000, globals=globals())
            print(f"{f.__name__} {n = }. time = {t:.4f} secs")
