#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treemate import BorieMatching

# 0---1---2---6
# |   |   |
# 3   4   5

class TestMatching1(unittest.TestCase):

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

    def test_borie_matching(self):
        algorithm = BorieMatching(self.G)
        algorithm.run()
        expected1 = set([Edge(0, 3), Edge(1, 4), Edge(2, 5)])
        expected2 = set([Edge(0, 3), Edge(1, 4), Edge(2, 6)])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.mate_set, expected1)
        # Testing matching.
        S = set()
        for edge in algorithm.mate_set:
            S.add(edge.source)
            S.add(edge.target)
        self.assertEqual(len(S), 2 * len(algorithm.mate_set))

    def tearDown(self): pass

# 0---1---2
#   / |   | \
# 3   4   5   6

class TestMatching2(unittest.TestCase):

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

    def test_borie_matching(self):
        algorithm = BorieMatching(self.G)
        algorithm.run()
        expected1 = set([Edge(1, 3), Edge(2, 5)])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.mate_set, expected1)
        # Testing matching.
        S = set()
        for edge in algorithm.mate_set:
            S.add(edge.source)
            S.add(edge.target)
        self.assertEqual(len(S), 2 * len(algorithm.mate_set))

    def tearDown(self): pass

# 0---1---2---3---4---5   path P_6
# best dset len([1, 4]) = 2
# best node cover len([1, 2, 4]) = 3
# best iset len([0, 2, 5]) = 3
# best matching set([Edge(0, 1), Edge(2. 3), Edge(4, 5)])

class TestMatching3(unittest.TestCase):

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

    def test_matching(self):
        algorithm = BorieMatching(self.G)
        algorithm.run()
        expected1 = set([Edge(0, 1), Edge(2, 3), Edge(4, 5)])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.mate_set, expected1)
        # Testing matching.
        S = set()
        for edge in algorithm.mate_set:
            S.add(edge.source)
            S.add(edge.target)
        self.assertEqual(len(S), 2 * len(algorithm.mate_set))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
