#!/usr/bin/python

from edges import Edge
from graphs import Graph
from hamilton import HamiltonCycle
import unittest

# 0 --------- 5
# | \       / |
# |  1 --- 4  |
# | /       \ |
# 2 --------- 3

class TestHamiltonCycle(unittest.TestCase):

    def setUp(self):
        # 3-prism graph, Halin graph
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = [0, 1, 2, 3, 4, 5]
        self.edges = [Edge(0, 1), Edge(0, 2), Edge(0, 5), Edge(1, 2),
        Edge(1, 4), Edge(2, 3), Edge(3, 4), Edge(3, 5), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_graph(self):
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), len(self.edges))

    def test_hamilton(self):
        algorithm = HamiltonCycle(self.G)
        algorithm.run(0)
        # 5 solutions
        expected_cycle = self.nodes
        self.assertEqual(algorithm.hamilton_cycle, expected_cycle)

    def tearDown(self): pass

# 0 ----------o 5
# o \         o |
# |  o       /  |
# |   1 --o 4   |
# |  o       o  |
# | /         \ o
# 2 o---------- 3

class TestHamiltonCycleDirected(unittest.TestCase):

    def setUp(self):
        # 3-prism graph, Halin graph
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = [0, 1, 2, 3, 4, 5]
        self.edges = [Edge(0, 1), Edge(2, 0), Edge(0, 5), Edge(2, 1),
        Edge(1, 4), Edge(3, 2), Edge(3, 4), Edge(5, 3), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_graph(self):
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), len(self.edges))

    def test_hamilton(self):
        algorithm = HamiltonCycle(self.G)
        algorithm.run(0)
        # 5 solutions
        expected_cycle = [0, 1, 4, 5, 3, 2]
        self.assertEqual(algorithm.hamilton_cycle, expected_cycle)

    def tearDown(self): pass


if __name__ == "__main__":

    unittest.main()

# EOF
