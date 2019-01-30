"""
Examples of how to create 2D matrix, multiply by scalar and dot operation
"""

from typing import List

Matrix = List[List[int]]


def matrix(rows: int, cols: int, start: int = 0) -> Matrix:
    return [[c + start + r * cols for c in range(cols)] for r in range(rows)]


def multiply(matrix: Matrix, n: int) -> Matrix:
    return [[col * n for col in row] for row in matrix]


def dot(m1: Matrix, m2: Matrix) -> Matrix:
    """Dot product of two matrixes"""
    # validate if number of rows in the first matrix
    # is the same as number of columns in the second matrix
    if len(m1[0]) != len(m2):
        raise ValueError(
            "Number of rows in the first matrix "
            "must match number of columns the second matrix"
        )

    return [
        [sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*m2)] for m1_r in m1
    ]


def main() -> None:
    m = matrix(2, 3, 1)
    assert m == [[1, 2, 3], [4, 5, 6]]
    result = multiply(m, 4)
    assert result == [[4, 8, 12], [16, 20, 24]]
    m1 = matrix(3, 3)
    m2 = matrix(4, 2)
    try:
        result = dot(m1, m2)
        assert False
    except ValueError as ex:
        print(ex)
    m2 = matrix(3, 2)
    result = dot(m1, m2)
    assert result == [[10, 13], [28, 40], [46, 67]]
    m1 = matrix(2, 3, 1)
    m2 = matrix(3, 2, 7)
    result = dot(m1, m2)
    assert result == [[58, 64], [139, 154]]


if __name__ == "__main__":
    main()
    print("Done!!!")
