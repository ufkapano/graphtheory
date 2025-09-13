#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treewdset import TreeWeightedDominatingSet1
from graphtheory.forests.treewdset import TreeWeightedDominatingSet2

# 0---1---2---6
# |   |   |
# 3   4   5

class TestDominatingSet1(unittest.TestCase):

    def setUp(self):
        self.N = 7
        self.G = Graph(n=self.N)
        self.nodes = range(self.N)
        # wagi 1 lub 3 stosownie do kolorowania wierzcholkow
        self.weights1 = dict([(0,3),(1,1),(2,3),(3,1),(4,3),(5,1),(6,1)])
        # wagi jednakowe
        self.weights2 = dict((node, 2) for node in self.nodes)
        self.edges = [Edge(0, 1), Edge(0, 3), Edge(1, 2), 
            Edge(1, 4), Edge(2, 5), Edge(2, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_weighted_dset_w1_a1(self):
        algorithm = TreeWeightedDominatingSet1(self.G, self.weights1)
        algorithm.run()
        expected1 = set([3, 1, 5, 6])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 4)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_weighted_dset_w1_a2(self):
        algorithm = TreeWeightedDominatingSet2(self.G, self.weights1)
        algorithm.run()
        expected1 = set([3, 1, 5, 6])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 4)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_weighted_dset_w2_a1(self):
        algorithm = TreeWeightedDominatingSet1(self.G, self.weights2)
        algorithm.run()
        expected1 = set([0, 1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 6)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_weighted_dset_w2_a2(self):
        algorithm = TreeWeightedDominatingSet2(self.G, self.weights2)
        algorithm.run()
        expected1 = set([0, 1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 6)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def tearDown(self): pass

# 0---1---2
#   / |   | \
# 3   4   5   6

class TestDominatingSet2(unittest.TestCase):

    def setUp(self):
        self.N = 7
        self.G = Graph(n=self.N)
        self.nodes = range(self.N)
        # wagi 1 lub 3 stosownie do kolorowania wierzcholkow
        self.weights1 = dict([(0,3),(1,1),(2,3),(3,1),(4,3),(5,1),(6,1)])
        # wagi jednakowe
        self.weights2 = dict((node, 2) for node in self.nodes)
        self.edges = [Edge(0, 1), Edge(1, 3), Edge(1, 2), 
            Edge(1, 4), Edge(2, 5), Edge(2, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_weighted_dset_w1_a1(self):
        algorithm = TreeWeightedDominatingSet1(self.G, self.weights1)
        algorithm.run()
        expected1 = set([1, 5, 6])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 3)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_weighted_dset_w1_a2(self):
        algorithm = TreeWeightedDominatingSet2(self.G, self.weights1)
        algorithm.run()
        expected1 = set([1, 5, 6])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 3)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_weighted_dset_w2_a1(self):
        algorithm = TreeWeightedDominatingSet1(self.G, self.weights2)
        algorithm.run()
        expected1 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 4)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_weighted_dset_w2_a2(self):
        algorithm = TreeWeightedDominatingSet2(self.G, self.weights2)
        algorithm.run()
        expected1 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 4)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def tearDown(self): pass

# 0---1---2---3---4---5   path P_6

class TestDominatingSet3(unittest.TestCase):

    def setUp(self):
        self.N = 6
        self.G = Graph(n=self.N)
        self.nodes = range(self.N)
        # wagi 1 lub 3 stosownie do kolorowania wierzcholkow
        self.weights1 = dict([(0,1),(1,3),(2,1),(3,3),(4,1),(5,3)])
        # wagi jednakowe
        self.weights2 = dict((node, 2) for node in self.nodes)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3),
            Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_weighted_dset_w1_a1(self):
        algorithm = TreeWeightedDominatingSet1(self.G, self.weights1)
        algorithm.run()
        expected1 = set([0, 2, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 3)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_weighted_dset_w1_a2(self):
        algorithm = TreeWeightedDominatingSet2(self.G, self.weights1)
        algorithm.run()
        expected1 = set([0, 2, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 3)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_weighted_dset_w2_a1(self):
        algorithm = TreeWeightedDominatingSet1(self.G, self.weights2)
        algorithm.run()
        expected1 = set([1, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 4)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_weighted_dset_w2_a2(self):
        algorithm = TreeWeightedDominatingSet2(self.G, self.weights2)
        algorithm.run()
        expected1 = set([1, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        self.assertEqual(algorithm.dominating_set_weight, 4)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
