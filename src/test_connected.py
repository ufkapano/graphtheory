#! /usr/bin/python

import unittest
from connected import *
from graphs import Graph
from edges import Edge

# r - s   t - u
# |   |   | / |
# v   w   x - y

class TestConnectedComponents(unittest.TestCase):

    def setUp(self):
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = ["r", "s", "t", "u", "v", "w", "x", "y"]
        self.edges = [Edge("r", "v"), Edge("r", "s"),
        Edge("s", "w"), Edge("t", "x"), Edge("t", "u"),
        Edge("x", "u"), Edge("x", "y"), Edge("u", "y")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        self.expected_cc = {'s': 0, 'r': 0, 'w': 0, 'v': 0, 
        'u': 1, 't': 1, 'y': 1, 'x': 1}
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
