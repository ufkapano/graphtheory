#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.bipartiteness.matchingap import MatchingUsingAugmentingPath

# 3---1---5
# |       |
# 2---4---0---6

class TestMatching(unittest.TestCase):

    def setUp(self):
        # Wilson, ex. 25.1, bipartite graph
        # 0 : 4 5 6
        # 1 : 3 5
        # 2 : 3 4
        # ...
        self.N = 7
        self.G = Graph(n=self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 4), Edge(0, 5), Edge(0, 6), Edge(1, 3),
            Edge(1, 5), Edge(2, 3), Edge(2, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_matching_augmenting_path(self):
        algorithm = MatchingUsingAugmentingPath(self.G)
        algorithm.run()
        # 5 solutions
        expected_cardinality = 3
        expected_mate1 = {0:5, 5:0, 1:3, 3:1, 2:4, 4:2, 6:None}
        expected_mate2 = {0:4, 4:0, 1:5, 5:1, 2:3, 3:2, 6:None}
        expected_mate3 = {0:6, 6:0, 1:3, 3:1, 2:4, 4:2, 5:None}
        expected_mate4 = {0:6, 6:0, 1:5, 5:1, 2:3, 3:2, 4:None}
        expected_mate5 = {0:6, 6:0, 1:5, 5:1, 2:4, 4:2, 3:None}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        self.assertEqual(algorithm.mate, expected_mate1)

    def test_exceptions(self):
        self.assertRaises(ValueError, MatchingUsingAugmentingPath, 
            Graph(n=2, directed=True))

    def tearDown(self): pass


class TestMatchingCube(unittest.TestCase):

    def setUp(self):
        self.N = 8
        gf = GraphFactory(Graph)
        self.G = gf.make_prism(size=4)
        # Sa kolejne wagi, ale z nich nie korzystam.
        self.nodes = list(self.G.iternodes())
        self.edges = list(self.G.iteredges())
        #self.G.show()

    def test_matching_augmenting_path(self):
        algorithm = MatchingUsingAugmentingPath(self.G)
        algorithm.run()
        # many solutions
        expected_cardinality = 4
        expected_mate1 = {0: 6, 1: 3, 2: 4, 3: 1, 4: 2, 5: 7, 6: 0, 7: 5}
        expected_mate2 = {0: 2, 1: 3, 2: 0, 3: 1, 4: 6, 5: 7, 6: 4, 7: 5}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        self.assertEqual(algorithm.mate, expected_mate2)

    def test_exceptions(self):
        self.assertRaises(ValueError, MatchingUsingAugmentingPath,
            Graph(n=2, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
