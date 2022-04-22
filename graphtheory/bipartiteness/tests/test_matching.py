#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.bipartiteness.matching import MatchingFordFulkersonSet
from graphtheory.bipartiteness.matching import MatchingFordFulkersonList
from graphtheory.bipartiteness.matching import MatchingFordFulkersonColor


class TestMatching(unittest.TestCase):

    def setUp(self):
        # Wilson, ex. 25.1, bipartite graph
        # 0 : 4 5 6
        # 1 : 3 5
        # 2 : 3 4
        # ...
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 4), Edge(0, 5), Edge(0, 6), Edge(1, 3), Edge(1, 5), 
            Edge(2, 3), Edge(2, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_matching_fordfulkerson_set(self):
        algorithm = MatchingFordFulkersonSet(self.G)
        algorithm.run()
        # 5 solutions
        expected_cardinality = 3
        expected_mate1 = {0:5, 5:0, 1:3, 3:1, 2:4, 4:2, 6:None}
        expected_mate2 = {0:4, 4:0, 1:5, 5:1, 2:3, 3:2, 6:None}
        expected_mate3 = {0:6, 6:0, 1:3, 3:1, 2:4, 4:2, 5:None}
        expected_mate4 = {0:6, 6:0, 1:5, 5:1, 2:3, 3:2, 4:None}
        expected_mate5 = {0:6, 6:0, 1:5, 5:1, 2:4, 4:2, 3:None}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        self.assertEqual(algorithm.mate, expected_mate5)

    def test_matching_fordfulkerson_list(self):
        algorithm = MatchingFordFulkersonList(self.G)
        algorithm.run()
        # 5 solutions
        expected_cardinality = 3
        expected_mate1 = {0:5, 5:0, 1:3, 3:1, 2:4, 4:2, 6:None}
        expected_mate2 = {0:4, 4:0, 1:5, 5:1, 2:3, 3:2, 6:None}
        expected_mate3 = {0:6, 6:0, 1:3, 3:1, 2:4, 4:2, 5:None}
        expected_mate4 = {0:6, 6:0, 1:5, 5:1, 2:3, 3:2, 4:None}
        expected_mate5 = {0:6, 6:0, 1:5, 5:1, 2:4, 4:2, 3:None}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        self.assertEqual(algorithm.mate, expected_mate5)

    def test_matching_fordfulkerson_color(self):
        algorithm = MatchingFordFulkersonColor(self.G)
        algorithm.run()
        # 5 solutions
        expected_cardinality = 3
        expected_mate1 = {0:5, 5:0, 1:3, 3:1, 2:4, 4:2, 6:None}
        expected_mate2 = {0:4, 4:0, 1:5, 5:1, 2:3, 3:2, 6:None}
        expected_mate3 = {0:6, 6:0, 1:3, 3:1, 2:4, 4:2, 5:None}
        expected_mate4 = {0:6, 6:0, 1:5, 5:1, 2:3, 3:2, 4:None}
        expected_mate5 = {0:6, 6:0, 1:5, 5:1, 2:4, 4:2, 3:None}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        self.assertEqual(algorithm.mate, expected_mate5)

    def test_exceptions(self):
        self.assertRaises(ValueError, MatchingFordFulkersonSet, Graph(2, directed=True))
        self.assertRaises(ValueError, MatchingFordFulkersonList, Graph(2, directed=True))
        self.assertRaises(ValueError, MatchingFordFulkersonColor, Graph(2, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
