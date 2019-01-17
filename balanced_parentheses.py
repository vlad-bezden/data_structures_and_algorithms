"""
Given a sequence consisting of parentheses,
determine whether the expression is balanced.
"""


def is_balanced(expression: str) -> bool:
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


if __name__ == "__main__":
    assert is_balanced("[{({[]})}]") is True
    assert is_balanced("") is True
    assert is_balanced("[](){}") is True
    assert is_balanced("[()]{}") is True
    assert is_balanced("[({}[])]") is True
    assert is_balanced("[]{([))}") is False

    print("PASSED")
