"""Reversing a Sequence with Recursion"""

from typing import List


def reverse(data: List[int]) -> List[int]:
    if len(data) <= 1:
        return data
    return [data[-1]] + reverse(data[1:-1]) + [data[0]]


def main() -> None:
    data = []
    assert reverse(data) == [], "Empty"
    data = [1]
    assert reverse(data) == [1], "One"
    data = [1, 2]
    assert reverse(data) == [2, 1], "Two"
    data = [1, 2, 3]
    assert reverse(data) == [3, 2, 1], "Three"

    print("Done!")


if __name__ == "__main__":
    main()
