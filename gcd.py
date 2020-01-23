"""Find the greatest common divisor of a and b."""


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    assert gcd(180, 150) == 30, "180/150"
    assert gcd(200, 15) == 5, "200/15"
    assert gcd(42, 56) == 14, "42/56"
    assert gcd(10, 9) == 1, "10/9"
    assert gcd(270, 192) == 6, "270/192"
