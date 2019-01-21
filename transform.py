"""
Transforms 2D array to 90 degree.

Input:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Output:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""

import matrix


def transform(data):
    return [list(x) for x in zip(*data)]


data = matrix.matrix(3, 3, 1)
data_t = transform(data)

assert data_t == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
