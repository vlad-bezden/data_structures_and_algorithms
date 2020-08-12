"""
Groups list of items in tuples of size n
"""

from typing import Iterable, Any, Tuple


def grouper(data: Iterable[Any], n: int) -> Iterable[Tuple[Any]]:
    iters = [iter(data)] * n
    return zip(*iters)


if __name__ == "__main__":
    print(list(grouper(range(9), 3)))
    # [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
