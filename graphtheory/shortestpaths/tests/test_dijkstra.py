#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.shortestpaths.dijkstra import Dijkstra, DijkstraMatrix

#    1
# 0 --> 1
# |   / |
# |5 /1 |3
# |./.  |.
# 2 --> 3
#    1

class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = [0, 1, 2, 3]
        self.edges = [
            Edge(0, 1, 1), Edge(0, 2, 5), Edge(1, 2, 1), Edge(1, 3, 3), 
            Edge(2, 3, 1)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_shortest_path(self):
        source = 0
        target = 3
        algorithm = Dijkstra(self.G)
        algorithm.run(source)
        distance_expected = {0: 0, 1: 1, 2: 2, 3: 3}
        self.assertEqual(algorithm.distance, distance_expected)
        parent_expected = {0: None, 2: 1, 1: 0, 3: 2}
        self.assertEqual(algorithm.parent, parent_expected)
        path_expected = [0, 1, 2, 3]
        self.assertEqual(algorithm.path(target), path_expected)

    def test_dijkstra_matrix(self):
        source = 0
        target = 3
        algorithm = DijkstraMatrix(self.G)
        algorithm.run(source)
        distance_expected = {0: 0, 1: 1, 2: 2, 3: 3}
        self.assertEqual(algorithm.distance, distance_expected)
        parent_expected = {0: None, 2: 1, 1: 0, 3: 2}
        self.assertEqual(algorithm.parent, parent_expected)
        path_expected = [0, 1, 2, 3]
        self.assertEqual(algorithm.path(target), path_expected)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
