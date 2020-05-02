"""Compare any and all performance

    Check if any is using short circut.
    This test proves that indeed 'all' is using short circut.

    Output:
    is_prime_any. Exec time: 81.4776
    is_prime_all. Exec time: 84.8617
"""

import math
from timeit import timeit
from time import time


def is_prime_any(n: int) -> bool:
    return lambda n: not any(n % p == 0 for p in range(2, int(math.sqrt(n)) + 1))


def is_prime_all(n: int) -> bool:
    return lambda n: all(n % p != 0 for p in range(2, int(math.sqrt(n)) + 1))


times = 1
n = 999984

for f in [is_prime_any, is_prime_all]:
    t = time()
    for x in range(n):
        timeit(stmt=f"f({x})", number=times, globals=globals())
    print(f"{f.__name__}. Exec time: {time() - t:.4f}")
