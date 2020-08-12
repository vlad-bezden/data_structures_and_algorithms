"""Coordinates Generator.

An example of using product, map, and range to generate
any shape of the array.

Output:
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

    points_by_list_comprehension, t=0.0002
    points_by_list_comprehension, t=0.0107
    points_by_list_comprehension, t=1.3254

    points_by_product, t=0.0001
    points_by_product, t=0.0064
    points_by_product, t=0.8818
"""

from itertools import product
from timeit import timeit


x = 10 ** 3
y = 10 ** 4


def points_by_list_comprehension(shape):
    return [(i, j) for i in range(shape[0]) for j in range(shape[1])]


def points_by_product(shape):
    return [*product(*map(range, shape))]


if __name__ == "__main__":
    funcs = [points_by_list_comprehension, points_by_product]
    for f in funcs:
        print(f((2, 3)))
    print()

    shapes = [(10 ** i, 10 ** i) for i in range(1, 4)]
    for func in funcs:
        for shape in shapes:
            t = timeit(stmt=f"func({shape})", number=10, globals=globals())
            print(f"{func.__name__}, {t=:.4f}")
        print()
