#!/usr/bin/python

import unittest
from edges import Edge
from graphs import Graph
#from matrixgraphs import Graph
from factory import GraphFactory


class TestGraphFactory(unittest.TestCase):

    def setUp(self):
        self.N = 10           # number of nodes
        self.graph_factory = GraphFactory(Graph)

    def test_complete(self):
        G = self.graph_factory.make_complete(n=self.N, directed=False)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N * (self.N-1) / 2)

    def test_sparse(self):
        m_edges = 2 * self.N
        G = self.graph_factory.make_sparse(n=self.N, directed=False, m=m_edges)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), m_edges)

    def test_tree(self):
        G = self.graph_factory.make_tree(n=self.N)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N-1)

    def test_connected(self):
        m_edges = 2 * self.N
        G = self.graph_factory.make_connected(n=self.N, m=m_edges)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), m_edges)

    def test_random(self):
        G = self.graph_factory.make_random(n=self.N, directed=True, edge_probability=0.1)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)

    def test_grid(self):
        size = 4
        G = self.graph_factory.make_grid(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), size * size)
        self.assertEqual(G.e(), 2 * size * size)
        self.assertRaises(ValueError, lambda: Graph.make_grid(2))

    def test_triangle(self):
        size = 4
        G = self.graph_factory.make_triangle(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), size * size)
        self.assertEqual(G.e(), 3 * size * size)
        self.assertRaises(ValueError, lambda: Graph.make_triangle(2))

    def test_ladder(self):
        size = 4
        G = self.graph_factory.make_ladder(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), 2 * size)
        self.assertEqual(G.e(), 3 * size)
        self.assertRaises(ValueError, lambda: Graph.make_ladder(2))

    def test_flow_network(self):
        G = self.graph_factory.make_flow_network(self.N)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertTrue(G.e() > self.N - 2)

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestGraphFactory)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
