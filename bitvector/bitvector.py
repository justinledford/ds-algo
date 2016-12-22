"""
Bit-vector: represents a set of integers using bits. An integer n
exists in the set if the nth bit is set.
"""
import unittest

class BitVector:
    def __init__(self):
        self.vector = 0

    def add(self, x):
        self.vector |= (1 << x)

    def remove(self, x):
        self.vector &= ~(1 << x)

    def contains(self, x):
        return (self.vector & (1 << x)) != 0



class TestBitVector(unittest.TestCase):
    def setUp(self):
        self.b = BitVector()
        self.b.add(1)
        self.b.add(2)
        self.b.add(10)
        self.b.add(17)
        self.b.add(38)

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

    def test_remove(self):
        self.b.remove(1)
        self.assertFalse(self.b.contains(1))
        self.b.remove(10)
        self.assertFalse(self.b.contains(10))



if __name__ == '__main__':
    unittest.main()
