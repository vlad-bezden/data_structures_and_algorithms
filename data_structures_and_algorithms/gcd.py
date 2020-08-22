"""Find the greatest common divisor (GCD) of a and b."""


def gcd(a: int, b: int) -> int:
    """GCD using recursion."""
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd2(a: int, b: int) -> int:
    """GCD using loop."""
    a, b = max(a, b), min(a, b)
    while d := a % b:
        a, b = b, d
    return b


if __name__ == "__main__":
    funcs = [gcd, gcd2]

    for func in funcs:
        assert func(180, 150) == 30, "180/150"
        assert func(200, 15) == 5, "200/15"
        assert func(42, 56) == 14, "42/56"
        assert func(10, 9) == 1, "10/9"
        assert func(270, 192) == 6, "270/192"

    print("PASSED!!!")
