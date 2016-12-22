"""
Bit-vector: represents a set of integers using bits. An integer n
exists in the set if the nth bit is set.
"""
import unittest

from math import log2, ceil

class BitVector:
    def __init__(self, bits=0):
        self.bits = bits

    def add(self, x):
        self.bits |= (1 << x)

    def remove(self, x):
        self.bits &= ~(1 << x)

    def contains(self, x):
        return (self.bits & (1 << x)) != 0

    def size(self):
        """
        Return size in bits (number of bits required to represent the
        largest number in the set, not the actual size in memory)
        """
        return ceil(log2(self.bits))

    def members(self):
        """
        Return a list of the members in the set
        """
        members = []

        for i in range(0, self.size()+1):
            if self.contains(i):
                members.append(i)

        return members

    def union(self, b):
        return BitVector(self.bits | b.bits)

    def intersection(self, b):
        return BitVector(self.bits & b.bits)

    def difference(self, b):
        return BitVector(self.bits & ~b.bits)


class TestBitVector(unittest.TestCase):
    def setUp(self):
        self.b = BitVector()
        self.b.add(1)
        self.b.add(2)
        self.b.add(10)
        self.b.add(17)
        self.b.add(38)
        self.a = BitVector()
        self.a.add(3)
        self.a.add(11)
        self.a.add(17)
        self.a.add(38)

    def test_contains(self):
        self.assertTrue(self.b.contains(1))
        self.assertTrue(self.b.contains(2))
        self.assertTrue(self.b.contains(10))
        self.assertTrue(self.b.contains(17))
        self.assertTrue(self.b.contains(38))
        self.assertFalse(self.b.contains(3))
        self.assertFalse(self.b.contains(9))
        self.assertFalse(self.b.contains(11))
        self.assertFalse(self.b.contains(10000))

    def test_union(self):
        c = self.a.union(self.b)
        self.assertTrue(c.contains(1))
        self.assertTrue(c.contains(3))

    def test_intersection(self):
        c = self.a.intersection(self.b)
        self.assertTrue(c.contains(17))
        self.assertTrue(c.contains(38))
        self.assertFalse(c.contains(1))
        self.assertFalse(c.contains(3))

    def test_difference(self):
        c = self.a.difference(self.b)
        self.assertTrue(c.contains(3))
        self.assertTrue(c.contains(11))
        self.assertFalse(c.contains(17))
        self.assertFalse(c.contains(38))

    def test_members(self):
        self.assertEqual([1,2,10,17,38], self.b.members())
        self.assertNotEqual([1,2,10,17], self.b.members())

    def test_remove(self):
        self.b.remove(1)
        self.assertFalse(self.b.contains(1))
        self.b.remove(10)
        self.assertFalse(self.b.contains(10))


if __name__ == '__main__':
    unittest.main()
