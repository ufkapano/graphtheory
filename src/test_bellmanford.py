#!/usr/bin/python
#
# test_bellmanford.py
#
# Tests for Bellman-Ford algorithm.

from edges import Edge
from graphs import Graph
from bellmanford import BellmanFord
import unittest

#    1
# A --> B
# |   / |
# |5 /1 |3
# |./.  |.
# C --> D
#    1

class TestBellmanFord(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True) # directed graph
        self.nodes = ["A", "B", "C", "D"]
        self.edges = [Edge("A", "B", 1), Edge("A", "C", 5), 
        Edge("B", "C", 1), Edge("B", "D", 3), Edge("C", "D", 1)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_shortest_path(self):
        source = "A"
        target = "D"
        algorithm = BellmanFord(self.G)
        algorithm.run(source)
        dist_expected = {'A': 0, 'C': 2, 'B': 1, 'D': 3}
        self.assertEqual(algorithm.dist, dist_expected)
        prev_expected = {'A': None, 'C': 'B', 'B': 'A', 'D': 'C'}
        self.assertEqual(algorithm.prev, prev_expected)
        path_expected = ['A', 'B', 'C', 'D']
        self.assertEqual(algorithm.path_to(target), path_expected)

    def tearDown(self): pass


class TestBellmanFordCormen(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.666, negative weights.
        self.N = 5           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["s", "t", "x", "y", "z"]
        self.edges = [Edge("s", "t", 6), Edge("s", "y", 7),
        Edge("t", "y", 8), Edge("t", "x", 5), Edge("t", "z", -4),
        Edge("x", "t", -2), Edge("y", "x", -3), Edge("y", "z", 9),
        Edge("z", "s", 2), Edge("z", "x", 7)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_shortest_path_cormen(self):
        source = "s"
        target = "z"
        algorithm = BellmanFord(self.G)
        algorithm.run(source)
        dist_expected = {'y': 7, 'x': 4, 's': 0, 'z': -2, 't': 2}
        self.assertEqual(algorithm.dist, dist_expected)
        prev_expected = {'y': 's', 'x': 'y', 's': None, 'z': 't', 't': 'x'}
        self.assertEqual(algorithm.prev, prev_expected)
        path_expected = ['s', 'y', 'x', 't', 'z']
        self.assertEqual(algorithm.path_to(target), path_expected)


    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
