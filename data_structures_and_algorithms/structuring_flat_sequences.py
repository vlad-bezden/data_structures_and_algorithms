"""
    Sometimes, we'll have raw data that is a flat list of values
    that we'd like to bunch up into subgroups.
"""

SIZE = 5


def group_by_sequence_even(n, sequence):
    """Groups sequence by n number of items
        It will only return number of rows divided evenly.
        Remaining items will not be generated
    """
    data_iter = iter(sequence)
    return [tuple(next(data_iter) for _ in range(n)) for _ in range(len(sequence) // n)]


def group_by_sequence(n, sequence):
    """Groups sequence by n number of items and appends remaining items to the end."""
    data_iter = iter(sequence)
    full_size_items = [
        tuple(next(data_iter) for _ in range(n)) for _ in range(len(sequence) // n)
    ]
    remaining = list(data_iter)
    return full_size_items + [remaining] if remaining else full_size_items


data = range(20)
print(group_by_sequence_even(SIZE, data))

data = range(23)
print(group_by_sequence(SIZE, data))
