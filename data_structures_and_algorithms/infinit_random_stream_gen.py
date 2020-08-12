"""
Generate infinite stream of odd numbers between 1 and 99 inclusive
"""

import itertools
import random

gen = (random.randrange(1, 100, 2) for _ in itertools.cycle("_"))
gen2 = (random.randrange(1, 100, 2) for _ in itertools.count())


def run(gen):
    for i, n in enumerate(gen, start=1):
        # assert n is a odd number and between 1 and 100
        assert n % 2, 1
        assert 1 <= n < 100
        print(i, n)
        if i == 100:
            print("=" * 10)
            break


for g in (gen, gen2):
    run(g)
