#!/usr/bin/env python3

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
        self.nodes = range(self.N)
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


class TestDijkstra2(unittest.TestCase):

    def setUp(self):
        self.N = 9           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1, 65), Edge(1, 8, 41), Edge(1, 2, 35),
            Edge(2, 3, 56), Edge(3, 4, 4),  Edge(3, 6, 20),
            Edge(5, 2, 30), Edge(6, 5, 18), Edge(6, 7, 15),
            Edge(8, 3, 28)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_shortest_path(self):
        source = 0
        target = 7
        algorithm = Dijkstra(self.G)
        algorithm.run(source)
        distance_expected = {0: 0, 1: 65, 2: 100, 3: 134, 4: 138,
            5: 172, 6: 154, 7: 169, 8: 106}
        self.assertEqual(algorithm.distance, distance_expected)
        parent_expected = {0: None, 1: 0, 2: 1, 3: 8, 4: 3, 5: 6,
            6: 3, 7: 6, 8: 1}
        self.assertEqual(algorithm.parent, parent_expected)
        path_expected = [0, 1, 8, 3, 6, 7]
        self.assertEqual(algorithm.path(target), path_expected)

    def test_no_path(self):
        source = 2
        target = 8
        algorithm = Dijkstra(self.G)
        algorithm.run(source)
        distance_expected = {0: float("inf"), 1: float("inf"), 2: 0, 
            3: 56, 4: 60, 5: 94, 6: 76, 7: 91, 8: float("inf")}
        self.assertEqual(algorithm.distance, distance_expected)
        parent_expected = {0: None, 1: None, 2: None, 3: 2, 4: 3,
            5: 6, 6: 3, 7: 6, 8: None}
        self.assertEqual(algorithm.parent, parent_expected)
        #path_expected = []
        #self.assertEqual(algorithm.path(target), path_expected)
        self.assertRaises(ValueError, algorithm.path, target)

    def test_no_path_matrix(self):
        source = 2
        target = 8
        algorithm = DijkstraMatrix(self.G)
        algorithm.run(source)
        distance_expected = {0: float("inf"), 1: float("inf"), 2: 0, 
            3: 56, 4: 60, 5: 94, 6: 76, 7: 91, 8: float("inf")}
        self.assertEqual(algorithm.distance, distance_expected)
        parent_expected = {
            0: None, 1: None, 2: None, 3: 2, 4: 3, 5: 6, 6: 3, 7: 6, 8: None}
        self.assertEqual(algorithm.parent, parent_expected)
        #path_expected = []
        #self.assertEqual(algorithm.path(target), path_expected)
        self.assertRaises(ValueError, algorithm.path, target)

    def test_dijkstra_matrix(self):
        source = 0
        target = 7
        algorithm = DijkstraMatrix(self.G)
        algorithm.run(source)
        distance_expected = {0: 0, 1: 65, 2: 100, 3: 134, 4: 138,
            5: 172, 6: 154, 7: 169, 8: 106}
        self.assertEqual(algorithm.distance, distance_expected)
        parent_expected = {
            0: None, 1: 0, 2: 1, 3: 8, 4: 3, 5: 6, 6: 3, 7: 6, 8: 1}
        self.assertEqual(algorithm.parent, parent_expected)
        path_expected = [0, 1, 8, 3, 6, 7]
        self.assertEqual(algorithm.path(target), path_expected)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
