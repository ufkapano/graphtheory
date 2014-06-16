#! /usr/bin/python

import unittest
from allpairs import *
from graphs import Graph
from edges import Edge


class TestAllPairsShortestPaths(unittest.TestCase):

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

    def test_slow(self):
        algorithm = SlowAllPairs(self.G)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 4, 'B': 4, 'E': float("inf"), 'D': 3},
        B={'A': 3, 'C': 7, 'B': 0, 'E': float("inf"), 'D': 6},
        C={'A': 6, 'C': 0, 'B': 3, 'E': float("inf"), 'D': 2},
        D={'A': 4, 'C': 1, 'B': 1, 'E': float("inf"), 'D': 0},
        E={'A': 6, 'C': 3, 'B': 3, 'E': 0, 'D': 2})
        self.assertEqual(algorithm.dist, expected_dist)

    def test_slow(self):
        algorithm = SlowAllPairsEdges(self.G)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 4, 'B': 4, 'E': float("inf"), 'D': 3},
        B={'A': 3, 'C': 7, 'B': 0, 'E': float("inf"), 'D': 6},
        C={'A': 6, 'C': 0, 'B': 3, 'E': float("inf"), 'D': 2},
        D={'A': 4, 'C': 1, 'B': 1, 'E': float("inf"), 'D': 0},
        E={'A': 6, 'C': 3, 'B': 3, 'E': 0, 'D': 2})
        self.assertEqual(algorithm.dist, expected_dist)

    def test_faster(self):
        algorithm = FasterAllPairs(self.G)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 4, 'B': 4, 'E': float("inf"), 'D': 3},
        B={'A': 3, 'C': 7, 'B': 0, 'E': float("inf"), 'D': 6},
        C={'A': 6, 'C': 0, 'B': 3, 'E': float("inf"), 'D': 2},
        D={'A': 4, 'C': 1, 'B': 1, 'E': float("inf"), 'D': 0},
        E={'A': 6, 'C': 3, 'B': 3, 'E': 0, 'D': 2})
        self.assertEqual(algorithm.dist, expected_dist)

    def test_slow_with_paths(self):
        algorithm = SlowAllPairsWithPaths(self.G)
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

    def test_negative_cycle(self):
        self.G.add_edge(Edge("B", "D", -2))
        algorithm = FasterAllPairs(self.G)
        self.assertRaises(ValueError, algorithm.run)
        algorithm = SlowAllPairs(self.G)
        self.assertRaises(ValueError, algorithm.run)
        algorithm = SlowAllPairsEdges(self.G)
        self.assertRaises(ValueError, algorithm.run)
        algorithm = SlowAllPairsWithPaths(self.G)
        self.assertRaises(ValueError, algorithm.run)

if __name__ == "__main__":

    unittest.main()
