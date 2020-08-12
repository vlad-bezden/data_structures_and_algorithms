"""Has Pair with sum.

Solution for Google's an interview question at:
https://www.youtube.com/watch?v=XKu_SEDAykw&t=1s
"""


def has_pair_with_sum(data, sum):
    visited = set()
    for i in data:
        if sum - i in visited:
            return True
        visited.add(i)
    return False


if __name__ == "__main__":
    assert has_pair_with_sum([1, 2, 3, 9], 8) is False, "No pairs"
    assert has_pair_with_sum([1, 2, 4, 4], 8) is True, "Found 4 and 4"
    assert has_pair_with_sum([1, 2, 3, 5], 8) is True, "Found 3 and 5"
    assert has_pair_with_sum([1, 2, 3, 4, 6, 9], 8) is True, "Found 2 and 6"
    assert has_pair_with_sum([8], 8) is False, "8, No pairs"
    assert has_pair_with_sum([], 8) is False, "[], No pairs"

    print("Passed Test!!!")
