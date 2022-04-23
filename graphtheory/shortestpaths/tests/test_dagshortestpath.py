#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.shortestpaths.dagshortestpath import *


class TestDAGShortestPath(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        for node in self.nodes:
            self.G.add_node(node)
        self.G.add_edge(Edge(0, 1, 5))
        self.G.add_edge(Edge(0, 2, 3))
        self.G.add_edge(Edge(1, 3, 6))
        self.G.add_edge(Edge(1, 2, 2))
        self.G.add_edge(Edge(2, 4, 4))
        self.G.add_edge(Edge(2, 3, 7))
        self.G.add_edge(Edge(2, 5, 2))
        self.G.add_edge(Edge(3, 4, -1))
        self.G.add_edge(Edge(3, 5, 1))
        self.G.add_edge(Edge(4, 5, -2))

    def test_shortest_path(self):
        source = 0
        target = 5
        algorithm = DAGShortestPath(self.G)
        algorithm.run(source)
        distance_expected = {0: 0, 1: 5, 2: 3, 3: 10, 4: 7, 5: 5}
        self.assertEqual(algorithm.distance, distance_expected)
        parent_expected = {1: 0, 0: None, 2: 0, 4: 2, 3: 2, 5: 2}
        self.assertEqual(algorithm.parent, parent_expected)
        path_expected = [0, 2, 5]
        self.assertEqual(algorithm.path(target), path_expected)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
