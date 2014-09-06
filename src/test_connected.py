#!/usr/bin/python

import unittest
from connected import *
from graphs import Graph
from edges import Edge

# 0 - 1   2 - 3
# |   |   | / |
# 4   5   6 - 7

class TestConnectedComponents(unittest.TestCase):

    def setUp(self):
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = [0, 1, 2, 3, 4, 5, 6, 7]
        self.edges = [Edge(0, 4), Edge(0, 1),
        Edge(1, 5), Edge(2, 6), Edge(2, 3),
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

    def test_cc_dfs(self):
        algorithm = ConnectedComponentsDFS(self.G)
        algorithm.run()
        self.assertEqual(algorithm.n_cc, self.expected_n_cc)
        self.assertEqual(algorithm.cc, self.expected_cc)

if __name__ == "__main__":

    unittest.main()
