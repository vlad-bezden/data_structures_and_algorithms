"""
Performance calculation for recursion, memoization, tabulation and generator

fib took: 27.052446
mem_fib took: 0.000134
tabular_fib took: 0.000175
yield_fib took: 0.000033
"""
from timeit import timeit


LOOKUP_SIZE = 100
number = 30
lookup = [None] * LOOKUP_SIZE


def fib(n):
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


def mem_fib(n):
    """Using memoization."""
    if n <= 2:
        return 1
    if lookup[n] is None:
        lookup[n] = mem_fib(n - 1) + mem_fib(n - 2)

    return lookup[n]


def tabular_fib(n):
    """Using Tabulation."""
    results = [1, 1]
    for i in range(2, n):
        results.append(results[i - 1] + results[i - 2])
    return results[-1]


def yield_fib(n):
    """Using generator."""
    a = b = 1
    yield a
    yield b
    while n > 2:
        n -= 1
        a, b = b, a + b
        yield b


for f in [fib, mem_fib, tabular_fib, yield_fib]:
    t = timeit(stmt=f"f({number})", number=10, globals=globals())
    print(f"{f.__name__} took: {t:.6f}")
