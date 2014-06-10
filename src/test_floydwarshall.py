#! /usr/bin/python

import unittest
from floydwarshall import FloydWarshall, FloydWarshallPaths
from graphs import Graph
from edges import Edge


class TestFloydWarshall(unittest.TestCase):

    def test_floydwarshall_list(self):
        graph = Graph(directed=True)
        graph.add_edge(Edge("A", "C", 6))
        graph.add_edge(Edge("A", "D", 3))
        graph.add_edge(Edge("B", "A", 3))
        graph.add_edge(Edge("C", "D", 2))
        graph.add_edge(Edge("D", "B", 1))
        graph.add_edge(Edge("D", "C", 1))
        graph.add_edge(Edge("E", "B", 4))
        graph.add_edge(Edge("E", "D", 2))
        algorithm = FloydWarshall(graph)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 4, 'B': 4, 'E': float("inf"), 'D': 3},
        B={'A': 3, 'C': 7, 'B': 0, 'E': float("inf"), 'D': 6},
        C={'A': 6, 'C': 0, 'B': 3, 'E': float("inf"), 'D': 2},
        D={'A': 4, 'C': 1, 'B': 1, 'E': float("inf"), 'D': 0},
        E={'A': 6, 'C': 3, 'B': 3, 'E': 0, 'D': 2})
        self.assertEqual(algorithm.dist, expected_dist)

    def test_with_negative_edges(self):
        graph = Graph(directed=True)
        graph.add_edge(Edge("A", "B", 3))
        graph.add_edge(Edge("A", "C", 6))
        graph.add_edge(Edge("B", "C", 4))
        graph.add_edge(Edge("B", "D", 5))
        graph.add_edge(Edge("C", "D", 2))
        graph.add_edge(Edge("D", "A", -5))
        graph.add_edge(Edge("D", "B", -3))
        algorithm = FloydWarshall(graph)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 6, 'B': 3, 'D': 8}, 
        B={'A': 0, 'C': 4, 'B': 0, 'D': 5}, 
        C={'A': -3, 'C': 0, 'B': -1, 'D': 2},
        D={'A': -5, 'C': 1, 'B': -3, 'D': 0})
        self.assertEqual(algorithm.dist, expected_dist)


class TestFloydWarshallPaths(unittest.TestCase):

    def test_floydwarshall_list(self):
        graph = Graph(directed=True)
        graph.add_edge(Edge("A", "C", 6))
        graph.add_edge(Edge("A", "D", 3))
        graph.add_edge(Edge("B", "A", 3))
        graph.add_edge(Edge("C", "D", 2))
        graph.add_edge(Edge("D", "B", 1))
        graph.add_edge(Edge("D", "C", 1))
        graph.add_edge(Edge("E", "B", 4))
        graph.add_edge(Edge("E", "D", 2))
        algorithm = FloydWarshallPaths(graph)
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

    def test_with_negative_edges(self):
        graph = Graph(directed=True)
        graph.add_edge(Edge("A", "B", 3))
        graph.add_edge(Edge("A", "C", 6))
        graph.add_edge(Edge("B", "C", 4))
        graph.add_edge(Edge("B", "D", 5))
        graph.add_edge(Edge("C", "D", 2))
        graph.add_edge(Edge("D", "A", -5))
        graph.add_edge(Edge("D", "B", -3))
        algorithm = FloydWarshallPaths(graph)
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


if __name__ == "__main__":

    unittest.main()
