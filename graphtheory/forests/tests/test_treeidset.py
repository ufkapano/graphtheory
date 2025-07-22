#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treeidset import TreeIndependentDominatingSet

# 0---1---2---6
# |   |   |
# 3   4   5

class TestDominatingSet1(unittest.TestCase):

    def setUp(self):
        self.N = 7
        self.G = Graph(n=self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(0, 3), Edge(1, 2), 
            Edge(1, 4), Edge(2, 5), Edge(2, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_idset(self):
        algorithm = TreeIndependentDominatingSet(self.G)
        algorithm.run()
        #print(algorithm.dominating_set)
        expected1 = set([0, 4, 2])
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
        self.G = Graph(n=self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 3), Edge(1, 2), 
            Edge(1, 4), Edge(2, 5), Edge(2, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_idset(self):
        algorithm = TreeIndependentDominatingSet(self.G)
        algorithm.run()
        #print(algorithm.dominating_set)
        expected1 = set([1, 5, 6])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
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
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3),
            Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_idset(self):
        algorithm = TreeIndependentDominatingSet(self.G)
        algorithm.run()
        #print(algorithm.dominating_set)
        expected1 = set([1, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def tearDown(self): pass

# 0---1---2---3---4---5---6   path P_7

class TestDominatingSet4(unittest.TestCase):

    def setUp(self):
        self.N = 7
        self.G = Graph(n=self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3),
            Edge(3, 4), Edge(4, 5), Edge(5, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_idset(self):
        algorithm = TreeIndependentDominatingSet(self.G)
        algorithm.run()
        #print(algorithm.dominating_set)
        #expected1 = set([0, 2, 5])
        #expected1 = set([0, 3, 5])
        #expected1 = set([0, 3, 6])
        expected1 = set([0, 2, 5])
        #expected1 = set([1, 3, 5])
        #expected1 = set([1, 3, 6])
        #expected1 = set([1, 4, 6])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

    def tearDown(self): pass

# forest with an isolated node

class TestDominatingSet5(unittest.TestCase):

    def setUp(self):
        self.N = 5
        self.G = Graph(n=self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(2, 3)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_idset(self):
        algorithm = TreeIndependentDominatingSet(self.G)
        algorithm.run()
        #print(algorithm.dominating_set)
        #expected1 = set([1, 3, 4])
        expected1 = set([0, 2, 4])
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
