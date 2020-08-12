"""Counting number of subarrays with a given sum.

For instance:
[1, 6, -1, 4, 2, -6]
Sum = 5 => [6, -1], [-1, 4, 2], [6, -1, 4, 2, -6]
"""

from collections import namedtuple
from typing import List, Dict

Test = namedtuple("Test", ["data", "sum_value", "expected"])

tests = [Test([1, 6, -1, 4, 2, -6], 5, 3)]


def naive(data: List, sum_value: int) -> int:
    n = len(data)
    counter = 0
    for i in range(n):
        for j in range(i, n):
            if sum(data[i : j + 1]) == sum_value:
                counter += 1
    return counter


def efficient(data: List, sum_value: int) -> int:
    counter = 0
    prefix_sum_counts: Dict[int, int] = {}
    current_sum = 0
    for v in data:
        current_sum += v
        counter += prefix_sum_counts.get(current_sum - sum_value, 0)
        prefix_sum_counts[current_sum] = prefix_sum_counts.get(current_sum, 0) + 1
    return counter


if __name__ == "__main__":
    for f in [naive, efficient]:
        for test in tests:
            result = f(test.data, test.sum_value)
            assert result == test.expected, f"{test = }, {result = }"
    print("PASSED!!!")
