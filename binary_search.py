import random
from typing import List


data = sorted(random.sample(range(0, 50), 20))
item = random.randint(0, 20)


def binary_search(data:List[int], item:int):
    first = 0
    last = len(data) - 1
    found = False

    while first <= last and not found:
        middle_point = (first + last) // 2
        middle_item = data[middle_point]

        if item == middle_item:
            found = True
        elif item < middle_item:
            last = middle_point - 1
        else:
            first = middle_point + 1

    return middle_point if found else -1


print(f"data: {data}, item to find: {item}, found: {binary_search(data, item)}")
