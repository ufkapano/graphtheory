#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treecover import BorieNodeCover
from graphtheory.forests.treecover import TreeNodeCover1
from graphtheory.forests.treecover import TreeNodeCover2

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
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def test_tree_node_cover1(self):
        algorithm = TreeNodeCover1(self.G)
        algorithm.run()
        expected1 = set([0, 1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected1)
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def test_tree_node_cover2(self):
        algorithm = TreeNodeCover2(self.G)
        algorithm.run()
        expected1 = set([0, 1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected1)
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
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def test_tree_node_cover1(self):
        algorithm = TreeNodeCover1(self.G)
        algorithm.run()
        expected1 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected1)
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def test_tree_node_cover2(self):
        algorithm = TreeNodeCover2(self.G)
        algorithm.run()
        expected1 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected1)
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def tearDown(self): pass

# 0---1---2---3---4---5   path P_6
# best dset len([1, 4]) = 2
# best node cover len([1, 2, 4]) = 3
# best iset len([0, 2, 5]) = 3
# best matching set([Edge(0, 1), Edge(2. 3), Edge(4, 5)])

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
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def test_tree_node_cover1(self):
        algorithm = TreeNodeCover1(self.G)
        algorithm.run()
        expected1 = set([1, 2, 4])
        expected2 = set([1, 3, 4])
        expected3 = set([0, 2, 4])
        expected4 = set([1, 3, 5])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected2)
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def test_tree_node_cover2(self):
        algorithm = TreeNodeCover2(self.G)
        algorithm.run()
        expected1 = set([1, 2, 4])
        expected2 = set([1, 3, 4])
        expected3 = set([0, 2, 4])
        expected4 = set([1, 3, 5])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected2)
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover or
                            edge.target in algorithm.node_cover)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
