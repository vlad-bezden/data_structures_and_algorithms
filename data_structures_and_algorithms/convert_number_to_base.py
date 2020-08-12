"""Converts number from one base to another numerical base."""

from collections import namedtuple

Test = namedtuple("Test", ["n", "from_base", "to_base", "expected"])


def convert(n: int, from_base: int, to_base: int) -> int:
    digits = []
    while n:
        (n, r) = divmod(n, to_base)
        digits.append(r)

    return sum(from_base ** i * v for i, v in enumerate(digits))


if __name__ == "__main__":
    tests = [
        Test(32, 16, 10, 50),
        Test(32, 20, 10, 62),
        Test(1010, 2, 10, 10),
        Test(8, 10, 8, 10),
        Test(150, 100, 1000, 150),
        Test(1500, 100, 10, 1050000),
    ]

    for test in tests:
        result = convert(*test[:-1])
        assert result == test.expected, f"{test=}, {result=}"
    print("PASSED!!!")
