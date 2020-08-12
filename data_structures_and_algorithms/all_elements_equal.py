"""
Check if all elements in a list are the equal.

Output:
    using_set took: 0.332290
    using_compare took: 0.220397
"""

from typing import List
import numpy as np
from timeit import timeit


data:List[int] = np.random.randint(1, 100, 1_000_000).tolist()
print(f"{len(data) = }")


def using_set(data:List[int]) -> bool:
    return len(set(data)) <= 1


def using_compare(data:List[int]) -> bool:
    return data[1:] == data[:-1]


if __name__ == "__main__":
    for f in [
        using_set,
        using_compare,
    ]:
        t = timeit(stmt=f"f({data})", number=10, globals=globals())
        print(f"{f.__name__} took: {t:.6f}")
