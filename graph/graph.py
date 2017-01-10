from collections import defaultdict, namedtuple
import unittest

class Graph:
    EdgeNode = namedtuple('EdgeNode', ['x', 'y', 'weight'])

    def __init__(self, directed=False):
        self.edges = defaultdict(list)

    def insert_edge(self, x, y, weight):
        self.edges[x].append(self.EdgeNode._make([x, y, weight]))


class TestGraph(unittest.TestCase):
    def test_insert(self):
        g = Graph()
        g.insert_edge(2, 4, 1)
        self.assertEqual(g.edges[2][0].x, 2)
        self.assertEqual(g.edges[2][0].y, 4)
        self.assertEqual(g.edges[2][0].weight, 1)

if __name__ == '__main__':
    unittest.main()
