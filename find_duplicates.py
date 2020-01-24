"""Finds if there are any duplicates in the list.

Three different types of find duplicates. The Counter is the fastest.

using_count took: 2.3854 sec
using_count took: 0.0031 sec
using_count took: 2.3692 sec
using_count took: 0.0030 sec

using_dict took: 0.0536 sec
using_dict took: 0.0009 sec
using_dict took: 0.0543 sec
using_dict took: 0.0009 sec

using_counter took: 0.0144 sec
using_counter took: 0.0015 sec
using_counter took: 0.0139 sec
using_counter took: 0.0015 sec
"""

import random as re
from collections import defaultdict, Counter
import itertools
import timeit

re.seed(42)

long_list = re.sample(range(100_000), 1_000)
short_list = re.sample(range(1_000), 10)
dups_long_list = long_list + long_list[:1]
dups_short_list = short_list + short_list[:1]


def using_count(d):
    """It's O(n**2)."""
    return 1 < max(d.count(x) for x in set(d))


def using_dict(d):
    """It's O(n)"""
    counter = defaultdict(int)
    for i in d:
        counter[i] += 1
    return 1 < max(counter.values())


def using_counter(d):
    """Using Counter from Python standard library."""
    counter = Counter(d)
    return 1 < max(counter.values())


if __name__ == "__main__":
    funcs = [using_count, using_dict, using_counter]
    data = [long_list, short_list, dups_long_list, dups_short_list]

    for f, d in itertools.product(funcs, data):
        t = timeit.timeit(stmt=f"f({d})", number=100, globals=globals())
        print(f"{f.__name__} took: {t:.4f} sec")

