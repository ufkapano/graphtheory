#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.shortestpaths.floydwarshall import *


class TestFloydWarshall(unittest.TestCase):

    def setUp(self):
        self.N = 5           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 2, 6), Edge(0, 3, 3), Edge(1, 0, 3), Edge(2, 3, 2), 
            Edge(3, 1, 1), Edge(3, 2, 1), Edge(4, 1, 4), Edge(4, 3, 2)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_floydwarshall(self):
        algorithm = FloydWarshall(self.G)
        algorithm.run()
        expected_distance = {
            0: {0: 0, 1: 4, 2: 4, 3: 3, 4: float("inf")}, 
            1: {0: 3, 1: 0, 2: 7, 3: 6, 4: float("inf")}, 
            2: {0: 6, 1: 3, 2: 0, 3: 2, 4: float("inf")}, 
            3: {0: 4, 1: 1, 2: 1, 3: 0, 4: float("inf")}, 
            4: {0: 6, 1: 3, 2: 3, 3: 2, 4: 0}}
        self.assertEqual(algorithm.distance, expected_distance)

    def test_floydwarshall_paths(self):
        algorithm = FloydWarshallPaths(self.G)
        algorithm.run()
        expected_distance = {
            0: {0: 0, 1: 4, 2: 4, 3: 3, 4: float("inf")}, 
            1: {0: 3, 1: 0, 2: 7, 3: 6, 4: float("inf")}, 
            2: {0: 6, 1: 3, 2: 0, 3: 2, 4: float("inf")}, 
            3: {0: 4, 1: 1, 2: 1, 3: 0, 4: float("inf")}, 
            4: {0: 6, 1: 3, 2: 3, 3: 2, 4: 0}}
        expected_parent = {
            0: {0: None, 2: 3, 1: 3, 4: None, 3: 0}, 
            1: {0: 1, 2: 3, 1: None, 4: None, 3: 0}, 
            2: {0: 1, 2: None, 1: 3, 4: None, 3: 2}, 
            3: {0: 1, 2: 3, 1: 3, 4: None, 3: None}, 
            4: {0: 1, 2: 3, 1: 3, 4: None, 3: 4}}
        self.assertEqual(algorithm.distance, expected_distance)
        self.assertEqual(algorithm.parent, expected_parent)
        self.assertEqual(algorithm.path(0, 1), [0, 3, 1])

    def test_floydwarshall_negative_cycle(self):
        self.G.add_edge(Edge(1, 3, -2))
        algorithm = FloydWarshall(self.G)
        self.assertRaises(ValueError, algorithm.run)


class TestFloydWarshallNegativeEdges(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1, 3), Edge(0, 2, 6), Edge(1, 2, 4), Edge(1, 3, 5), 
            Edge(2, 3, 2), Edge(3, 0, -5), Edge(3, 1, -3)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_negative_edges(self):
        algorithm = FloydWarshall(self.G)
        algorithm.run()
        expected_distance = {
            0: {0: 0, 1: 3, 2: 6, 3: 8}, 
            1: {0: 0, 1: 0, 2: 4, 3: 5}, 
            2: {0: -3, 1: -1, 2: 0, 3: 2}, 
            3: {0: -5, 1: -3, 2: 1, 3: 0}}
        self.assertEqual(algorithm.distance, expected_distance)

    def test_negative_edges_with_paths(self):
        algorithm = FloydWarshallPaths(self.G)
        algorithm.run()
        expected_distance = {
            0: {0: 0, 1: 3, 2: 6, 3: 8}, 
            1: {0: 0, 1: 0, 2: 4, 3: 5}, 
            2: {0: -3, 1: -1, 2: 0, 3: 2}, 
            3: {0: -5, 1: -3, 2: 1, 3: 0}}
        expected_parent = {
            0: {0: None, 1: 0, 2: 0, 3: 1}, 
            1: {0: 3, 1: None, 2: 1, 3: 1}, 
            2: {0: 3, 1: 3, 2: None, 3: 2}, 
            3: {0: 3, 1: 3, 2: 0, 3: None}}
        self.assertEqual(algorithm.distance, expected_distance)
        self.assertEqual(algorithm.parent, expected_parent)
        self.assertEqual(algorithm.path(0, 3), [0, 1, 3])

    def test_negative_cycle(self):
        self.G.add_edge(Edge(0, 3, 2))
        algorithm = FloydWarshall(self.G)
        self.assertRaises(ValueError, algorithm.run)

#    3     6
# 1 --- 0 --- 2
# | \   |   /
# |4 \1 |3 /2
# |   \ | /
# 4 --- 3
#    2

class TestFloydWarshallAllGraphs(unittest.TestCase):

    def setUp(self):
        self.N = 5           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 2, 6), Edge(0, 3, 3), Edge(1, 0, 3), Edge(2, 3, 2), 
            Edge(3, 1, 1), Edge(4, 1, 4), Edge(4, 3, 2)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_floydwarshall(self):
        algorithm = FloydWarshallAllGraphs(self.G)
        algorithm.run()
        expected_distance = {
            0: {0: 0, 1: 3, 2: 5, 3: 3, 4: 5}, 
            1: {0: 3, 1: 0, 2: 3, 3: 1, 4: 3}, 
            2: {0: 5, 1: 3, 2: 0, 3: 2, 4: 4}, 
            3: {0: 3, 1: 1, 2: 2, 3: 0, 4: 2}, 
            4: {0: 5, 1: 3, 2: 4, 3: 2, 4: 0}}
        self.assertEqual(algorithm.distance, expected_distance)

    def test_negative_edge(self):
        # An edge with the negative weight gives a negative cycle.
        self.G.add_edge(Edge(2, 4, -1))
        algorithm = FloydWarshallAllGraphs(self.G)
        self.assertRaises(ValueError, algorithm.run)

if __name__ == "__main__":

    unittest.main()

# EOF
