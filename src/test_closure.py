#!/usr/bin/python

import unittest
from closure import *
from graphs import Graph
from edges import Edge

# A --> B --> C --> D

class TestTransitiveClosure(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["A", "B", "C", "D"]
        self.edges = [Edge("A", "B"), Edge("B", "C"), Edge("C", "D")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        self.expected_T = {
        'A': {'A': True, 'B': True, 'C': True, 'D': True}, 
        'B': {'A': False, 'B': True, 'C': True, 'D': True}, 
        'C': {'A': False, 'B': False, 'C': True, 'D': True}, 
        'D': {'A': False, 'B': False, 'C': False, 'D': True}}

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
