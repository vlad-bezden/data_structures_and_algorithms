"""Zig Zag Array
    Solution for StackOverflow question at:
    https://stackoverflow.com/questions/41750670/function-to-create-a-zigzag-array-in-python/60590040#60590040

    I'm trying to create an array of positive and negative integers,
    representing distances north and south of a location -
    I need to see the elements of the array in zigzag order.

    This means that the largest member appears first,
    the smallest member appears second, and the remaining elements alternate
    between the larger members decreasing from the largest
    and the smaller members increasing from the smallest.

    I.e. the array [1, 3, 6, 9, -3] becomes [9, -3, 6, 1, 3].

    Solution description:
    1. Sort your data in reversed order (9, 6, 3, 1, -3)
    2. Split by two lists (9, 6) (3, 1, -3)
    3. Iterate over both (using zip_longest) first one from start,
        second in reverse order (9, -3), (6, 1) (None, 3)
    4. Unpack tuples created by zip_longest (chain(*zip...))
        so you get iterable data (9, -3, 6, 1, None, 3)
    5. Remove None value in case if the list has
        an odd number of elements (if x is not None)
"""

from itertools import zip_longest, chain


def zig_zag_array(data):
    data = sorted(data)
    mid = len(data) // 2
    return [
        x for x in chain(*zip_longest(data[mid:][::-1], data[:mid])) if x is not None
    ]


if __name__ == "__main__":
    data = [1, 3, 6, 9, -3]
    expected = [9, -3, 6, 1, 3]
    output = zig_zag_array(data)
    assert output == expected, f"Odd length: {output=}"

    data = [1, 3, 6, 9, -3, 0]
    expected = [9, -3, 6, 0, 3, 1]
    output = zig_zag_array(data)
    assert output == expected, f"Even length: {output=}"
    print("PASSED")
