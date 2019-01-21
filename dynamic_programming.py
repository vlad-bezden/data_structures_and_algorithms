"""
Performance calculation for memoization, and tabularization

fib took: 2.564971
dynamic_fib took: 0.000275
tabular_fib took: 0.000228
"""
from timeit import timeit


LOOKUP_SIZE = 10000
number = 30
lookup = [None] * LOOKUP_SIZE


def fib(n):
    return 1 if n <= 2 else fib(n - 2) + fib(n - 1)


def dyna_fib(n, lookup):
    if n <= 2:
        return 1
    if lookup[n] is None:
        lookup[n] = dyna_fib(n - 1, lookup) + dyna_fib(n - 2, lookup)

    return lookup[n]


def dynamic_fib(n):
    return dyna_fib(n, lookup)


def tabular_fib(n):
    results = [1, 1]
    for i in range(2, n):
        results.append(results[i - 1] + results[i - 2])
    return results[-1]


for f in [fib, dynamic_fib, tabular_fib]:
    t = timeit(stmt=f"f({number})", number=10, globals=globals())
    print(f"{f.__name__} took: {t:.6f}")
