#!/usr/bin/python

import unittest
from closure import *
from graphs import Graph
from edges import Edge

# 0 --> 1 --> 2 --> 3

class TestTransitiveClosure(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = [0, 1, 2, 3]
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        self.expected_T = {
        0: {0: True, 1: True, 2: True, 3: True}, 
        1: {0: False, 1: True, 2: True, 3: True}, 
        2: {0: False, 1: False, 2: True, 3: True}, 
        3: {0: False, 1: False, 2: False, 3: True}}

    def test_closure(self):
        algorithm = TransitiveClosure(self.G)
        algorithm.run()
        self.assertEqual(algorithm.T, self.expected_T)

    def test_closure_simple(self):
        algorithm = TransitiveClosureSimple(self.G)
        algorithm.run()
        self.assertEqual(algorithm.T, self.expected_T)

    def test_closure_bfs(self):
        algorithm = TransitiveClosureBFS(self.G)
        algorithm.run()
        self.assertEqual(algorithm.T, self.expected_T)

    def test_closure_dfs(self):
        algorithm = TransitiveClosureDFS(self.G)
        algorithm.run()
        self.assertEqual(algorithm.T, self.expected_T)


if __name__ == "__main__":

    unittest.main()