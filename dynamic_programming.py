"""
Performance calculation for memoization, and tabularization
"""
from timeit import timeit


LOOKUP_SIZE = 10000
number = 25
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


t1 = timeit(stmt=f"fib({number})", number=10, globals=globals())
t2 = timeit(stmt=f"dynamic_fib({number})", number=10, globals=globals())
t3 = timeit(stmt=f"tabular_fib({number})", number=10, globals=globals())

print(f"fib took: {t1:.6f}")
print(f"dyna_fib took: {t2:.6f}")
print(f"tabular_fib took: {t3: 6f}")
