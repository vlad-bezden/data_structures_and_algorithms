"""Minimum sum path in a matrix

Consider a square matrix.
We want to get from the top left corner to the bottom right corner
such that the sum of the path elements is minimum possible,
and we can only move right or down from a given element.

Assumption:
Matrix is a square (number of rows == number of columns)
"""


def calc(data):
    n = len(data)
    # create matrix the same size as data
    path = [[0 for i in range(n)] for j in range(n)]
    # initialize left upper cell
    path[0][0] = data[0][0]

    # initialize first row and first column
    for i in range(1, n):
        path[0][i] = path[0][i - 1] + data[0][i]
        path[i][0] = path[i - 1][0] + data[i][0]

    # calculate rest of the values in the matrix
    for i in range(1, n):
        for j in range(1, n):
            path[i][j] = data[i][j] + min(path[i][j - 1], path[i - 1][j])
    return path[n - 1][n - 1]


if __name__ == "__main__":
    data = [[4, 3, 4, 31], [1, 15, 9, 11], [71, 13, 10, 6], [21, 41, 51, 2]]
    expected = 38
    result = calc(data)
    assert result == expected, f"{result=}, {expected=}"
    print("PASSED!!!")
