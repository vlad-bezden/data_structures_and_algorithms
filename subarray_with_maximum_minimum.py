"""Subarray with the maximum minimum

Given the length of the subarray find the maximum-minimum of the subarray.

Example:

data = [2, 1, 4, 5, 6, 1, 9]
length = 3

1. [2, 1, 4] -> 1
2. [1, 4, 5] -> 1
3. [4, 5, 6] -> 4
4. [5, 6, 1] -> 1
5. [6, 1, 9] -> 1

Result: maximum of minimums - max([1, 1, 4, 1, 1]) = 4
"""

from typing import List
from collections import namedtuple, deque
from timeit import timeit
import random

Test = namedtuple("Test", ["data", "size", "expected"])

Tests = [
    Test([2, 1, 4, 5, 6, 1, 9], 3, 4),
    Test([3, 4, -9, 1, 2], 2, 3),
    Test([3, 4, -9, 5, 6, 7, 20, 2, 1], 3, 6),
    Test([1, 2, 3], 1, 3),
    Test([-1, -2, -3], 1, -1),
]


def naive(data: List[int], size: int) -> int:
    """
    This performs O(n^2) solution
    """
    max_val = data[0]
    for i in range(len(data) - size + 1):
        current_min = min(data[i : i + size])
        max_val = max(current_min, max_val)

    return max_val


def calc_with_deque(data: List[int], size: int) -> int:
    """
    Performs O(n) solution
    """
    max_val = data[0]
    d = deque([0])
    for i, _ in enumerate(data):
        if i - d[0] == size:
            d.popleft()
        while len(d) and data[d[-1]] >= data[i]:
            d.pop()
        d.append(i)
        if i >= size:
            max_val = max(max_val, data[d[0]])

    return max_val


def validation() -> None:
    """Performs functions validations."""
    for f in [naive, calc_with_deque]:
        for test in Tests:
            actual = f(test.data, test.size)
            assert test.expected == actual, f"{test = }. {actual = }"
    print("PASSED!!!")


def test_data(tests_number: int) -> List[Test]:
    """Generates test data."""
    tests = []

    for i in range(tests_number):
        size = random.randint(1, 100)
        data = random.sample(
            range(1, size * 1_000_000), random.randint(1, size * 1_000)
        )
        tests.append(Test(data, size, None))

    return tests


if __name__ == "__main__":
    validation()

    tests = test_data(10)
    for test in tests:
        print(f"\ndata len = {len(test.data)}, size = {test.size:}")
        for f in [calc_with_deque, naive]:
            t = timeit(f"f({test.data}, {test.size})", number=10, globals=globals())
            print(f"{f.__name__:20} time = {t:.4f} secs")

    print("DONE!!!")
