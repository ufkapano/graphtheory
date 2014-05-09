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
        # The graph (unique weights) from
        # http://en.wikipedia.org/wiki/Boruvka's_algorithm
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


class TestKruskalCormen(unittest.TestCase):

    def setUp(self):
        # The modified graph (unique weights) from Cormen.
        self.N = 9           # number of nodes
        self.G = Graph(self.N)
        self.nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        self.edges = [Edge("A", "B", 4), Edge("A", "H", 8),
        Edge("B", "H", 11), Edge("B", "C", 12), Edge("H", "I", 7),
        Edge("I", "C", 2), Edge("I", "G", 6), Edge("H", "G", 1),
        Edge("C", "D", 13), Edge("C", "F", 5), Edge("G", "F", 3),
        Edge("D", "F", 14), Edge("D", "E", 9), Edge("F", "E", 10)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G

    def test_mst_cormen(self):
        self.assertEqual(self.G.v(), self.N)
        kruskal = KruskalMST(self.G)
        kruskal.run()
        self.assertEqual(kruskal.mst.v(), self.N)
        self.assertEqual(kruskal.mst.e(), self.N-1)
        mst_weight_expected = 42
        mst_weight = sum(edge.weight for edge in kruskal.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [Edge("A", "B", 4), Edge("A", "H", 8),
        Edge("I", "C", 2), Edge("H", "G", 1), Edge("C", "F", 5),
        Edge("G", "F", 3), Edge("D", "E", 9), Edge("F", "E", 10)]
        for edge in mst_edges_expected:
            self.assertTrue(kruskal.mst.has_edge(edge))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
