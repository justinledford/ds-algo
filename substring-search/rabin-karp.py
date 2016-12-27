"""
Rabin-Karp substring search, returns the index of the substring t
in s, or -1 if substring is not found.

Uses a rolling hash to compare strings, with time complexity
of O(n+m), compared to the naive substring search's O(nm).
"""

import unittest

def hash(s, b):
    return sum([b**(len(s)-i-1) * ord(c) for i, c in enumerate(s)])

def rabin_karp_find(s, t):
    m = len(t)
    n = len(s)
    b = 101

    ht = hash(t, b)
    hs = hash(s[0:m], b)

    if hs == ht and s[0:m] == t:
        return 0

    for i in range(1, n-m+1):
        # rehash
        hs = b*(hs - b**(m-1)*ord(s[i-1])) + ord(s[i+m-1])
        if hs == ht and s[i:i+m] == t:
            return i

    return -1


class TestFind(unittest.TestCase):
    def test_find(self):
        self.assertEqual(0, rabin_karp_find("foobar", "foo"))
        self.assertEqual(1, rabin_karp_find("abcd", "bcd"))
        self.assertEqual(3, rabin_karp_find("foobar", "bar"))
        self.assertEqual(-1, rabin_karp_find("quux", "bar"))


if __name__ == '__main__':
    unittest.main()
