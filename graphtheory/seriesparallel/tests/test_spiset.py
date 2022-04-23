#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.spnodes import Node
from graphtheory.seriesparallel.spiset import SPGraphIndependentSet
from graphtheory.seriesparallel.spiset import SPTreeIndependentSet


class TestIndependentSet(unittest.TestCase):

    def setUp(self):
        pass

    def test_spgraph_independent_set_small(self):
        self.prepareSmallGraph()
        algorithm = SPGraphIndependentSet(self.G, self.root)
        algorithm.run()
        expected1 = set([0, 3, 4])
        expected2 = set([2, 3, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertTrue(algorithm.independent_set == expected1
                        or algorithm.independent_set == expected2)

    def test_sptree_independent_set_small(self):
        self.prepareSmallGraph()
        algorithm = SPTreeIndependentSet(self.root)
        algorithm.run()
        expected1 = set([0, 3, 4])
        expected2 = set([2, 3, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertTrue(algorithm.independent_set == expected1
                        or algorithm.independent_set == expected2)

    def  test_spgraph_independent_set_small2(self):
        self.prepareSmallGraph2()
        algorithm = SPGraphIndependentSet(self.G, self.root)
        algorithm.run()
        expected1 = set([0, 2, 3, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertTrue(algorithm.independent_set == expected1)

    def  test_sptree_independent_set_small2(self):
        self.prepareSmallGraph2()
        algorithm = SPTreeIndependentSet(self.root)
        algorithm.run()
        expected1 = set([0, 2, 3, 4])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertTrue(algorithm.independent_set == expected1)

    def test_spgraph_independent_set_medium(self):
        self.prepareMediumGraph()
        algorithm = SPGraphIndependentSet(self.G, self.root)
        algorithm.run()
        expected = set([1, 2, 3, 4, 7])
        self.assertEqual(algorithm.cardinality, len(expected))
        self.assertEqual(algorithm.independent_set, expected)

    def test_sptree_independent_set_medium(self):
        self.prepareMediumGraph()
        algorithm = SPTreeIndependentSet(self.root)
        algorithm.run()
        expected = set([1, 2, 3, 4, 7])
        self.assertEqual(algorithm.cardinality, len(expected))
        self.assertEqual(algorithm.independent_set, expected)

    def tearDown(self): pass

    def prepareSmallGraph(self):
        # 0      s=0, t=1
        # | \
        # 1---2
        # | \
        # 3   4
        self.N = 5
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2),
                      Edge(1, 3), Edge(1, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        # self.G.show()
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

    def prepareSmallGraph2(self):
        #     0      s=0, t=1
        #     |
        #  3--1--2
        #     |
        #     4
        self.N = 5
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(1, 3), Edge(1, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        # self.G.show()
        node1 = Node(0, 1, "edge")
        node2 = Node(1, 2, "edge")
        node3 = Node(1, 3, "edge")
        node4 = Node(1, 4, "edge")
        node5 = Node(0, 1, "jackknife", node1, node2)
        node6 = Node(0, 1, "jackknife", node5, node3)
        node7 = Node(0, 1, "jackknife", node6, node4)
        self.root = node7

    def prepareMediumGraph(self):
        #    0_____     s=0, t=8
        #    | \ \ \
        # 1  2 3 4  |
        #  \ | |/  /
        #    5 6  /
        #    \/  /
        #    7  /
        #    | /
        #    8
        self.N = 9
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 2), Edge(0, 3), Edge(0, 4), Edge(0, 8),
                      Edge(1, 5), Edge(2, 5), Edge(3, 6), Edge(4, 6),
                      Edge(5, 7), Edge(6, 7), Edge(7, 8)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        # self.G.show()

        node1 = Node(0, 2, "edge")
        node2 = Node(0, 3, "edge")
        node3 = Node(0, 4, "edge")
        node4 = Node(0, 8, "edge")
        node5 = Node(5, 1, "edge")
        node6 = Node(2, 5, "edge")
        node7 = Node(3, 6, "edge")
        node8 = Node(4, 6, "edge")
        node9 = Node(5, 7, "edge")
        node10 = Node(6, 7, "edge")
        node11 = Node(7, 8, "edge")

        node12 = Node(0, 5, "series", node1, node6)
        node13 = Node(0, 6, "series", node2, node7)
        node14 = Node(0, 6, "series", node3, node8)
        node15 = Node(0, 6, "parallel", node13, node14)
        node16 = Node(0, 5, "jackknife", node12, node5)
        node17 = Node(0, 7, "series", node15, node10)
        node18 = Node(0, 7, "series", node16, node9)
        node19 = Node(0, 7, "parallel", node17, node18)
        node20 = Node(0, 8, "series", node19, node11)
        node21 = Node(0, 8, "parallel", node20, node4)

        self.root = node21


if __name__ == "__main__":

    unittest.main()

# EOF
