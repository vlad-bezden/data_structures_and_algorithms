"""
Performance calculation for memoization, and tabularization

fib took: 28.341462
mem_fib took: 0.000143
tabular_fib took: 0.000181

Memoization is about 200K times faster
"""
from timeit import timeit


LOOKUP_SIZE = 100
number = 30
lookup = [None] * LOOKUP_SIZE


def fib(n):
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


def mem_fib(n):
    """Using memoization"""
    if n <= 2:
        return 1
    if lookup[n] is None:
        lookup[n] = mem_fib(n - 1) + mem_fib(n - 2)

    return lookup[n]


def tabular_fib(n):
    """Using Tabulation"""
    results = [1, 1]
    for i in range(2, n):
        results.append(results[i - 1] + results[i - 2])
    return results[-1]


for f in [fib, mem_fib, tabular_fib]:
    t = timeit(stmt=f"f({number})", number=10, globals=globals())
    print(f"{f.__name__} took: {t:.6f}")
