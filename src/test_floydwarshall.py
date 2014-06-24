#!/usr/bin/python

import unittest
from floydwarshall import FloydWarshall, FloydWarshallPaths
from graphs import Graph
from edges import Edge


class TestFloydWarshall(unittest.TestCase):

    def setUp(self):
        self.N = 5           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["A", "B", "C", "D", "E"]
        self.edges = [Edge("A", "C", 6), Edge("A", "D", 3),
        Edge("B", "A", 3), Edge("C", "D", 2), Edge("D", "B", 1),
        Edge("D", "C", 1), Edge("E", "B", 4), Edge("E", "D", 2)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_floydwarshall(self):
        algorithm = FloydWarshall(self.G)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 4, 'B': 4, 'E': float("inf"), 'D': 3},
        B={'A': 3, 'C': 7, 'B': 0, 'E': float("inf"), 'D': 6},
        C={'A': 6, 'C': 0, 'B': 3, 'E': float("inf"), 'D': 2},
        D={'A': 4, 'C': 1, 'B': 1, 'E': float("inf"), 'D': 0},
        E={'A': 6, 'C': 3, 'B': 3, 'E': 0, 'D': 2})
        self.assertEqual(algorithm.dist, expected_dist)

    def test_floydwarshall_paths(self):
        algorithm = FloydWarshallPaths(self.G)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 4, 'B': 4, 'E': float("inf"), 'D': 3},
        B={'A': 3, 'C': 7, 'B': 0, 'E': float("inf"), 'D': 6},
        C={'A': 6, 'C': 0, 'B': 3, 'E': float("inf"), 'D': 2},
        D={'A': 4, 'C': 1, 'B': 1, 'E': float("inf"), 'D': 0},
        E={'A': 6, 'C': 3, 'B': 3, 'E': 0, 'D': 2})
        expected_prev = {
        'A': {'A': None, 'C': 'D', 'B': 'D', 'E': None, 'D': 'A'}, 
        'B': {'A': 'B', 'C': 'D', 'B': None, 'E': None, 'D': 'A'}, 
        'C': {'A': 'B', 'C': None, 'B': 'D', 'E': None, 'D': 'C'}, 
        'D': {'A': 'B', 'C': 'D', 'B': 'D', 'E': None, 'D': None}, 
        'E': {'A': 'B', 'C': 'D', 'B': 'D', 'E': None, 'D': 'E'}}
        self.assertEqual(algorithm.dist, expected_dist)
        self.assertEqual(algorithm.prev, expected_prev)

    def test_floydwarshall_negative_cycle(self):
        self.G.add_edge(Edge("B", "D", -2))
        algorithm = FloydWarshall(self.G)
        self.assertRaises(ValueError, algorithm.run)


class TestFloydWarshallNegativeEdges(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["A", "B", "C", "D"]
        self.edges = [Edge("A", "B", 3), Edge("A", "C", 6),
        Edge("B", "C", 4), Edge("B", "D", 5), Edge("C", "D", 2),
        Edge("D", "A", -5), Edge("D", "B", -3)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_negative_edges(self):
        algorithm = FloydWarshall(self.G)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 6, 'B': 3, 'D': 8}, 
        B={'A': 0, 'C': 4, 'B': 0, 'D': 5}, 
        C={'A': -3, 'C': 0, 'B': -1, 'D': 2},
        D={'A': -5, 'C': 1, 'B': -3, 'D': 0})
        self.assertEqual(algorithm.dist, expected_dist)

    def test_negative_edges_with_paths(self):
        algorithm = FloydWarshallPaths(self.G)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 6, 'B': 3, 'D': 8}, 
        B={'A': 0, 'C': 4, 'B': 0, 'D': 5}, 
        C={'A': -3, 'C': 0, 'B': -1, 'D': 2},
        D={'A': -5, 'C': 1, 'B': -3, 'D': 0})
        expected_prev = {
        'A': {'A': None, 'C': 'A', 'B': 'A', 'D': 'C'}, 
        'B': {'A': 'D', 'C': 'B', 'B': None, 'D': 'B'}, 
        'C': {'A': 'D', 'C': None, 'B': 'D', 'D': 'C'}, 
        'D': {'A': 'D', 'C': 'A', 'B': 'D', 'D': None}}
        self.assertEqual(algorithm.dist, expected_dist)
        self.assertEqual(algorithm.prev, expected_prev)

    def test_negative_cycle(self):
        self.G.add_edge(Edge("A", "D", 2))
        algorithm = FloydWarshall(self.G)
        self.assertRaises(ValueError, algorithm.run)


if __name__ == "__main__":

    unittest.main()
