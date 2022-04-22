#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.connectivity.connected import ConnectedComponentsBFS
from graphtheory.connectivity.connected import ConnectedComponentsDFS
from graphtheory.connectivity.connected import is_connected
from graphtheory.connectivity.connected import StronglyConnectedComponents

# 0 - 1   2 - 3
# |   |   | / |
# 4   5   6 - 7

class TestConnectedComponents(unittest.TestCase):

    def setUp(self):
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 4), Edge(0, 1), Edge(1, 5), Edge(2, 6), Edge(2, 3),
            Edge(6, 3), Edge(6, 7), Edge(3, 7)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        self.expected_cc = {1: 0, 0: 0, 5: 0, 4: 0, 3: 1, 2: 1, 7: 1, 6: 1}
        self.expected_n_cc = 2

    def test_cc_bfs(self):
        algorithm = ConnectedComponentsBFS(self.G)
        algorithm.run()
        self.assertEqual(algorithm.n_cc, self.expected_n_cc)
        self.assertEqual(algorithm.cc, self.expected_cc)
        self.assertRaises(ValueError, ConnectedComponentsBFS, Graph(1, True))

    def test_cc_dfs(self):
        algorithm = ConnectedComponentsDFS(self.G)
        algorithm.run()
        self.assertEqual(algorithm.n_cc, self.expected_n_cc)
        self.assertEqual(algorithm.cc, self.expected_cc)
        self.assertRaises(ValueError, ConnectedComponentsDFS, Graph(1, True))

    def test_is_connected(self):
        self.assertFalse(is_connected(self.G))
        self.G.add_edge(Edge(5, 6))
        self.assertTrue(is_connected(self.G))
        self.assertRaises(ValueError, is_connected, Graph(1, True))

    def tearDown(self): pass

# 0 -o 1 --o 2 o-o 3   Cormen, s.628 modified
# o  / |     |     |
# | o  o     o     o
# 4 -o 5 o-o 6 --o 7

class TestStronglyConnectedComponents(unittest.TestCase):

    def setUp(self):
        self.N = 8           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(1, 4), Edge(4, 0), Edge(4, 5), Edge(1, 5), 
            Edge(1, 2), Edge(5, 6), Edge(6, 5), Edge(2, 6), Edge(2, 3), 
            Edge(3, 2), Edge(6, 7), Edge(3, 7)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        self.expected_scc = {0: 0, 1: 0, 2: 1, 3: 1, 4: 0, 5: 2, 6: 2, 7: 3}
        self.expected_n_scc = 4

    def test_scc(self):
        algorithm = StronglyConnectedComponents(self.G)
        algorithm.run()
        self.assertEqual(algorithm.n_scc, self.expected_n_scc)
        self.assertEqual(algorithm.scc, self.expected_scc)
        self.assertRaises(
            ValueError, StronglyConnectedComponents, Graph(1, False))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
