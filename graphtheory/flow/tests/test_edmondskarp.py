#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.flow.edmondskarp import EdmondsKarp
from graphtheory.flow.edmondskarp import EdmondsKarpSparse

#     10
#  0 ---> 1
#  |   /  |
#10|  /1  |10
# .| /.   |.
#  2 ---> 3
#     10

class TestEdmondsKarp(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1, 10), Edge(0, 2, 10), Edge(1, 2, 1), Edge(1, 3, 10), 
            Edge(2, 3, 10)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_edmondskarp(self):
        algorithm = EdmondsKarp(self.G)
        algorithm.run(0, 3)
        expected_max_flow = 20
        expected_flow = {
            0: {0: 0, 2: 10, 1: 10, 3: 0}, 
            1: {0: -10, 2: 0, 1: 0, 3: 10}, 
            2: {0: -10, 2: 0, 1: 0, 3: 10}, 
            3: {0: 0, 2: -10, 1: -10, 3: 0}}
        self.assertEqual(algorithm.max_flow, expected_max_flow)
        self.assertEqual(algorithm.flow, expected_flow)

    def test_edmondskarp_sparse(self):
        algorithm = EdmondsKarpSparse(self.G)
        algorithm.run(0, 3)
        expected_max_flow = 20
        expected_flow = {
            0: {1: 10, 2: 10},
            1: {0: -10, 2: 0, 3: 10},
            2: {0: -10, 1: 0, 3: 10},
            3: {1: -10, 2: -10}}
        self.assertEqual(algorithm.max_flow, expected_max_flow)
        self.assertEqual(algorithm.flow, expected_flow)


class TestEdmondsKarpWiki(unittest.TestCase):

    def setUp(self):
        self.N = 7           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1, 3), Edge(0, 3, 3), Edge(1, 2, 4), Edge(2, 0, 3), 
            Edge(2, 3, 1), Edge(2, 4, 2), Edge(3, 4, 2), Edge(3, 5, 6), 
            Edge(4, 1, 1), Edge(4, 6, 1), Edge(5, 6, 9)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_edmondskarp(self):
        algorithm = EdmondsKarp(self.G)
        algorithm.run(0, 6)
        expected_max_flow = 5
        expected_flow = {
            0: {0: 0, 1: 2, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0},
            1: {0: -2, 1: 0, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0},
            2: {0: 0, 1: -2, 2: 0, 3: 1, 4: 1, 5: 0, 6: 0},
            3: {0: -3, 1: 0, 2: -1, 3: 0, 4: 0, 5: 4, 6: 0},
            4: {0: 0, 1: 0, 2: -1, 3: 0, 4: 0, 5: 0, 6: 1},
            5: {0: 0, 1: 0, 2: 0, 3: -4, 4: 0, 5: 0, 6: 4},
            6: {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -4, 6: 0}}
        self.assertEqual(algorithm.max_flow, expected_max_flow)
        self.assertEqual(algorithm.flow, expected_flow)

    def test_edmondskarp_sparse(self):
        algorithm = EdmondsKarpSparse(self.G)
        algorithm.run(0, 6)
        expected_max_flow = 5
        expected_flow = {
            0: {1: 2, 2: 0, 3: 3},
            1: {0: -2, 2: 2, 4: 0},
            2: {0: 0, 1: -2, 3: 1, 4: 1},
            3: {0: -3, 2: -1, 4: 0, 5: 4},
            4: {1: 0, 2: -1, 3: 0, 6: 1},
            5: {3: -4, 6: 4},
            6: {4: -1, 5: -4}}
        self.assertEqual(algorithm.max_flow, expected_max_flow)
        self.assertEqual(algorithm.flow, expected_flow)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
