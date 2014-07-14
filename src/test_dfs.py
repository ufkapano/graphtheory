#!/usr/bin/python
#
# test_dfs.py
#
# Tests for DFS.

from edges import Edge
from graphs import Graph
from dfs import DFSWithStack, DFSWithRecursion
import unittest

# r---s   t---u
# |   | / | / |
# v   w---x---y

class TestDFS(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = ["r", "s", "t", "u", "v", "w", "x", "y"]
        self.edges = [Edge("r", "v"), Edge("r", "s"), 
        Edge("s", "w"), Edge("w", "t"), Edge("w", "x"), Edge("t", "x"),
        Edge("t", "u"), Edge("x", "u"), Edge("x", "y"), Edge("u", "y")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_dfs_with_stack(self):
        self.assertEqual(self.G.v(), self.N)
        pre_ordering = []
        post_ordering = []
        algorithm = DFSWithStack(self.G)
        algorithm.run("s", pre_action=lambda node: pre_ordering.append(node),
            post_action=lambda node: post_ordering.append(node))
        pre_ordering_expected = ['s', 'r', 'w', 'x', 't', 'u', 'y', 'v']
        post_ordering_expected = ['s', 'w', 't', 'u', 'y', 'x', 'r', 'v']
        self.assertEqual(pre_ordering, pre_ordering_expected)
        self.assertEqual(post_ordering, post_ordering_expected)
        dd_expected = {'s': 1, 'r': 2, 'u': 8, 't': 6, 
        'w': 3, 'v': 14, 'y': 10, 'x': 5}
        ff_expected = {'s': 4, 'r': 15, 'u': 11, 't': 9, 
        'w': 7, 'v': 16, 'y': 12, 'x': 13}
        self.assertEqual(algorithm.dd, dd_expected)
        self.assertEqual(algorithm.ff, ff_expected)
        prev_expected = {'s': None, 'r': 's', 'u': 't', 't': 'w', 
        'w': 's', 'v': 'r', 'y': 'u', 'x': 'w'}
        # second possibility: 
        self.assertEqual(algorithm.prev, prev_expected)

    def test_dfs_with_recursion(self):
        self.assertEqual(self.G.v(), self.N)
        pre_ordering = []
        post_ordering = []
        algorithm = DFSWithRecursion(self.G)
        algorithm.run("s", pre_action=lambda node: pre_ordering.append(node),
            post_action=lambda node: post_ordering.append(node))
        pre_ordering_expected = ['s', 'r', 'v', 'w', 'x', 'y', 'u', 't']
        post_ordering_expected = ['v', 'r', 't', 'u', 'y', 'x', 'w', 's']
        self.assertEqual(pre_ordering, pre_ordering_expected)
        self.assertEqual(post_ordering, post_ordering_expected)
        dd_expected = {'s': 1, 'r': 2, 'u': 9, 't': 10, 
        'w': 6, 'v': 3, 'y': 8, 'x': 7}
        ff_expected = {'s': 16, 'r': 5, 'u': 12, 't': 11, 
        'w': 15, 'v': 4, 'y': 13, 'x': 14}
        self.assertEqual(algorithm.dd, dd_expected)
        self.assertEqual(algorithm.ff, ff_expected)
        prev_expected = {'s': None, 'r': 's', 'u': 'y', 't': 'u', 
        'w': 's', 'v': 'r', 'y': 'x', 'x': 'w'}
        # second possibility: 
        self.assertEqual(algorithm.prev, prev_expected)

    def test_to_tree_stack(self):
        algorithm = DFSWithStack(self.G)
        algorithm.run("s")
        tree = algorithm.to_tree()
        self.assertFalse(tree.is_directed())
        self.assertEqual(tree.v(), self.N)
        self.assertEqual(tree.e(), self.N-1)

    def test_to_tree_recursion(self):
        algorithm = DFSWithRecursion(self.G)
        algorithm.run("s")
        tree = algorithm.to_tree()
        self.assertFalse(tree.is_directed())
        self.assertEqual(tree.v(), self.N)
        self.assertEqual(tree.e(), self.N-1)

    def test_to_dag_stack(self):
        algorithm = DFSWithStack(self.G)
        algorithm.run("s")
        dag = algorithm.to_dag()
        self.assertTrue(dag.is_directed())
        self.assertEqual(dag.v(), self.N)
        self.assertEqual(dag.e(), self.N-1)

    def test_to_dag_recursion(self):
        algorithm = DFSWithRecursion(self.G)
        algorithm.run("s")
        dag = algorithm.to_dag()
        self.assertTrue(dag.is_directed())
        self.assertEqual(dag.v(), self.N)
        self.assertEqual(dag.e(), self.N-1)

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestDFS)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
