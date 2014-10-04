#!/usr/bin/python

from edges import Edge
from graphs import Graph
from bfsfast import BFSWithQueue, SimpleBFS
import unittest

# 0---1   2---3
# |   | / | / |
# 4   5---6---7

class TestBFS(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = [0, 1, 2, 3, 4, 5, 6, 7]
        self.edges = [Edge(0, 4), Edge(0, 1), 
        Edge(1, 5), Edge(5, 2), Edge(5, 6), Edge(2, 6),
        Edge(2, 3), Edge(6, 3), Edge(6, 7), Edge(3, 7)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_bfs(self):
        self.assertEqual(self.G.v(), self.N)
        pre_ordering = []
        post_ordering = []
        algorithm = BFSWithQueue(self.G)
        algorithm.run(1, pre_action=lambda node: pre_ordering.append(node),
        post_action=lambda node: post_ordering.append(node))
        ordering_expected = [1, 0, 5, 4, 2, 6, 3, 7]
        self.assertEqual(pre_ordering, ordering_expected)
        self.assertEqual(post_ordering, ordering_expected)
        distance_expected = dict([(1, 0), (0, 1), (5, 1), 
        (2, 2), (4, 2), (6, 2), (3, 3), (7, 3)])
        self.assertEqual(algorithm.distance, distance_expected)
        parent_expected = {0: 1, 1: None, 2: 5, 3: 2, 4: 0, 5: 1, 6: 5, 7: 6}
        self.assertEqual(algorithm.parent, parent_expected)

    def test_simple_bfs(self):
        self.assertEqual(self.G.v(), self.N)
        pre_ordering = []
        post_ordering = []
        algorithm = SimpleBFS(self.G)
        algorithm.run(1, pre_action=lambda node: pre_ordering.append(node),
        post_action=lambda node: post_ordering.append(node))
        ordering_expected = [1, 0, 5, 4, 2, 6, 3, 7]
        self.assertEqual(pre_ordering, ordering_expected)
        self.assertEqual(post_ordering, ordering_expected)
        parent_expected = {0: 1, 1: None, 2: 5, 3: 2, 4: 0, 5: 1, 6: 5, 7: 6}
        self.assertEqual(algorithm.parent, parent_expected)

    def test_to_tree(self):
        algorithm = BFSWithQueue(self.G)
        algorithm.run(1)
        tree = algorithm.to_tree()
        self.assertFalse(tree.is_directed())
        self.assertEqual(tree.v(), self.N)
        self.assertEqual(tree.e(), self.N-1)

    def test_to_dag(self):
        algorithm = BFSWithQueue(self.G)
        algorithm.run(1)
        dag = algorithm.to_dag()
        self.assertTrue(dag.is_directed())
        self.assertEqual(dag.v(), self.N)
        self.assertEqual(dag.e(), self.N-1)

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBFS)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
