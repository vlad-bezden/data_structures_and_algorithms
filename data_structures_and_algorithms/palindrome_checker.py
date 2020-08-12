"""Palindrome checker.

An interesting problem that can be easily solved using the deque data structure
is the classic palindrome problem. A palindrome is a string that reads the same
forward and backward, for example, radar, toot, and madam.
We would like to construct an algorithm to input a string of characters and check
whether it is a palindrome.

OUTPUT:
is_polindrome_1('lsdkjfskf'). Exec time = 0.007552
is_polindrome_2('lsdkjfskf'). Exec time = 0.003494
is_polindrome_3('lsdkjfskf'). Exec time = 0.009897

is_polindrome_1('abc'). Exec time = 0.006958
is_polindrome_2('abc'). Exec time = 0.003344
is_polindrome_3('abc'). Exec time = 0.008387

is_polindrome_1('ab'). Exec time = 0.007050
is_polindrome_2('ab'). Exec time = 0.004560
is_polindrome_3('ab'). Exec time = 0.009168

is_polindrome_1('abcabcabcabcabcabcabcabcabcabc'). Exec time = 0.011033
is_polindrome_2('abcabcabcabcabcabcabcabcabcabc'). Exec time = 0.004304
is_polindrome_3('abcabcabcabcabcabcabcabcabcabc'). Exec time = 0.011630

is_polindrome_1('abababababababababab'). Exec time = 0.011505
is_polindrome_2('abababababababababab'). Exec time = 0.004614
is_polindrome_3('abababababababababab'). Exec time = 0.011491

is_polindrome_1('radar'). Exec time = 0.008844
is_polindrome_2('radar'). Exec time = 0.006347
is_polindrome_3('radar'). Exec time = 0.015975

is_polindrome_1('tattarrattat'). Exec time = 0.008064
is_polindrome_2('tattarrattat'). Exec time = 0.003461
is_polindrome_3('tattarrattat'). Exec time = 0.023152

is_polindrome_1('aibohphobia'). Exec time = 0.011266
is_polindrome_2('aibohphobia'). Exec time = 0.003907
is_polindrome_3('aibohphobia'). Exec time = 0.021719

Conclusion:
Using reverse string is the fastest way for checking if a string is a palindrome
"""

from collections import deque, namedtuple
from timeit import timeit
from typing import List, Sequence, Callable

Test = namedtuple("Test", ["data", "expected"])

tests = [
    Test("lsdkjfskf", False),
    Test("abc", False),
    Test("ab", False),
    Test("abc" * 10, False),
    Test("ab" * 10, False),
    Test("radar", True),
    Test("tattarrattat", True),
    Test("aibohphobia", True),
]


def is_polindrome_1(string: str) -> bool:
    """Using deque."""
    d = deque(string)
    return True if (l := d.popleft()) and (r := d.pop()) and l == r else False


def is_polindrome_2(string: str) -> bool:
    """Using reverse string and compare two strings."""
    return string == string[::-1]


def is_polindrome_3(string: str) -> bool:
    """Classic example go over each char from left and right and compare them."""
    n = len(string)
    for i in range(n // 2 + 1):
        if string[i] != string[-(i + 1)]:
            return False
    return True


def validate(funcs: Sequence[Callable[[str], bool]]) -> None:
    for test in tests:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!")


if __name__ == "__main__":
    funcs = [is_polindrome_1, is_polindrome_2, is_polindrome_3]
    validate(funcs)
    for test in tests:
        for f in funcs:
            t = timeit(stmt=f"f('{test.data}')", number=10_000, globals=globals())
            print(f"{f.__name__}('{test.data}'). Exec time = {t:.6f}")
        print()
