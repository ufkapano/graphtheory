#!/usr/bin/python

import unittest
from edges import Edge
from graphs import Graph
from bfs import BFSWithQueue, SimpleBFS

# 0---1   2---3
# |   | / | / |
# 4   5---6---7

class TestBFS(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = [0, 1, 2, 3, 4, 5, 6, 7]
        self.edges = [
            Edge(0, 4, 2), Edge(0, 1, 3), Edge(1, 5, 4), Edge(5, 2, 5),
            Edge(5, 6, 6), Edge(2, 6, 7), Edge(2, 3, 8), Edge(6, 3, 9),
            Edge(6, 7, 10), Edge(3, 7, 11)]
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
        distance_expected = {0: 1, 1: 0, 2: 2, 3: 3, 4: 2, 5: 1, 6: 2, 7: 3}
        self.assertEqual(algorithm.distance, distance_expected)
        parent_expected = {0: 1, 1: None, 2: 5, 3: 2, 4: 0, 5: 1, 6: 5, 7: 6}
        self.assertEqual(algorithm.parent, parent_expected)
        self.assertEqual(algorithm.path(1, 7), [1, 5, 6, 7])
        self.assertEqual(algorithm.path(1, 4), [1, 0, 4])
        self.assertRaises(ValueError, algorithm.path, 4, 7)
        #algorithm.dag.show()
        self.assertEqual(algorithm.dag.v(), self.N)
        self.assertEqual(algorithm.dag.e(), self.N-1)
        self.assertTrue(algorithm.dag.is_directed())
        for edge in algorithm.dag.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

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
        self.assertEqual(algorithm.path(1, 7), [1, 5, 6, 7])
        self.assertEqual(algorithm.path(1, 4), [1, 0, 4])
        self.assertRaises(ValueError, algorithm.path, 4, 7)
        #algorithm.dag.show()
        self.assertEqual(algorithm.dag.v(), self.N)
        self.assertEqual(algorithm.dag.e(), self.N-1)
        self.assertTrue(algorithm.dag.is_directed())
        for edge in algorithm.dag.iteredges():
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(edge.weight, self.G.weight(edge))

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBFS)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
