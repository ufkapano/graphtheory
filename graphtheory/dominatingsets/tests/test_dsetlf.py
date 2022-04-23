#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.dominatingsets.dsetlf import LargestFirstDominatingSet

# 0 --- 1 --- 2 not bipartite (triangles are present)
# |   / |     |
# |  /  |     | maximum iset: (0, 4, 2)
# | /   |     | minimum dset: (3, 2), (3, 5), (1, 5), (1, 4), (1, 2), (0, 5)
# 3 --- 4 --- 5

class TestDominatingSet(unittest.TestCase):

    def setUp(self):
        self.N = 6
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(0, 3), Edge(1, 3), Edge(1, 4), 
            Edge(1, 2), Edge(2, 5), Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_dominating_set(self):
        algorithm = LargestFirstDominatingSet(self.G)
        algorithm.run()
        used = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            used.update(self.G.iteradjacent(node))
        self.assertEqual(len(used), self.N)
        self.assertEqual(algorithm.cardinality, len(algorithm.dominating_set))
        self.assertEqual(algorithm.cardinality, 2)   # best = 2
        #print ( algorithm.dominating_set )

    def test_dominating_set_source(self):
        algorithm = LargestFirstDominatingSet(self.G)
        algorithm.run(3)
        used = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            used.update(self.G.iteradjacent(node))
        self.assertEqual(len(used), self.N)
        self.assertEqual(algorithm.cardinality, len(algorithm.dominating_set))
        self.assertEqual(algorithm.cardinality, 2)   # best = 2
        #print ( algorithm.dominating_set )

    def test_exceptions(self):
        self.assertRaises(ValueError, LargestFirstDominatingSet,
            Graph(5, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
