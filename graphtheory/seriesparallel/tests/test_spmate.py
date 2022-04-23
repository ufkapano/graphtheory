#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.spnodes import Node
from graphtheory.seriesparallel.spmate import SPGraphMatching
from graphtheory.seriesparallel.spmate import SPTreeMatching

# 0      s=0, t=1
# | \
# 1---2
# | \
# 3   4

class TestSPMatching(unittest.TestCase):

    def setUp(self):
        self.N = 5
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2),
            Edge(1, 3), Edge(1, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        node1 = Node(0, 1, "edge")
        node2 = Node(0, 2, "edge")
        node3 = Node(2, 1, "edge")
        node4 = Node(1, 3, "edge")
        node5 = Node(1, 4, "edge")
        node6 = Node(0, 1, "series", node2, node3)
        node7 = Node(0, 1, "parallel", node1, node6)
        node8 = Node(0, 1, "jackknife", node7, node4)
        node9 = Node(0, 1, "jackknife", node8, node5)
        self.root = node9

    def test_spgraph_mate(self):
        algorithm = SPGraphMatching(self.G, self.root)
        algorithm.run()
        expected1 = set([Edge(0, 2), Edge(1, 3)])
        expected2 = set([Edge(0, 2), Edge(1, 4)])
        #print "mate_set", algorithm.mate_set
        #print "mate", algorithm.mate
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.mate_set, expected1)
        #self.assertEqual(algorithm.mate_set, expected2)
        # Test poprawnosci skojarzenia na krawedziach.
        # Sprawdzam, czy konce sie nie powtarzaja.
        S = set()
        for edge in algorithm.mate_set:
            S.add(edge.source)
            S.add(edge.target)
        self.assertEqual(len(S), 2 * len(algorithm.mate_set))

    def test_sptree_mate(self):
        algorithm = SPTreeMatching(self.root)
        algorithm.run()
        expected1 = set([Edge(0, 2), Edge(1, 3)])
        expected2 = set([Edge(0, 2), Edge(1, 4)])
        #print "mate_set", algorithm.mate_set
        #print "mate", algorithm.mate
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.mate_set, expected1)
        #self.assertEqual(algorithm.mate_set, expected2)
        # Test poprawnosci skojarzenia na krawedziach.
        # Sprawdzam, czy konce sie nie powtarzaja.
        S = set()
        for edge in algorithm.mate_set:
            S.add(edge.source)
            S.add(edge.target)
        self.assertEqual(len(S), 2 * len(algorithm.mate_set))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
