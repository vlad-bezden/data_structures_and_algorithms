"""Find values in list of items using Binary Search.

    Binary Search assumes that all items are sorted.
    This example provides all values in the data using binary search
    for all sort of data, sorted and unsorted and returns only
    values that are binary search will find out.

    Examples:
    [1, 2, 5, 4, 6, 3, 7, 8, 10, 9] -> [1, 2, 7, 8, 10]
"""

from bisect import bisect_left
from typing import Sequence


def find_items(items: Sequence[int]) -> Sequence[int]:
    result = []
    for item in items:
        if (idx := bisect_left(items, item)) < len(items) and items[idx] == item:
            result.append(item)

    return result


if __name__ == "__main__":
    assert find_items([1, 2, 5, 4, 6, 3, 7, 8, 10, 9]) == [1, 2, 7, 8, 10]
    assert find_items([5, 3, 2, 4, 6, 8, 7, 9, 10, 1]) == [4, 6, 8, 9, 10]
    assert find_items(range(10)) == [*range(10)], "All sorted"
    assert find_items([]) == []

    print("PASSED!!!")
