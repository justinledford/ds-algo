"""
Boyer-Moore substring search, returns the index of the substring t
in s, or -1 if substring is not found.

This is a very basic version of the Boyer-Moore string
search, using only the bad character heuristic.
"""

import unittest


def boyer_moore_find(s, t):
    n = len(s)
    m = len(t)

    # Get rightmost indices of each character in string
    indices = {c:i for i,c in enumerate(t)}

    i = m-1
    while i < n:
        j = m-1
        while j >= 0 and i < n:
            if s[i] == t[j]:
                if j == 0:
                    return i
                i -= 1
                j -= 1
            else:
                if s[i] in indices:
                    i += indices[s[i]]
                else:
                    i += j+1
                j = m-1

    return -1


class TestFind(unittest.TestCase):
    def test_find(self):
        self.assertEqual(0, boyer_moore_find("foobar", "foo"))
        self.assertEqual(1, boyer_moore_find("abcd", "bcd"))
        self.assertEqual(3, boyer_moore_find("foobar", "bar"))
        self.assertEqual(-1, boyer_moore_find("quux", "bar"))
        self.assertEqual(4, boyer_moore_find("abcdefghijklmn", "efg"))


if __name__ == '__main__':
    unittest.main()
