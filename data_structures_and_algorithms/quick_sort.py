"""Example of quick sort using recursion"""

import random
from typing import List


def quick_sort(data: List[int]) -> List[int]:
    if len(data) < 2:
        return data
    pivot, left, right = data.pop(), [], []
    for item in data:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    data = random.sample(range(1000), 15)
    print(data)
    print(quick_sort(data))
