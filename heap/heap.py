"""
Min heap
"""

import unittest

class Heap:
    def __init__(self):
        self.h = []
        self.n = -1


    def _parent(self, n):
        return n//2 if n > 0 else -1


    def _child(self, n):
        return 2*n


    def insert(self, x):
        self.n += 1
        self.h.append(x)
        self._bubble_up(self.n)


    def _bubble_up(self, n):
        p = self._parent(n)

        # at root, no more bubbling necessary
        if p == -1:
            return

        if self.h[p] > self.h[n]:
            self.h[p], self.h[n] = self.h[n], self.h[p]
            self._bubble_up(p)


    def make_heap(self, A):
        for x in A:
            self.insert(x)


    def fast_make_heap(self, A):
        """
        A faster make heap function exploiting the fact that
        all leafs already dominate their non-existent children,
        so we can insert all elements directly into the heap's
        array and then bubble down on only the first n/2 elements.
        """

        self.h = A
        self.n = len(A)-1

        for i in range(len(A)//2, -1, -1):
            self._bubble_down(i)


    def extract(self):
        if self.n < 0:
            raise Exception("Heap is empty")

        x = self.h[0]

        # swap and delete last element
        self.h[0] = self.h[self.n]
        del self.h[self.n]
        self.n -= 1

        self._bubble_down(0)
        return x


    def _bubble_down(self, p):
        c = self._child(p)

        # check that parent dominates both children
        for i in [0, 1]:
            if (c + i) <= self.n and self.h[p] > self.h[c+i]:
                self.h[p], self.h[c+i] = self.h[c+i], self.h[p]
                self._bubble_down(c+i)


class TestHeap(unittest.TestCase):
    def test_insert(self):
        heap = Heap()
        self.assertEqual([], heap.h)
        heap.insert(1)
        self.assertEqual([1], heap.h)
        heap.insert(3)
        self.assertEqual([1, 3], heap.h)
        heap.insert(4)
        self.assertEqual([1, 3, 4], heap.h)
        heap.insert(2)
        self.assertEqual([1, 2, 4, 3], heap.h)
        heap.insert(5)
        self.assertEqual([1, 2, 4, 3, 5], heap.h)


    def test_make_heap(self):
        heap = Heap()
        heap.make_heap([3, 4, 1])
        self.assertEqual([1, 3, 4], heap.h)


    def test_fast_make_heap(self):
        heap = Heap()
        heap.fast_make_heap([3, 4, 1])
        self.assertEqual([1, 3, 4], heap.h)


    def test_extract(self):
        heap = Heap()
        heap.insert(1)
        self.assertEqual(1, heap.extract())
        heap.make_heap([3, 4, 1])
        self.assertEqual(1, heap.extract())
        self.assertEqual(3, heap.extract())
        self.assertEqual(4, heap.extract())

        # heapsort test
        xs = [42, 5, 17, 38, 7, 11, 27, 12, 3, 99, 2, 1]
        heap.make_heap(xs)
        s = []
        for x in xs:
            s.append(heap.extract())

        self.assertEqual(s, sorted(xs))


if __name__ == '__main__':
    unittest.main()
