#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treelongestpath import TreeLongestPath

# 0---1---2---3   the longest path [3, 2, 1, 4, 5]
#     |
#     4---5

class TestTreeLongestPath(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(1, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_longest_path(self):
        self.assertEqual(self.G.v()-1, self.G.e())
        algorithm = TreeLongestPath(self.G)
        algorithm.run()
        self.assertEqual(len(algorithm.longest_path), 5)

    def test_longest_path2(self):
        self.G.add_edge(Edge(0, 6))
        self.G.add_edge(Edge(6, 7))
        algorithm = TreeLongestPath(self.G)
        algorithm.run()
        self.assertEqual(len(algorithm.longest_path), 6)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
