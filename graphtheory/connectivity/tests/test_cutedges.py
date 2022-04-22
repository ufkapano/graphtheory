#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.connectivity.cutedges import TrivialCutEdge
from graphtheory.connectivity.cutedges import TarjanCutEdge

# 0---1   2---3
# | / | / | / |
# 4   5---6---7

class TestCutEdge(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607 changed
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 4, 2), Edge(0, 1, 3), Edge(1, 4, 12), Edge(2, 3, 8), 
            Edge(1, 5, 4), Edge(5, 2, 5), Edge(5, 6, 6), Edge(2, 6, 7), 
            Edge(6, 3, 9), Edge(6, 7, 10), Edge(3, 7, 11)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_trivial_cut_edge(self):
        algorithm = TrivialCutEdge(self.G)
        algorithm.run(0)
        cut_edges_expected = [Edge(1, 5, 4)]
        self.assertEqual(algorithm.cut_edges, cut_edges_expected)

    def test_tarjan_cut_edges(self):
        algorithm = TarjanCutEdge(self.G)
        algorithm.run(2)
        dd_expected = {0: 6, 1: 5, 2: 1, 3: 2, 4: 7, 5: 4, 6: 3, 7: 8}
        self.assertEqual(algorithm._dd, dd_expected)
        parent_expected = {0: 1, 1: 5, 2: None, 3: 2, 4: 0, 5: 6, 6: 3, 7: 6}
        self.assertEqual(algorithm.parent, parent_expected)
        cut_edges_expected = [Edge(5, 1, 4)]
        self.assertEqual(algorithm.cut_edges, cut_edges_expected)

    def test_exceptions(self):
        self.assertRaises(ValueError, TrivialCutEdge, Graph(1, True))
        self.assertRaises(ValueError, TarjanCutEdge, Graph(1, True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
