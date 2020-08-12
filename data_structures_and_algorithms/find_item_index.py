"""Find index of the item in collection.

    Finds an index of the item in the collection by:
    1. Using 'index' method
    2. using 'bisect' module

    Results:
        index=0, index: t1=0.0002, bisect: t2=0.0008, diffs t1/t2=0.26
        index=100, index: t1=0.0017, bisect: t2=0.0008, diffs t1/t2=2.17
        index=200, index: t1=0.0032, bisect: t2=0.0008, diffs t1/t2=4.27
        index=300, index: t1=0.0047, bisect: t2=0.0008, diffs t1/t2=5.80
        index=400, index: t1=0.0063, bisect: t2=0.0009, diffs t1/t2=7.35
        index=500, index: t1=0.0076, bisect: t2=0.0009, diffs t1/t2=8.62
        index=600, index: t1=0.0091, bisect: t2=0.0009, diffs t1/t2=10.62
        index=700, index: t1=0.0105, bisect: t2=0.0009, diffs t1/t2=12.08
        index=800, index: t1=0.0120, bisect: t2=0.0008, diffs t1/t2=15.89
        index=900, index: t1=0.0136, bisect: t2=0.0008, diffs t1/t2=16.91
        index=1000, index: t1=0.0150, bisect: t2=0.0008, diffs t1/t2=19.29

    bisect performs faster than index, and if performs much faster with
    data increase
"""

import bisect
from timeit import timeit


def bisect_search(container, index, default=-1):
    return (
        index
        if (index := bisect.bisect_left(container, index)) < len(container)
        and container[index] == index
        else default
    )


if __name__ == "__main__":
    n = 1000
    data = list(range(n + 1))
    index = 666
    # times to test
    times_to_test = 1000

    for index in range(0, n + 1, 100):
        t1 = timeit(lambda: data.index(index), number=times_to_test)
        t2 = timeit(lambda: bisect_search(data, index), number=times_to_test)

        print(f"{index=}, index: {t1=:.4f}, bisect: {t2=:.4f}, diffs {t1/t2=:.2f}")
