"""PowerFizz

    This is an example from "Ten Essays on Fizz Buzz"
    book by Joel Grus
    https://leanpub.com/fizzbuzz

    PowerFizz:
    Print the numbers 1 to N, except that if the number is a perfect square, print
    “fizz”; if the number is a perfect cube, print “buzz”; and if the number is a
    sixth power, print “fizzbuzz”.
"""


import itertools
from typing import Iterator


def power_fizz() -> Iterator[str]:
    squares = (n ** 2 for n in itertools.count(1))
    cubes = (n ** 3 for n in itertools.count(1))

    # Buffer for next element of each iterator
    next_square, next_cube = next(squares), next(cubes)

    for n in itertools.count(1):
        fizz = buzz = ""
        if n == next_square:
            fizz = "fizz"
            next_square = next(squares)
        if n == next_cube:
            buzz = "buzz"
            next_cube = next(cubes)
        yield (fizz + buzz) or str(n)


# Put a "" at the beginning so output[1] is the output for 1
output = [""] + list(itertools.islice(power_fizz(), 1000))

assert output[7 ** 2] == "fizz"
assert output[6 ** 3] == "buzz"
assert output[2 ** 6] == "fizzbuzz"
assert output[3 ** 5] == str(3 ** 5)
assert output[2 ** 7] == str(2 ** 7)

print("PASSED!!!")
