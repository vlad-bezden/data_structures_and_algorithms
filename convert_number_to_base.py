"""Converts number from one base to another numerical base."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Test:
    n: int
    from_base: int
    to_base: int
    expected: int


Tests = [
    Test(32, 16, 10, 50),
    Test(32, 20, 10, 62),
    Test(1010, 2, 10, 10),
    Test(8, 10, 8, 10),
    Test(150, 100, 1000, 150),
    Test(1500, 100, 10, 1050000),
]


def convert(n: int, from_base: int, to_base: int) -> int:
    digits = []
    while n:
        (n, r) = divmod(n, to_base)
        digits.append(r)

    return sum(from_base ** i * v for i, v in enumerate(digits))


if __name__ == "__main__":
    for test in Tests:
        result = convert(test.n, test.from_base, test.to_base)
        assert result == test.expected, f"{test=}, {result=}"
    print("PASSED!!!")
