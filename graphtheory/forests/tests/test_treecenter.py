#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treecenter import TreeCenter

# 0     3
# |     |
# |     |
# 1 --- 4 --- 5 --- 6
# |
# |
# 2

class TestTreeCenter(unittest.TestCase):

    def setUp(self):
        self.N = 7           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(1, 2), Edge(1, 4),
            Edge(3, 4), Edge(4, 5), Edge(5, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_center_one(self):
        self.assertEqual(self.G.e(), self.N-1)
        algorithm = TreeCenter(self.G)
        algorithm.run()
        self.assertEqual(algorithm.tree_center, [4])
        self.assertEqual(algorithm.tree_radius, 2)

    def test_center_two(self):
        self.G.add_edge(Edge(6, 7))
        algorithm = TreeCenter(self.G)
        algorithm.run()
        self.assertEqual(algorithm.tree_center, [4, 5])
        self.assertEqual(algorithm.tree_radius, 3)

    def test_path1(self):
        T = Graph(2)
        T.add_edge(Edge(0, 1))
        algorithm = TreeCenter(T)
        algorithm.run()
        self.assertEqual(algorithm.tree_center, [0, 1])
        self.assertEqual(algorithm.tree_radius, 1)

    def test_path2(self):
        T = Graph(3)
        T.add_edge(Edge(0, 1))
        T.add_edge(Edge(1, 2))
        algorithm = TreeCenter(T)
        algorithm.run()
        self.assertEqual(algorithm.tree_center, [1])
        self.assertEqual(algorithm.tree_radius, 1)

    def test_cycle(self):
        self.G.add_edge(Edge(2, 4))
        algorithm = TreeCenter(self.G)
        self.assertRaises(ValueError, algorithm.run)

    def test_directed_graph(self):
        self.G.directed = True
        self.assertRaises(ValueError, TreeCenter, self.G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
