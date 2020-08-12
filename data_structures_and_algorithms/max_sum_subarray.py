"""Maximum sum subarray problem.

In the array find subarray with the max value.
"""

from typing import List


def max_sum_subbarray(data: List[int]) -> int:
    current_max = max_value = data[0]
    for i in range(1, len(data)):
        current_max = max(current_max + data[i], data[i])
        max_value = max(max_value, current_max)
    return max_value


if __name__ == "__main__":
    tests = [
        ([3, 4, -9, 1, 2], 7),
        ([3, 4, -9, 5, 6], 11),
        ([1, 2, 3], 6),
        ([-1, -2, -3], -1),
    ]

    for data, expected in tests:
        actual = max_sum_subbarray(data)
        assert expected == actual, f"{data = }, {expected = }, {actual = }"
    print("PASSED!!!")
