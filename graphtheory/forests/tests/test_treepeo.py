#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treepeo import find_peo_tree
from graphtheory.forests.treepeo import TreePEO

# 0---1---3---4
#     |   |
#     2   5

class TestTreePEO(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(n=self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(1, 3), Edge(3, 4), Edge(3, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_peo1(self):
        self.assertEqual(self.G.e(), self.N-1)
        peo = find_peo_tree(self.G)
        self.assertEqual(len(peo), self.N)
        self.assertEqual(peo, [0, 2, 4, 5, 1, 3])

        algorithm = TreePEO(self.G)
        algorithm.run()
        self.assertEqual(algorithm.peo, [0, 2, 4, 5, 1, 3])
        self.assertEqual(len(algorithm.parent), self.G.v())
        self.assertEqual(algorithm.parent, {0: 1, 2: 1, 4: 3, 5: 3, 1: 3, 3: None})
        #print(algorithm.parent)

    def test_peo2(self):   # single edge
        T = Graph()
        for edge in [Edge(0, 1)]:
            T.add_edge(edge)
        peo = find_peo_tree(T)
        self.assertEqual(len(peo), T.v())
        self.assertEqual(peo, [0, 1])

        algorithm = TreePEO(T)
        algorithm.run()
        self.assertEqual(algorithm.peo, [0, 1])
        self.assertEqual(len(algorithm.parent), T.v())
        #print(algorithm.parent)

    def test_peo3(self):   # two trees
        T = Graph()
        for edge in [Edge(0, 1), Edge(2, 3)]:
            T.add_edge(edge)
        peo = find_peo_tree(T)
        self.assertEqual(len(peo), 4)
        self.assertEqual(peo, [0, 1, 2, 3])

        algorithm = TreePEO(T)
        algorithm.run()
        self.assertEqual(algorithm.peo, [0, 1, 2, 3])
        self.assertEqual(len(algorithm.parent), T.v())
        #print(algorithm.parent)

    def test_peo4(self):
        T = Graph()
        for edge in [Edge(0, 1), Edge(0, 2), Edge(0, 3)]:
            T.add_edge(edge)
        peo = find_peo_tree(T)
        self.assertEqual(len(peo), 4)
        self.assertEqual(peo, [1, 2, 3, 0])

        algorithm = TreePEO(T)
        algorithm.run()
        self.assertEqual(algorithm.peo, [1, 2, 3, 0])
        self.assertEqual(len(algorithm.parent), T.v())
        self.assertEqual(algorithm.parent, {1: 0, 2: 0, 3: 0, 0: None})
        #print(algorithm.parent)

    def test_peo5(self):   # two trees and a single node
        T = Graph()
        for node in range(5):
            T.add_node(node)
        for edge in [Edge(0, 1), Edge(2, 3)]:
            T.add_edge(edge)
        peo = find_peo_tree(T)
        self.assertEqual(len(peo), 5)
        self.assertEqual(peo, [4, 0, 1, 2, 3])

        algorithm = TreePEO(T)
        algorithm.run()
        self.assertEqual(algorithm.peo, [4, 0, 1, 2, 3])
        self.assertEqual(len(algorithm.parent), T.v())
        #print(algorithm.parent)

    def test_directed_graph(self):
        self.G.directed = True
        self.assertRaises(ValueError, TreePEO, self.G)
        T = Graph()   # not a tree
        for edge in [Edge(0, 1), Edge(0, 2), Edge(1, 2), Edge(0, 3)]:
            T.add_edge(edge)
        algorithm = TreePEO(T)
        self.assertRaises(ValueError, algorithm.run)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
