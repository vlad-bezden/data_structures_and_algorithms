"""
Python lacks a way to store more than a value for each key in a dictionary.
This is a very common need, and most languages provide some form of multimap container.
Python tends to prefer having a single way of doing things,
and as storing multiple values for the keymeans just storing a list of values
for a key, it doesn't provide a specialized container.
"""

from collections import defaultdict


def reverse_dict(data: dict) -> dict:
    rd = defaultdict(list)
    for k, v in data.items():
        rd[v].append(k)
    return rd


if __name__ == "__main__":
    from collections import Counter

    data = "aaa bbb ccc ddd aaa bbb ccc aaa"
    c = Counter(data.split())
    print(c)
    # Counter({'aaa': 3, 'bbb': 2, 'ccc': 2, 'ddd': 1})
    rd = reverse_dict(c)
    print(rd)
    # defaultdict(<class 'list'>, {3: ['aaa'], 2: ['bbb', 'ccc'], 1: ['ddd']})
