"""Find the Missing Number
You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list.
One of the integers is missing in the list.
Write an efficient code to find the missing integer.

Example :

Input: [1, 2, 4, 6, 3, 7, 8]
Output: 5
"""

from typing import List
from dataclasses import dataclass


@dataclass
class Test:
    data: List[int]
    expected: int


def find_missing(data: List[int]) -> int:
    n = len(data)
    total = (n + 1) * (n + 2) // 2
    total_data = sum(data)
    return total - total_data


if __name__ == "__main__":
    tests = [
        Test([1, 3], 2),
        Test([2, 3], 1),
        Test([*range(1, 5), *range(6, 9)], 5),
        Test([*range(1, 10), *range(11, 20)], 10),
    ]

    for test in tests:
        result = find_missing(test.data)
        assert result == test.expected, f"{test=}, {result=}"

    print("PASSED!!!")
