#!/usr/bin/python

from edges import Edge
from graphs import Graph
from matching import MatchingFordFulkerson
import unittest


class TestMatching(unittest.TestCase):

    def setUp(self):
        # Wilson, ex. 25.1, bipartite graph
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = [0, 1, 2, 3, 4, 5, 6]
        self.edges = [Edge(0, 4), Edge(0, 5), Edge(0, 6), 
            Edge(1, 3), Edge(1, 5), Edge(2, 3), Edge(2, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_matching_fordfulkerson(self):
        algorithm = MatchingFordFulkerson(self.G)
        algorithm.run()
        # 5 solutions
        expected_cardinality = 3
        expected_matching1 = set([Edge(0, 5), Edge(1, 3), Edge(2, 4)])
        expected_matching2 = set([Edge(0, 4), Edge(1, 5), Edge(2, 3)])
        expected_matching3 = set([Edge(0, 6), Edge(1, 3), Edge(2, 4)])
        expected_matching4 = set([Edge(0, 6), Edge(1, 5), Edge(2, 3)])
        expected_matching5 = set([Edge(0, 6), Edge(1, 5), Edge(2, 4)])
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        self.assertEqual(algorithm.matching, expected_matching5)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
