#!/usr/bin/python
#
# test_topsort.py
#
# Topological sorting test.

from edges import Edge
from graphs import Graph
from topsort import TopologicalSort
#from topsort2 import TopologicalSort
import unittest


class TestTopologicalSorting(unittest.TestCase):

    def setUp(self):
        #  Knuth s.273 t.1
        self.N = 10           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.edges = [Edge(9, 2), Edge(3, 7), Edge(7, 5), Edge(5, 8),
        Edge(8, 6), Edge(4, 6), Edge(1, 3), Edge(7, 4), Edge(9, 5), Edge(2, 8)]
        self.G.add_node(0)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_topsort(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = TopologicalSort(self.G)
        algorithm.run()
        idx = dict((node, i) for (i, node) in enumerate(algorithm.sorted_nodes))
        for edge in self.edges:
            self.assertTrue(idx[edge.source] < idx[edge.target])

    def tearDown(self): pass


if __name__ == "__main__":

    unittest.main()

# EOF
