#!/usr/bin/python

import unittest
from dagshortestpath import *
from graphs import Graph
from edges import Edge


class TestDAGShortestPath(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["R", "S", "T", "X", "Y", "Z"]
        for node in self.nodes:
            self.G.add_node(node)
        self.G.add_edge(Edge("R", "S", 5))
        self.G.add_edge(Edge("R", "T", 3))
        self.G.add_edge(Edge("S", "X", 6))
        self.G.add_edge(Edge("S", "T", 2))
        self.G.add_edge(Edge("T", "Y", 4))
        self.G.add_edge(Edge("T", "X", 7))
        self.G.add_edge(Edge("T", "Z", 2))
        self.G.add_edge(Edge("X", "Y", -1))
        self.G.add_edge(Edge("X", "Z", 1))
        self.G.add_edge(Edge("Y", "Z", -2))

    def test_shortest_path(self):
        source = "R"
        target = "Z"
        algorithm = DAGShortestPath(self.G)
        algorithm.run(source)
        dist_expected = dict(R=0, S=5, T=3, X=10, Y=7, Z=5)
        self.assertEqual(algorithm.dist, dist_expected)
        prev_expected = {'S': 'R', 'R': None, 'T': 'R', 
        'Y': 'T', 'X': 'T', 'Z': 'T'}
        self.assertEqual(algorithm.prev, prev_expected)
        path_expected = ['R', 'T', 'Z']
        self.assertEqual(algorithm.path(target), path_expected)


if __name__ == "__main__":

    unittest.main()

# EOF
