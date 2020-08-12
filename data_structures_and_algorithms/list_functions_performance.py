"""
index, count, in operators performance calculation
"""
from timeit import timeit
from typing import List

SIZE_1 = 10 ** 3
SIZE_2 = 10 ** 6

list_1 = [*range(SIZE_1)]
list_2 = [*range(SIZE_2)]


def in_test(data: List[int]) -> bool:
    """
    Check if last number exist in the list using 'in' operator
    It scans full list to the last element: O(k + 1)

    0.0018 sec
    1.5887 sec
    """
    return data[-1] in data


def count_test(data: List[int]) -> int:
    """
    Counts number of last element in the list occurs in list: O(n)

    0.0019
    1.8211
    """
    return data.count(data[-1])


def len_test(data: List[int]) -> int:
    """
    Testing len function if there is a difference based on size of the list

    0.0002
    0.0002
    """
    return len(data)


def bracket_test(data: List[int]) -> int:
    """
    Testing data[j]

    0.0002
    0.0002
    """
    return data[len(data) - 1]


if __name__ == "__main__":
    for data in [list_1, list_2]:
        t = timeit(stmt=f"in_test(data)", number=100, globals=globals())
        print(f"'in_test': {t:.4f}")
        t = timeit(stmt=f"count_test(data)", number=100, globals=globals())
        print(f"'count_test': {t:.4f}")
        t = timeit(stmt=f"len_test(data)", number=100, globals=globals())
        print(f"'len_test': {t:.4f}")
        t = timeit(stmt=f"bracket_test(data)", number=100, globals=globals())
        print(f"'bracket_test': {t:.4f}")
