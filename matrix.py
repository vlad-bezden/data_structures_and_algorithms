"""
Creates 2D matrix
"""


def matrix(rows, cols, start=0):
    return [[c + start + r * cols for c in range(cols)] for r in range(rows)]


assert matrix(2, 3, 1) == [[1, 2, 3], [4, 5, 6]]
