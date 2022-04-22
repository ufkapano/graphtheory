#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.connectivity.cutnodes import TrivialCutNode
from graphtheory.connectivity.cutnodes import TarjanCutNode
from graphtheory.connectivity.cutnodes import is_biconnected

# 0---1   2---3
# | / | / | \ |
# 4   5---6   7

class TestCutNode(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607 changed.
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 4, 2), Edge(0, 1, 3), Edge(1, 4, 12), Edge(1, 5, 4), 
            Edge(5, 2, 5), Edge(5, 6, 6), Edge(2, 6, 7), Edge(2, 3, 8), 
            Edge(2, 7, 9), Edge(3, 7, 11)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_trivial_cut_node(self):
        algorithm = TrivialCutNode(self.G)
        algorithm.run(0)
        cut_nodes_expected = [1, 2, 5]
        self.assertEqual(algorithm.cut_nodes, cut_nodes_expected)

    def test_tarjan_cut_node(self):
        algorithm = TarjanCutNode(self.G)
        algorithm.run(0)
        cut_nodes_expected = [2, 5, 1]
        self.assertEqual(algorithm.cut_nodes, cut_nodes_expected)
        dd_expected = {0: 1, 1: 2, 2: 5, 3: 6, 4: 3, 5: 4, 6: 8, 7: 7}
        #self.assertEqual(algorithm._dd, dd_expected) # problems in Py3
        parent_expected = {0: None, 1: 0, 2: 5, 3: 2, 4: 1, 5: 1, 6: 2, 7: 3}
        #self.assertEqual(algorithm.parent, parent_expected) # problems in Py3

    def test_is_biconnected(self):
        self.assertFalse(is_biconnected(self.G))
        self.G.add_edge(Edge(4, 5))
        self.assertFalse(is_biconnected(self.G))
        self.G.add_edge(Edge(1, 2))
        self.assertFalse(is_biconnected(self.G))
        self.G.add_edge(Edge(6, 7))
        self.assertTrue(is_biconnected(self.G))

    def test_exceptions(self):
        self.assertRaises(ValueError, TrivialCutNode, Graph(1, True))
        self.assertRaises(ValueError, TarjanCutNode, Graph(1, True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
