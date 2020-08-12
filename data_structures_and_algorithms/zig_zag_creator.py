"""Zig Zag 2D list generator.

    Creates 2D zig zag list of SIZE x SIZE

    Example: SIZE = 4
    [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12], [16, 15, 14, 13]]
"""

from typing import List


def zig_zag(size: int) -> List[List[int]]:
    return [
        [(i if j % 2 == 0 else size - i + 1) + j * size for i in range(1, size + 1)]
        for j in range(size)
    ]


if __name__ == "__main__":
    expected = [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12], [16, 15, 14, 13]]
    assert expected == zig_zag(4), f"{expected=}"
    print("PASSED!!!")
