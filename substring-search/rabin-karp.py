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

    for i in range(0, n-m+1):
        if hs == ht and s[i:i+m] == t:
            return i
        if i < n-m:
            hs = b*(hs - b**(m-1)*ord(s[i])) + ord(s[i+m])

    return -1


class TestFind(unittest.TestCase):
    def test_find(self):
        self.assertEqual(0, rabin_karp_find("foobar", "foo"))
        self.assertEqual(1, rabin_karp_find("abcd", "bcd"))
        self.assertEqual(3, rabin_karp_find("foobar", "bar"))
        self.assertEqual(-1, rabin_karp_find("quux", "bar"))


if __name__ == '__main__':
    unittest.main()
