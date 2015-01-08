#!/usr/bin/python

import unittest
from edges import Edge
from graphs import Graph
from dfs import *

# 0---1   2---3
# |   | / | / |
# 4   5---6---7

class TestDFS(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = [0, 1, 2, 3, 4, 5, 6, 7]
        self.edges = [Edge(0, 4, 2), Edge(0, 1, 3), 
        Edge(1, 5, 4), Edge(5, 2, 5), Edge(5, 6, 6), Edge(2, 6, 7),
        Edge(2, 3, 8), Edge(6, 3, 9), Edge(6, 7, 10), Edge(3, 7, 11)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        print self.G
        #self.G.show()

    def test_dfs_with_stack(self):
        self.assertEqual(self.G.v(), self.N)
        pre_ordering = []
        post_ordering = []
        algorithm = DFSWithStack(self.G)
        algorithm.run(1, pre_action=lambda node: pre_ordering.append(node),
            post_action=lambda node: post_ordering.append(node))
        pre_ordering_expected = [1, 0, 5, 2, 6, 3, 7, 4]
        post_ordering_expected = [1, 5, 6, 7, 3, 2, 0, 4]
        self.assertEqual(pre_ordering, pre_ordering_expected)
        self.assertEqual(post_ordering, post_ordering_expected)
        dd_expected = {0: 2, 1: 1, 2: 5, 3: 8, 4: 14, 5: 3, 6: 6, 7: 9}
        ff_expected = {0: 15, 1: 4, 2: 13, 3: 12, 4: 16, 5: 7, 6: 10, 7: 11}
        self.assertEqual(algorithm.dd, dd_expected)
        self.assertEqual(algorithm.ff, ff_expected)
        parent_expected = {0: 1, 1: None, 2: 5, 3: 6, 4: 0, 5: 1, 6: 5, 7: 6}
        self.assertEqual(algorithm.parent, parent_expected)

    def test_dfs_with_recursion(self):
        self.assertEqual(self.G.v(), self.N)
        pre_ordering = []
        post_ordering = []
        algorithm = DFSWithRecursion(self.G)
        algorithm.run(1, pre_action=lambda node: pre_ordering.append(node),
            post_action=lambda node: post_ordering.append(node))
        pre_ordering_expected = [1, 0, 4, 5, 2, 3, 6, 7]
        post_ordering_expected = [4, 0, 7, 6, 3, 2, 5, 1]
        self.assertEqual(pre_ordering, pre_ordering_expected)
        self.assertEqual(post_ordering, post_ordering_expected)
        dd_expected = {0: 2, 1: 1, 2: 7, 3: 8, 4: 3, 5: 6, 6: 9, 7: 10}
        ff_expected = {0: 5, 1: 16, 2: 14, 3: 13, 4: 4, 5: 15, 6: 12, 7: 11}
        self.assertEqual(algorithm.dd, dd_expected)
        self.assertEqual(algorithm.ff, ff_expected)
        parent_expected = {0: 1, 1: None, 2: 5, 3: 2, 4: 0, 5: 1, 6: 3, 7: 6}
        self.assertEqual(algorithm.parent, parent_expected)

    def test_simple_dfs_with_recursion(self):
        self.assertEqual(self.G.v(), self.N)
        pre_ordering = []
        post_ordering = []
        algorithm = SimpleDFS(self.G)
        algorithm.run(1, pre_action=lambda node: pre_ordering.append(node),
            post_action=lambda node: post_ordering.append(node))
        pre_ordering_expected = [1, 0, 4, 5, 2, 3, 6, 7]
        post_ordering_expected = [4, 0, 7, 6, 3, 2, 5, 1]
        self.assertEqual(pre_ordering, pre_ordering_expected)
        self.assertEqual(post_ordering, post_ordering_expected)
        parent_expected = {0: 1, 1: None, 2: 5, 3: 2, 4: 0, 5: 1, 6: 3, 7: 6}
        self.assertEqual(algorithm.parent, parent_expected)

    def test_to_tree_stack(self):
        algorithm = DFSWithStack(self.G)
        algorithm.run(1)
        tree = algorithm.to_tree()
        self.assertFalse(tree.is_directed())
        self.assertEqual(tree.v(), self.N)
        self.assertEqual(tree.e(), self.N-1)
        for edge in tree.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def test_to_tree_recursion(self):
        algorithm = DFSWithRecursion(self.G)
        algorithm.run(1)
        tree = algorithm.to_tree()
        self.assertFalse(tree.is_directed())
        self.assertEqual(tree.v(), self.N)
        self.assertEqual(tree.e(), self.N-1)
        for edge in tree.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def test_to_tree_simple(self):
        algorithm = SimpleDFS(self.G)
        algorithm.run(1)
        tree = algorithm.to_tree()
        self.assertFalse(tree.is_directed())
        self.assertEqual(tree.v(), self.N)
        self.assertEqual(tree.e(), self.N-1)
        for edge in tree.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def test_to_dag_stack(self):
        algorithm = DFSWithStack(self.G)
        algorithm.run(1)
        dag = algorithm.to_dag()
        self.assertTrue(dag.is_directed())
        self.assertEqual(dag.v(), self.N)
        self.assertEqual(dag.e(), self.N-1)
        for edge in dag.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def test_to_dag_recursion(self):
        algorithm = DFSWithRecursion(self.G)
        algorithm.run(1)
        dag = algorithm.to_dag()
        self.assertTrue(dag.is_directed())
        self.assertEqual(dag.v(), self.N)
        self.assertEqual(dag.e(), self.N-1)
        for edge in dag.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def test_to_dag_simple(self):
        algorithm = SimpleDFS(self.G)
        algorithm.run(1)
        dag = algorithm.to_dag()
        self.assertTrue(dag.is_directed())
        self.assertEqual(dag.v(), self.N)
        self.assertEqual(dag.e(), self.N-1)
        for edge in dag.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestDFS)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
