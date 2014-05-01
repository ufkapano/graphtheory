#!/usr/bin/python
#
# test_kruskal.py
#
# Kruskal's algorithm test.

from edges import Edge
from graphs import Graph
from kruskal import KruskalMST
import unittest


class TestKruskal(unittest.TestCase):

    def setUp(self):
        self.N = 7           # number of nodes
        self.G = Graph(self.N)
        self.edges = [Edge("A", "B", 7), Edge("B", "C", 11), Edge("A", "D", 4),
        Edge("D", "B", 9), Edge("E", "B", 10), Edge("C", "E", 5), Edge("D", "E", 15),
        Edge("D", "F", 6), Edge("F", "E", 12), Edge("F", "G", 13), Edge("E", "G", 8)]
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_mst(self):
        self.assertEqual(self.G.v(), self.N)
        kruskal = KruskalMST(self.G)
        kruskal.run()
        self.assertEqual(kruskal.mst.v(), self.N)
        self.assertEqual(kruskal.mst.e(), self.N-1)
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in kruskal.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [Edge('A', 'B', 7), Edge('A', 'D', 4), 
        Edge('C', 'E', 5), Edge('B', 'E', 10), Edge('E', 'G', 8), Edge('D', 'F', 6)]
        for edge in mst_edges_expected:
            self.assertTrue(kruskal.mst.has_edge(edge))

    def tearDown(self): pass


if __name__ == "__main__":

    unittest.main()

# EOF
