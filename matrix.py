"""Matrix class implementation"""

import unittest
from typing import List, Tuple

MatrixType = List[List[int]]


class Matrix:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix = self.matrix(rows, cols)

    @staticmethod
    def matrix(rows: int, cols: int) -> MatrixType:
        """
        Creates matrix [rows, cols] size
        and initialize values from 0 to rows * cols
        """
        return [[r * cols + c for c in range(cols)] for r in range(rows)]

    def T(self, inplace: bool = False) -> MatrixType:
        """
        Transpose matrix

        if inplace = True will replace existing matrix to T otherwise will just create
        new matrix
        """
        result = []
        for c in range(self.cols):
            t = []
            for r in range(self.rows):
                t.append(self.matrix[r][c])
            result.append(t)
        if inplace:
            self.rows, self.cols = self.cols, self.rows
            self.matrix = result
        return result

    def __getitem__(self, index: int) -> List[int]:
        return self.matrix[index]

    def __repr__(self) -> str:
        return f"matrix: {self.size}, {self.matrix}"

    @property
    def shape(self) -> Tuple[int, int]:
        """Returns size of the matrix."""
        return self.rows, self.cols

    def multiply(self, n: int, inplace: bool = False) -> MatrixType:
        """Multiplies matrix by n value."""
        result = [
            [self.matrix[r][c] * n for c in range(self.cols)] for r in range(self.rows)
        ]
        if inplace:
            self.matrix = result
        return result

    def dot(self, other: MatrixType, inplace: bool = False) -> MatrixType:
        """Performs matrix dot operation."""
        if self.rows != other.cols:
            raise ValueError("Number of rows doesn't match number of columns")
        result = [
            [sum(a * b for a, b in zip(m_1, m_2)) for m_2 in zip(*other)]
            for m_1 in self.matrix
        ]
        if inplace:
            self.matrix = result
        return result


class Tests(unittest.TestCase):
    def test_square_matrix(self):
        rows = cols = 4
        matrix = Matrix(rows, cols)
        self.assertEqual(matrix.shape, (rows, cols))
        self.assertEqual(matrix[0], [0, 1, 2, 3])
        self.assertEqual(matrix[rows - 1], [12, 13, 14, 15])

    def test_rectangular_matrix(self):
        rows = 4
        cols = 2
        matrix = Matrix(rows, cols)
        self.assertEqual(matrix.shape, (rows, cols))
        self.assertEqual(matrix[0], [0, 1])
        self.assertEqual(matrix[rows - 1], [6, 7])

    def test_square_transform(self):
        rows = cols = 3
        matrix = Matrix(rows, cols)
        self.assertEqual(matrix.matrix, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        matrix_t = matrix.T()
        self.assertEqual(matrix_t, [[0, 3, 6], [1, 4, 7], [2, 5, 8]])
        self.assertEqual(matrix.matrix, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        matrix.T(inplace=True)
        self.assertEqual(matrix.matrix, [[0, 3, 6], [1, 4, 7], [2, 5, 8]])

    def test_multiply(self):
        rows = 2
        cols = 3
        m = Matrix(rows, cols)
        m.multiply(3, inplace=True)
        self.assertEqual(m.matrix, [[0, 3, 6], [9, 12, 15]])

    def test_dot(self):
        m_1 = Matrix(3, 2)
        m_2 = Matrix(2, 3)
        result = m_1.dot(m_2)
        self.assertEqual(result, [[3, 4, 5], [9, 14, 19], [15, 24, 33]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
