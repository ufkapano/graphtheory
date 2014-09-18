#!/usr/bin/python

from edges import Edge
from graphs import Graph
from bellmanford import BellmanFord
import unittest

#    1
# 0 --> 1
# |   / |
# |5 /1 |3
# |./.  |.
# 2 --> 3
#    1

class TestBellmanFord(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True) # directed graph
        self.nodes = [0, 1, 2, 3]
        self.edges = [Edge(0, 1, 1), Edge(0, 2, 5), 
        Edge(1, 2, 1), Edge(1, 3, 3), Edge(2, 3, 1)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_shortest_path(self):
        source = 0
        target = 3
        algorithm = BellmanFord(self.G)
        algorithm.run(source)
        dist_expected = {0: 0, 2: 2, 1: 1, 3: 3}
        self.assertEqual(algorithm.dist, dist_expected)
        prev_expected = {0: None, 2: 1, 1: 0, 3: 2}
        self.assertEqual(algorithm.prev, prev_expected)
        path_expected = [0, 1, 2, 3]
        self.assertEqual(algorithm.path(target), path_expected)

    def tearDown(self): pass


class TestBellmanFordCormen(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.666, negative weights.
        self.N = 5           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = [0, 1, 2, 3, 4]
        self.edges = [Edge(0, 1, 6), Edge(0, 3, 7),
        Edge(1, 3, 8), Edge(1, 2, 5), Edge(1, 4, -4),
        Edge(2, 1, -2), Edge(3, 2, -3), Edge(3, 4, 9),
        Edge(4, 0, 2), Edge(4, 2, 7)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_shortest_path_cormen(self):
        source = 0
        target = 4
        algorithm = BellmanFord(self.G)
        algorithm.run(source)
        dist_expected = {3: 7, 2: 4, 0: 0, 4: -2, 1: 2}
        self.assertEqual(algorithm.dist, dist_expected)
        prev_expected = {3: 0, 2: 3, 0: None, 4: 1, 1: 2}
        self.assertEqual(algorithm.prev, prev_expected)
        path_expected = [0, 3, 2, 1, 4]
        self.assertEqual(algorithm.path(target), path_expected)


    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF