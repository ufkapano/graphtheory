#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.traversing.dfs import DFSWithStack
from graphtheory.traversing.dfs import DFSWithRecursion
from graphtheory.traversing.dfs import SimpleDFS
from graphtheory.traversing.dfs import DFSWithDepthTracker

# 0---1   2---3
# |   | / | / |
# 4   5---6---7

class TestDFS(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 4, 2), Edge(0, 1, 3), Edge(1, 5, 4), Edge(5, 2, 5), 
            Edge(5, 6, 6), Edge(2, 6, 7), Edge(2, 3, 8), Edge(6, 3, 9), 
            Edge(6, 7, 10), Edge(3, 7, 11)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_dfs_with_stack(self):
        self.assertEqual(self.G.v(), self.N)
        pre_order = []
        post_order = []
        algorithm = DFSWithStack(self.G)
        algorithm.run(1, pre_action=lambda node: pre_order.append(node),
                        post_action=lambda node: post_order.append(node))
        pre_order_expected = [1, 0, 5, 2, 6, 3, 7, 4]
        post_order_expected = [1, 5, 6, 7, 3, 2, 0, 4]
        self.assertEqual(pre_order, pre_order_expected)
        self.assertEqual(post_order, post_order_expected)
        dd_expected = {0: 2, 1: 1, 2: 5, 3: 8, 4: 14, 5: 3, 6: 6, 7: 9}
        ff_expected = {0: 15, 1: 4, 2: 13, 3: 12, 4: 16, 5: 7, 6: 10, 7: 11}
        self.assertEqual(algorithm.dd, dd_expected)
        self.assertEqual(algorithm.ff, ff_expected)
        parent_expected = {0: 1, 1: None, 2: 5, 3: 6, 4: 0, 5: 1, 6: 5, 7: 6}
        self.assertEqual(algorithm.parent, parent_expected)
        self.assertEqual(algorithm.path(1, 7), [1, 5, 6, 7])
        self.assertEqual(algorithm.path(1, 4), [1, 0, 4])
        #algorithm.dag.show()
        self.assertEqual(algorithm.dag.v(), self.N)
        self.assertEqual(algorithm.dag.e(), self.N-1)
        self.assertTrue(algorithm.dag.is_directed())
        for edge in algorithm.dag.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def test_dfs_with_recursion(self):
        self.assertEqual(self.G.v(), self.N)
        pre_order = []
        post_order = []
        algorithm = DFSWithRecursion(self.G)
        algorithm.run(1, pre_action=lambda node: pre_order.append(node),
                        post_action=lambda node: post_order.append(node))
        pre_order_expected = [1, 0, 4, 5, 2, 3, 6, 7]
        post_order_expected = [4, 0, 7, 6, 3, 2, 5, 1]
        #self.assertEqual(pre_order, pre_order_expected)
        #self.assertEqual(post_order, post_order_expected)
        dd_expected = {0: 2, 1: 1, 2: 7, 3: 8, 4: 3, 5: 6, 6: 9, 7: 10}
        ff_expected = {0: 5, 1: 16, 2: 14, 3: 13, 4: 4, 5: 15, 6: 12, 7: 11}
        #self.assertEqual(algorithm.dd, dd_expected)
        #self.assertEqual(algorithm.ff, ff_expected)
        parent_expected = {0: 1, 1: None, 2: 5, 3: 2, 4: 0, 5: 1, 6: 3, 7: 6}
        #self.assertEqual(algorithm.parent, parent_expected)
        #self.assertEqual(algorithm.path(1, 7), [1, 5, 2, 3, 6, 7])
        self.assertEqual(algorithm.path(1, 4), [1, 0, 4])
        #algorithm.dag.show()
        self.assertEqual(algorithm.dag.v(), self.N)
        self.assertEqual(algorithm.dag.e(), self.N-1)
        self.assertTrue(algorithm.dag.is_directed())
        for edge in algorithm.dag.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def test_simple_dfs_with_recursion(self):
        self.assertEqual(self.G.v(), self.N)
        pre_order = []
        post_order = []
        algorithm = SimpleDFS(self.G)
        algorithm.run(1, pre_action=lambda node: pre_order.append(node),
                        post_action=lambda node: post_order.append(node))
        pre_order_expected = [1, 0, 4, 5, 2, 3, 6, 7]
        post_order_expected = [4, 0, 7, 6, 3, 2, 5, 1]
        #self.assertEqual(pre_order, pre_order_expected)
        #self.assertEqual(post_order, post_order_expected)
        parent_expected = {0: 1, 1: None, 2: 5, 3: 2, 4: 0, 5: 1, 6: 3, 7: 6}
        #self.assertEqual(algorithm.parent, parent_expected)
        #self.assertEqual(algorithm.path(1, 7), [1, 5, 2, 3, 6, 7])
        self.assertEqual(algorithm.path(1, 4), [1, 0, 4])
        #algorithm.dag.show()
        self.assertEqual(algorithm.dag.v(), self.N)
        self.assertEqual(algorithm.dag.e(), self.N-1)
        self.assertTrue(algorithm.dag.is_directed())
        for edge in algorithm.dag.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def test_dfs_with_depth_tracker(self):
        self.assertEqual(self.G.v(), self.N)
        pre_order = []
        post_order = []
        algorithm = DFSWithDepthTracker(self.G)
        algorithm.run(5,
            pre_action=lambda pair: pre_order.append(pair),
            post_action=lambda pair: post_order.append(pair))
        pre_order.sort(key=lambda pair: (pair[1], pair[0]))
        post_order.sort(key=lambda pair: (pair[1], pair[0]))
        pre_order_expected = [(5, 0), (1, 1), (2, 1), (0, 2), (6, 2), (3, 3), (4, 3), (7, 4)]
        post_order_expected = [(5, 0), (1, 1), (2, 1), (0, 2), (6, 2), (3, 3), (4, 3), (7, 4)]
        self.assertEqual(pre_order, pre_order_expected)
        self.assertEqual(post_order, post_order_expected)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
