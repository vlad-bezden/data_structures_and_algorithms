"""Add two numbers represented by lists

Solution for the problem as described at:
https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/

Given two numbers represented by two lists, write a function that returns the sum list.
The sum list is list representation of the addition of two input numbers.

For instance:
    1.
    num1 = [1, 2, 3]
    num2 = [4, 5, 6]
    num1 + num2 = [5, 7, 9]
    2.
    num1 = [9, 8, 9]
    num2 = [6, 9, 9]
    num1 + num2 = [1, 6, 8, 8]
"""

from typing import List
from itertools import zip_longest
from dataclasses import dataclass


@dataclass
class Test:
    nums1: List[int]
    nums2: List[int]
    expected: List[int]


def calculate(nums1: List[int], nums2: List[int]) -> List[int]:
    result = [0] * max(len(nums1), len(nums2))
    carry_over = 0

    for i, v in enumerate(zip_longest(reversed(nums1), reversed(nums2), fillvalue=0)):
        d, r = divmod(sum(v) + carry_over, 10)
        result[i] = r
        carry_over = d

    if carry_over:
        result = result + [d]

    return list(reversed(result))


if __name__ == "__main__":
    tests = [
        Test([5, 6, 3], [8, 4, 2], [1, 4, 0, 5]),
        Test([1, 2, 3], [4, 5, 6], [5, 7, 9]),
        Test([9, 8, 9], [6, 9, 9], [1, 6, 8, 8]),
        Test([2, 4, 6, 8, 9], [8, 9], [2, 4, 7, 7, 8]),
        Test([9, 9], [9, 9], [1, 9, 8]),
        Test([9], [9, 1], [1, 0, 0]),
    ]
    for test in tests:
        result = calculate(test.nums1, test.nums2)
        assert test.expected == result, f"{test=}, {result=}"
    print("DONE!!!")
