"""
Naive substring search, returns the index of the substring t
in s, or -1 if substring is not found.
"""

import unittest

def find(s, t):
    m = len(t)
    n = len(s)

    for i in range(0, n-m+1):
        if s[i:i+m] == t:
            return i
    return -1



class TestFind(unittest.TestCase):
    def test_find(self):
        self.assertEqual(0, find("foobar", "foo"))
        self.assertEqual(3, find("foobar", "bar"))
        self.assertEqual(-1, find("quux", "bar"))


if __name__ == '__main__':
    unittest.main()
