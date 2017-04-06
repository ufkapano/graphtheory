#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treecover import BorieNodeCover

# 0---1---2---6
# |   |   |
# 3   4   5

class TestNodeCover1(unittest.TestCase):

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

    def test_borie_node_cover(self):
        algorithm = BorieNodeCover(self.G)
        algorithm.run()
        expected1 = set([0, 1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected1)
        #print "cover", algorithm.node_cover
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def tearDown(self): pass

# 0---1---2
#   / |   | \
# 3   4   5   6

class TestNodeCover2(unittest.TestCase):

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

    def test_borie_node_cover(self):
        algorithm = BorieNodeCover(self.G)
        algorithm.run()
        expected1 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected1)
        #print "cover", algorithm.node_cover
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def tearDown(self): pass

# 0---1---2---3---4---5
# best dset len([1, 4]) = 2
# best node cover len([1, 2, 4]) = 3
# best iset len([0, 2, 5]) = 3

class TestNodeCover3(unittest.TestCase):

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

    def test_borie_node_cover(self):
        algorithm = BorieNodeCover(self.G)
        algorithm.run()
        expected1 = set([1, 2, 4])
        expected2 = set([1, 3, 4])
        expected3 = set([0, 2, 4])
        expected4 = set([1, 3, 5])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected3)
        #print "cover", algorithm.node_cover
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
