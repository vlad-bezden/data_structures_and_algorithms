"""
Finds longest index overlap
"""

from collections import namedtuple
import unittest

Match = namedtuple("Match", ["length", "s1_index", "s2_index"])


def overlap(text1, text2):
    """
    Returns longest overlap, between two strings
    """
    best_match = Match(0, -1, -1)
    i = 0
    text1_length = len(text1)

    while i < text1_length:
        for j, c1, c2 in (
            (j, *t) for j, t in enumerate(zip(text1[i:], text2)) if t[0] == t[1]
        ):
            match_length = 1
            while (
                i + j + match_length < text1_length
                and text1[i + j + match_length] == text2[j + match_length]
            ):
                match_length += 1
            if best_match.length < match_length:
                best_match = Match(match_length, i + j, j)
                i += match_length
            break
        i += 1
    return best_match


class Tests(unittest.TestCase):
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
            a[result.s1_index : result.s1_index + result.length], " language"
        )
        self.assertEqual(
            b[result.s2_index : result.s2_index + result.length], " language"
        )


if __name__ == "__main__":
    unittest.main()
