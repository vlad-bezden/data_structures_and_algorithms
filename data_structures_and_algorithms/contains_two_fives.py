"""
The function determines if a number contains at least two fives.

For example:
contains_two_fives(1234) == False
contains_two_fives(1534) == False
contains_two_fives(1535) == True
contains_two_fives(5505) == True

Performance:
contains_two_fives_loop took: 0.0167
contains_two_fives_recursion took: 0.0089
contains_two_fives_str took: 0.0043
"""

from timeit import timeit


def contains_two_fives_loop(n: int) -> bool:
    counter = 0
    while n:
        counter += n % 10 == 5
        n //= 10
    return 2 <= counter


def contains_two_fives_recursion(n: int) -> bool:
    return 2 <= (n % 10) == 5 + contains_two_fives_recursion(n // 10)


def contains_two_fives_str(n: int) -> bool:
    return 2 <= str(n).count("5")


for f in [
    contains_two_fives_loop,
    contains_two_fives_recursion,
    contains_two_fives_str,
]:
    assert f(1234) is False
    assert f(1534) is False
    assert f(1535) is True
    assert f(5505) is True
    t = timeit(stmt="f(12345678905)", number=1000, globals=globals())
    print(f"{f.__name__} took: {t:.4f}")
