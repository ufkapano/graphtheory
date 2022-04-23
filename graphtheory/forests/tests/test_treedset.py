#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treedset import BorieDominatingSet
from graphtheory.forests.treedset import TreeDominatingSet1
from graphtheory.forests.treedset import TreeDominatingSet2

# 0---1---2---6
# |   |   |
# 3   4   5

class TestDominatingSet1(unittest.TestCase):

    def setUp(self):
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(0, 3), Edge(1, 2), 
            Edge(1, 4), Edge(2, 5), Edge(2, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_borie_dset(self):
        algorithm = BorieDominatingSet(self.G)
        algorithm.run()
        expected1 = set([0, 1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_tree_dset1(self):
        algorithm = TreeDominatingSet1(self.G)
        algorithm.run()
        expected1 = set([0, 1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_tree_dset2(self):
        algorithm = TreeDominatingSet2(self.G)
        algorithm.run()
        expected1 = set([0, 1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
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
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 3), Edge(1, 2), 
            Edge(1, 4), Edge(2, 5), Edge(2, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_borie_dset(self):
        algorithm = BorieDominatingSet(self.G)
        algorithm.run()
        expected1 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_tree_dset1(self):
        algorithm = TreeDominatingSet1(self.G)
        algorithm.run()
        expected1 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_tree_dset2(self):
        algorithm = TreeDominatingSet2(self.G)
        algorithm.run()
        expected1 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def tearDown(self): pass

# 0---1---2---3---4---5   path P_6
# best dset len([1, 4]) = 2
# best node cover len([1, 2, 4]) = 3
# best iset len([0, 2, 5]) = 3
# best matching set([Edge(0, 1), Edge(2. 3), Edge(4, 5)])

class TestDominatingSet3(unittest.TestCase):

    def setUp(self):
        self.N = 6
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3),
            Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_borie_dset(self):
        algorithm = BorieDominatingSet(self.G)
        algorithm.run()
        expected1 = set([1, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_tree_dset1(self):
        algorithm = TreeDominatingSet1(self.G)
        algorithm.run()
        expected1 = set([1, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def test_tree_dset2(self):
        algorithm = TreeDominatingSet2(self.G)
        algorithm.run()
        expected1 = set([1, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
