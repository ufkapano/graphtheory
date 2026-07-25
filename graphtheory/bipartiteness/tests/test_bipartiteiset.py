#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.bipartiteness.bipartiteiset import BipartiteIndependentSet

# 0---1---2   max iset1 {0,2,4}
# |   |   |   max iset2 {1,3,5}
# 3---4---5

class TestBipartiteIndependentSet1(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(n=self.N, directed=False)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(1, 2), Edge(0, 3), Edge(1, 4), Edge(2, 5), 
            Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_bipartite_iset(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = BipartiteIndependentSet(self.G)
        algorithm.run()
        iset1_expected = {0, 2, 4}
        iset2_expected = {1, 3, 5}
        self.assertEqual(algorithm.independent_set, iset1_expected)
        self.assertEqual(algorithm.cardinality, 3)

    def tearDown(self): pass

# 1   2   3       maximum matching {(2,4),(3,5)} (przykladowe krawedzie)
#   \ | / | \       minimum vertex cover {3,4}
#     4   5   0   maximum iset {1,2,5,0}

class TestBipartiteIndependentSet2(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(n=self.N, directed=False)
        self.nodes = range(self.N)
        self.edges = [Edge(1,4), Edge(2,4), Edge(3,4), Edge(3,5), Edge(3,0)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_bipartite_iset(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = BipartiteIndependentSet(self.G)
        algorithm.run()
        iset_expected = {0, 1, 2, 5}
        self.assertEqual(algorithm.independent_set, iset_expected)
        self.assertEqual(algorithm.cardinality, 4)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
