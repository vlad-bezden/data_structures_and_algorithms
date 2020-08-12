"""Classical balanced parenthesis problem

Given a sequence consisting of parentheses,
determine whether the expression is balanced.

is_balanced_1('[{({[]})}]'). Exec time = 0.052175
is_balanced_2('[{({[]})}]'). Exec time = 0.068144

is_balanced_1('OMITTED BECAUSE TOO LONG ("[{({[]})}]" * 100)'). Exec time = 4.515048
is_balanced_2('OMITTED BECAUSE TOO LONG ("[{({[]})}]" * 100)'). Exec time = 0.298920

is_balanced_1('[](){}'). Exec time = 0.040901
is_balanced_2('[](){}'). Exec time = 0.028327

is_balanced_1('OMITTED BECAUSE TOO LONG ("[](){}" * 100)'). Exec time = 3.031309
is_balanced_2('OMITTED BECAUSE TOO LONG ("[](){}" * 100)'). Exec time = 0.091780

is_balanced_1(''). Exec time = 0.010686
is_balanced_2(''). Exec time = 0.014911

is_balanced_1('[()]{}'). Exec time = 0.042118
is_balanced_2('[()]{}'). Exec time = 0.037112

is_balanced_1('[({}[])]'). Exec time = 0.042690
is_balanced_2('[({}[])]'). Exec time = 0.050359

is_balanced_1('[]{([))}'). Exec time = 0.037194
is_balanced_2('[]{([))}'). Exec time = 0.024557

is_balanced_1('OMITTED BECAUSE TOO LONG ("[]{([))}" * 100)'). Exec time = 0.036458
is_balanced_2('OMITTED BECAUSE TOO LONG ("[]{([))}" * 100)'). Exec time = 0.099932

Conclusion:
    For a long balanced expressions replace is much faster. However for unbalanced
    expressions dictionary works faster
"""

from typing import Sequence, Callable
from collections import namedtuple
from timeit import timeit

Test = namedtuple("Test", ["data", "expected"])

tests = [
    Test("[{({[]})}]", True),
    Test("[{({[]})}]" * 100, True),
    Test("[](){}", True),
    Test("[](){}" * 100, True),
    Test("", True),
    Test("[()]{}", True),
    Test("[({}[])]", True),
    Test("[]{([))}", False),
    Test("[]{([))}" * 100, False),
]


def is_balanced_1(expression: str) -> bool:
    """Using dictionary for mapping and stack for validation."""
    mapping = dict(zip("({[", ")}]"))
    stack = []

    for p in expression:
        if p in mapping:
            stack.append(mapping[p])
        elif p not in mapping.values():
            raise ValueError(f"Invalid: '{p}' letter in expression")
        elif not (stack and stack.pop() == p):
            return False
    return not stack


def is_balanced_2(expression: str) -> bool:
    """Check for pairs instead of individual char and if they exist delete from expr."""
    brackets = set(["()", "[]", "{}"])

    while (brs := [br for br in brackets if br in expression]):
        expression = expression.replace(brs[0], "")
    return not expression


def validate(funcs: Sequence[Callable[[str], bool]]) -> None:
    for test in tests:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!")


if __name__ == "__main__":
    funcs = [is_balanced_1, is_balanced_2]
    validate(funcs)
    for test in tests:
        for f in funcs:
            t = timeit(stmt=f"f('{test.data}')", number=10_000, globals=globals())
            print(f"{f.__name__}('{test.data}'). Exec time = {t:.6f}")
        print()
