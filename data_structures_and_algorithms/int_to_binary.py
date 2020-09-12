"""Converts integer number to binary.

    Examples:
        1 = 0001
        7 = 0111
        8 = 1000
"""


from typing import List


def int_to_binary(n: int, num_digits: int = 8) -> List[int]:
    digits = []
    for _ in range(num_digits):
        digits.insert(0, n % 2)
        n //= 2
    return digits


for i in range(16):
    print(f"{i:>2} ", "".join(str(i) for i in int_to_binary(i)))
