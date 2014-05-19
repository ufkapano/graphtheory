#!/usr/bin/python
#
# test_dijkstra.py
#
# Tests for Dijkstra.

from edges import Edge
from graphs import Graph
from dijkstra import Dijkstra, DijkstraMatrix
import unittest

#    1
# A --- B
# |   / |
# |5 /1 |3
# | /   |
# C --- D
#    1

class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N)
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
        algorithm = Dijkstra(self.G)
        algorithm.run(source)
        dist_expected = dict(A=0, B=1, C=2, D=3)
        self.assertEqual(algorithm.dist, dist_expected)
        prev_expected = {'A': None, 'C': 'B', 'B': 'A', 'D': 'C'}
        self.assertEqual(algorithm.prev, prev_expected)
        path_expected = ['A', 'B', 'C', 'D']
        self.assertEqual(algorithm.path_to(target), path_expected)

    def test_dijkstra_matrix(self):
        source = "A"
        target = "D"
        algorithm = DijkstraMatrix(self.G)
        algorithm.run(source)
        dist_expected = dict(A=0, B=1, C=2, D=3)
        self.assertEqual(algorithm.dist, dist_expected)
        prev_expected = {'A': None, 'C': 'B', 'B': 'A', 'D': 'C'}
        self.assertEqual(algorithm.prev, prev_expected)
        path_expected = ['A', 'B', 'C', 'D']
        self.assertEqual(algorithm.path_to(target), path_expected)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
