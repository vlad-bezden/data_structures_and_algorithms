"""
Finds longest index overlap that starts at the beginning of the string
"""

import unittest


def overlap_index(text1, text2):
    """Returns starting match index and matching length."""
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


class Tests(unittest.TestCase):
    def test_overlap_1(self):
        a = "python"
        b = "honbe"
        result = overlap_index(a, b)
        self.assertEqual(result, (3, 3))

    def test_overlap_2(self):
        a = "Python is amazing language"
        b = "languages express meaning"
        result = overlap_index(a, b)
        self.assertEqual(result, (18, 8))


if __name__ == "__main__":
    unittest.main()
