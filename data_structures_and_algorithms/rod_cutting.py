"""Rod Cutting Problem.

In the rod-cutting problem, the goal is to cut a wooden or metal ord into pieces.
Pieces of different lengths have different values, so you must decide the best way
to cut the rod to maximize the total value.

Output:
VALUES = [1, 2, 4, 6, 7, 9, 10, 10, 10, 11, 12, 12, 15, 20, 20, 20, 20, 20, 25, 30]
The best value for 1 rod cuts are: Result(value=1, cuts=[1]).
Calc time 0.000005 secs
The best value for 2 rod cuts are: Result(value=2, cuts=[2]).
Calc time 0.000007 secs
The best value for 3 rod cuts are: Result(value=4, cuts=[3]).
Calc time 0.000006 secs
The best value for 4 rod cuts are: Result(value=6, cuts=[4]).
Calc time 0.000006 secs
The best value for 5 rod cuts are: Result(value=7, cuts=[5]).
Calc time 0.000006 secs
The best value for 6 rod cuts are: Result(value=9, cuts=[6]).
Calc time 0.000007 secs
The best value for 7 rod cuts are: Result(value=10, cuts=[7]).
Calc time 0.000006 secs
The best value for 8 rod cuts are: Result(value=12, cuts=[4, 4]).
Calc time 0.000009 secs
The best value for 9 rod cuts are: Result(value=13, cuts=[1, 4, 4]).
Calc time 0.000008 secs
The best value for 10 rod cuts are: Result(value=15, cuts=[4, 6]).
Calc time 0.000010 secs
The best value for 11 rod cuts are: Result(value=16, cuts=[1, 4, 6]).
Calc time 0.000010 secs
The best value for 12 rod cuts are: Result(value=18, cuts=[4, 4, 4]).
Calc time 0.000009 secs
The best value for 13 rod cuts are: Result(value=19, cuts=[1, 4, 4, 4]).
Calc time 0.000014 secs
The best value for 14 rod cuts are: Result(value=21, cuts=[4, 4, 6]).
Calc time 0.000010 secs
The best value for 15 rod cuts are: Result(value=22, cuts=[1, 4, 4, 6]).
Calc time 0.000009 secs
The best value for 16 rod cuts are: Result(value=24, cuts=[4, 4, 4, 4]).
Calc time 0.000010 secs
The best value for 17 rod cuts are: Result(value=25, cuts=[1, 4, 4, 4, 4]).
Calc time 0.000018 secs
The best value for 18 rod cuts are: Result(value=27, cuts=[4, 4, 4, 6]).
Calc time 0.000012 secs
The best value for 19 rod cuts are: Result(value=28, cuts=[1, 4, 4, 4, 6]).
Calc time 0.000010 secs
The best value for 20 rod cuts are: Result(value=30, cuts=[20]).
Calc time 0.000010 secs
"""

from dataclasses import dataclass
from functools import lru_cache
from typing import List, Tuple
from timeit import default_timer as t


@dataclass
class Result:
    value: int
    cuts: List[int]

    def update(self, value: int, cuts: List[int]) -> None:
        self.value = value
        self.cuts = cuts


LENGTH = 20

VALUES = [1, 2, 4, 6, 7, 9, 10, 10, 10, 11, 12, 12, 15, 20, 20, 20, 20, 20, 25, 30]

print(f"{VALUES = }")


@lru_cache
def find_optimal_cuts(length: int) -> Result:
    # assume we make no cuts
    best_result = Result(VALUES[length - 1], [length])

    for i in range(1, length // 2 + 1):
        left_result = find_optimal_cuts(i)
        right_result = find_optimal_cuts(length - i)

        # check if this is a better result
        if best_result.value < (best_value := (left_result.value + right_result.value)):
            best_result.update(best_value, left_result.cuts + right_result.cuts)
    return best_result


if __name__ == "__main__":
    for length in range(1, LENGTH + 1):
        t0 = t()
        result = find_optimal_cuts(length)
        t1 = t()
        print(f"The best value for {length} rod cuts are: {result}.")
        print(f"Calc time {t1 - t0:.6f} secs")
