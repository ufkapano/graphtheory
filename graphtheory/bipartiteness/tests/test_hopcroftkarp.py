#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarp


class TestHopcroftKarp(unittest.TestCase):

    def setUp(self):
        # Wilson, ex. 25.1, bipartite graph
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = [0, 1, 2, 3, 4, 5, 6]
        self.edges = [
            Edge(0, 4), Edge(0, 5), Edge(0, 6), 
            Edge(1, 3), Edge(1, 5), Edge(2, 3), Edge(2, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_matching_hopcroftkarp(self):
        algorithm = HopcroftKarp(self.G)
        algorithm.run()
        # 5 solutions
        expected_cardinality = 3
        expected_pair1 = {0:5, 5:0, 1:3, 3:1, 2:4, 4:2, 6:None}
        expected_pair2 = {0:4, 4:0, 1:5, 5:1, 2:3, 3:2, 6:None}
        expected_pair3 = {0:6, 6:0, 1:3, 3:1, 2:4, 4:2, 5:None}
        expected_pair4 = {0:6, 6:0, 1:5, 5:1, 2:3, 3:2, 4:None}
        expected_pair5 = {0:6, 6:0, 1:5, 5:1, 2:4, 4:2, 3:None}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        self.assertEqual(algorithm.pair, expected_pair1)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
