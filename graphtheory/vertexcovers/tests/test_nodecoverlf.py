#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.vertexcovers.nodecoverlf import LargestFirstNodeCover

# 0---1---2     best node cover len([0, 2, 4]) = 3
# |   | / | \   approximate len([0, 1, 2, 6, 4, 5]) = 6
# 3   4---5   6

class TestNodeCover(unittest.TestCase):

    def setUp(self):
        # Cormen p. 1135
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(0, 3), Edge(1, 2), Edge(1, 4),
            Edge(2, 4), Edge(2, 5), Edge(2, 6), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_node_cover(self):
        algorithm = LargestFirstNodeCover(self.G)
        algorithm.run()
        #print ( "cover {}".format(algorithm.node_cover) )
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)
        self.assertEqual(algorithm.cardinality, 3)
        self.assertEqual(algorithm.cardinality, len(algorithm.node_cover))

    def test_exceptions(self):
        self.assertRaises(ValueError, LargestFirstNodeCover,
            Graph(5, directed=True))

    def tearDown(self): pass

# 0---1---2     best node cover len([1, 2]) = 2
#   / |   | \
# 3   4   5   6

class TestNodeCover2(unittest.TestCase):

    def setUp(self):
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(1, 3), Edge(1, 2), Edge(1, 4),
            Edge(2, 5), Edge(2, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_node_cover(self):
        algorithm = LargestFirstNodeCover(self.G)
        algorithm.run()
        #print ( "cover {}".format(algorithm.node_cover) )
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)
        self.assertEqual(algorithm.cardinality, 2)
        self.assertEqual(algorithm.cardinality, len(algorithm.node_cover))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
