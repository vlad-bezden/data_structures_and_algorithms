"""Find factorial with a given number of zeros.

Factorial is equal to the product of all positive numbers up to n, starting from one.
Also, zero factorial is, by definition, equal to one.
For example, by number of zeros we mean trailing zeros,
so the number of zeros at the end of a factorial.
For example, the number of zeros at the end of five factorial
is 1 because 5 factorial is equal to 120, which ends with 1 0.
The number of zeros at the end of 100 factorial is 24.
We want to find the smallest number n such that zeros of n,
so the number of trailing zeros at the end of n factorial
is equal to a given number of zeros.
"""

from typing import Optional


def zeros(n: int) -> int:
    """Calculates number of zeroes in factorial number.

    Factorial has 0 if it's devisable by file.
    So we need to find number of times number divisible by 5
    """

    counter = 0

    while n:
        counter += n // 5
        n //= 5

    return counter


def factorial_zeros(num_zeros: int) -> Optional[int]:
    """
    Uses binary search to find factorial that has num_zeros of trailing 0s.
    """
    left = 0
    right = 5 * num_zeros

    while left < right:
        middle = (left + right) // 2
        if zeros(middle) < num_zeros:
            left = middle + 1
        else:
            right = middle

    return left if zeros(left) == num_zeros else None


if __name__ == "__main__":
    tests = [
        (1, 5),
        (2, 10),
        (4, 20),
        (5, None),
        (6, 25),
        (10, 45),
        (11, None),
        (17, None),
    ]

    for data, expected in tests:
        actual = factorial_zeros(data)
        assert expected == actual, f"{data = }, {expected = }, {actual = }"
    print("PASSED!!!")
