#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treeiset import BorieIndependentSet

# 0---1---2---6
# |   |   |
# 3   4   5

class TestIndependentSet1(unittest.TestCase):

    def setUp(self):
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [ Edge(0, 1), Edge(0, 3), Edge(1, 2), 
            Edge(1, 4), Edge(2, 5), Edge(2, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_borie_iset(self):
        algorithm = BorieIndependentSet(self.G)
        algorithm.run()
        expected1 = set([3, 4, 5, 6])
        expected2 = set([0, 4, 5, 6])
        #print "iset", algorithm.independent_set
        for edge in self.G.iteredges():
            self.assertFalse(edge.source in algorithm.independent_set and
                             edge.target in algorithm.independent_set)
        self.assertEqual(algorithm.cardinality, 4)
        self.assertEqual(algorithm.cardinality, len(algorithm.independent_set))
        self.assertEqual(algorithm.independent_set, expected2)

    def tearDown(self): pass

# 0---1---2
#   / |   | \
# 3   4   5   6

class TestIndependentSet2(unittest.TestCase):

    def setUp(self):
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 3), Edge(1, 2), Edge(1, 4),
            Edge(2, 5), Edge(2, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_borie_iset(self):
        algorithm = BorieIndependentSet(self.G)
        algorithm.run()
        expected1 = set([0, 3, 4, 5, 6])
        #print "iset", algorithm.independent_set
        for edge in self.G.iteredges():
            self.assertFalse(edge.source in algorithm.independent_set and
                             edge.target in algorithm.independent_set)
        self.assertEqual(algorithm.cardinality, 5)
        self.assertEqual(algorithm.cardinality, len(algorithm.independent_set))
        self.assertEqual(algorithm.independent_set, expected1)

    def tearDown(self): pass

# 0---1---2---3---4---5
# best dset len([1, 4]) = 2
# best node cover len([1, 2, 4]) = 3
# best iset len([0, 2, 5]) = 3

class TestIndependentSet3(unittest.TestCase):

    def setUp(self):
        self.N = 6
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_borie_iset(self):
        algorithm = BorieIndependentSet(self.G)
        algorithm.run()
        expected1 = set([0, 2, 5])
        expected2 = set([0, 3, 5])
        expected3 = set([0, 2, 4])
        expected4 = set([1, 3, 5])
        #print "iset", algorithm.independent_set
        for edge in self.G.iteredges():
            self.assertFalse(edge.source in algorithm.independent_set and
                             edge.target in algorithm.independent_set)
        self.assertEqual(algorithm.cardinality, 3)
        self.assertEqual(algorithm.cardinality, len(algorithm.independent_set))
        self.assertEqual(algorithm.independent_set, expected3)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
