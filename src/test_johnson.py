#! /usr/bin/python

import unittest
from johnson import Johnson
from graphs import Graph
from edges import Edge


class TestJohnson(unittest.TestCase):

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

    def test_johnson(self):
        algorithm = Johnson(self.G)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 4, 'B': 4, 'E': float("inf"), 'D': 3},
        B={'A': 3, 'C': 7, 'B': 0, 'E': float("inf"), 'D': 6},
        C={'A': 6, 'C': 0, 'B': 3, 'E': float("inf"), 'D': 2},
        D={'A': 4, 'C': 1, 'B': 1, 'E': float("inf"), 'D': 0},
        E={'A': 6, 'C': 3, 'B': 3, 'E': 0, 'D': 2})
        self.assertEqual(algorithm.dist, expected_dist)

    def test_negative_cycle(self):
        self.G.add_edge(Edge("B", "D", -2))
        algorithm = Johnson(self.G)
        self.assertRaises(ValueError, algorithm.run)

class TestJohnsonNegativeEdges(unittest.TestCase):

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

    def test_johnson(self):
        algorithm = Johnson(self.G)
        algorithm.run()
        expected_dist = dict(
        A={'A': 0, 'C': 6, 'B': 3, 'D': 8}, 
        B={'A': 0, 'C': 4, 'B': 0, 'D': 5}, 
        C={'A': -3, 'C': 0, 'B': -1, 'D': 2},
        D={'A': -5, 'C': 1, 'B': -3, 'D': 0})
        self.assertEqual(algorithm.dist, expected_dist)

    def test_negative_cycle(self):
        self.G.add_edge(Edge("A", "D", 2))
        algorithm = Johnson(self.G)
        self.assertRaises(ValueError, algorithm.run)

class TestJohnsonWiki(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["x", "y", "z", "w"]
        self.edges = [Edge("x", "y", 3), Edge("x", "w", 6),
        Edge("y", "w", 4), Edge("y", "z", 5), Edge("w", "z", 2),
        Edge("z", "x", -7), Edge("z", "y", -3)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_johnson(self):
        algorithm = Johnson(self.G)
        algorithm.run()
        expected_dist = {
        'y': {'y': 0, 'x': -2, 'z': 5, 'w': 4}, 
        'x': {'y': 3, 'x': 0, 'z': 8, 'w': 6}, 
        'z': {'y': -4, 'x': -7, 'z': 0, 'w': -1}, 
        'w': {'y': -2, 'x': -5, 'z': 2, 'w': 0}}
        self.assertEqual(algorithm.dist, expected_dist)

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestJohnson)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestJohnsonNegativeEdges)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestJohnsonWiki)
    suite = unittest.TestSuite([suite1, suite2, suite3])
    unittest.TextTestRunner(verbosity=2).run(suite)
