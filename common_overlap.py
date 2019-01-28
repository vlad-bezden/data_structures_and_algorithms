"""
Finds longest index overlap
"""

from collections import namedtuple
import unittest

Match = namedtuple("Match", ["length", "s1_index", "s2_index"])


def overlap_index(text1, text2):
    """
    Returns starting match index and matching length.

    This one assumes that overlap starts at the beginning of the string
    """
    best = 0
    length = 1
    while True:
        pattern = text1[-length:]
        found = text2.find(pattern)
        if found == -1:
            return len(text1) - best, best
        length += found
        if text1[-length:] == text2[:length]:
            best = length
            length += 1


def overlap(text1, text2):
    """
    Returns longest overlap, between two strings
    """
    index_a = -1
    index_b = -1
    best_match_length = 0
    i = 0
    text1_length = len(text1)

    while i < text1_length:
        for j, c in enumerate(text2):
            if i + j < text1_length and text1[i + j] == c:
                match_length = 1
                while (
                    i + j + match_length < text1_length
                    and text1[i + j + match_length] == text2[j + match_length]
                ):
                    match_length += 1
                if best_match_length < match_length:
                    best_match_length = match_length
                    index_a = i + j
                    index_b = j
        i += 1
    return Match(best_match_length, index_a, index_b)


class Tests(unittest.TestCase):
    def test_overlap_index_1(self):
        a = "python"
        b = "honbe"
        result = overlap_index(a, b)
        self.assertEqual(result, (3, 3))

    def test_overlap_index_2(self):
        a = "Python is amazing language"
        b = "languages express meaning"
        result = overlap_index(a, b)
        self.assertEqual(result, (18, 8))

    def test_overlap_1(self):
        a = "colors"
        b = "antique"
        result = overlap(a, b)
        self.assertEqual(result, Match(0, -1, -1))

    def test_overlap_2(self):
        a = "Python is amazing language"
        b = "Best languages in the world?"
        result = overlap(a, b)
        self.assertEqual(
            a[result.s1_index : result.s1_index + result.length],
            b[result.s2_index : result.s2_index + result.length],
        )


if __name__ == "__main__":
    unittest.main()
