#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.wheels import is_wheel


class TestGraphFactory(unittest.TestCase):

    def setUp(self):
        self.N = 10           # number of nodes
        self.graph_factory = GraphFactory(Graph)

    def test_complete(self):
        G = self.graph_factory.make_complete(n=self.N, directed=False)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N * (self.N-1) // 2)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))

    def test_complete_directed(self):
        G = self.graph_factory.make_complete(n=self.N, directed=True)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N * (self.N-1) // 2)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))

    def test_path(self):
        G = self.graph_factory.make_path(n=self.N, directed=False)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N-1)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))
        self.assertEqual(aset, set(range(1, self.N)))

    def test_cyclic(self):
        G = self.graph_factory.make_cyclic(n=self.N, directed=False)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))
        with self.assertRaises(ValueError):
            self.graph_factory.make_cyclic(n=1)
        with self.assertRaises(ValueError):
            self.graph_factory.make_cyclic(n=2)

    def test_cyclic_directed(self):
        G = self.graph_factory.make_cyclic(n=self.N, directed=True)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))
        with self.assertRaises(ValueError):
            self.graph_factory.make_cyclic(n=1)
        with self.assertRaises(ValueError):
            self.graph_factory.make_cyclic(n=2)

    def test_sparse(self):
        m_edges = 2 * self.N
        G = self.graph_factory.make_sparse(n=self.N, directed=False, m=m_edges)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), m_edges)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))

    def test_tree(self):
        G = self.graph_factory.make_tree(n=self.N)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N-1)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))

    def test_connected(self):
        m_edges = 2 * self.N
        G = self.graph_factory.make_connected(n=self.N, m=m_edges)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), m_edges)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))

    def test_random(self):
        G = self.graph_factory.make_random(
            n=self.N, directed=False, edge_probability=0.1)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))

    def test_random_directed(self):
        G = self.graph_factory.make_random(
            n=self.N, directed=True, edge_probability=0.1)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))

    def test_bipartite(self):
        N1, N2 = 5, 6
        G = self.graph_factory.make_bipartite(n1=N1, n2=N2,
            directed=False, edge_probability=0.1)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), N1 + N2)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))
        # We use the fact that nodes are in two sets
        # [0 ... N1-1], [N1 ... N1+N2-1].
        for edge in G.iteredges():
            self.assertEqual(edge.source < N1, edge.target >= N1)

    def test_grid(self):
        s = 4
        G = self.graph_factory.make_grid(size=s)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), s * s)
        self.assertEqual(G.e(), 2 * s * (s-1))
        with self.assertRaises(ValueError):
            self.graph_factory.make_grid(size=2)

    def test_grid_periodic(self):
        s = 4
        G = self.graph_factory.make_grid_periodic(size=s)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), s * s)
        self.assertEqual(G.e(), 2 * s * s)
        with self.assertRaises(ValueError):
            self.graph_factory.make_grid_periodic(size=2)

    def test_triangle(self):
        s = 4
        G = self.graph_factory.make_triangle(size=s)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), s * s)
        self.assertEqual(G.e(), 3 * s * s -4 * s + 1)
        with self.assertRaises(ValueError):
            self.graph_factory.make_triangle(size=2)

    def test_triangle_periodic(self):
        s = 4
        G = self.graph_factory.make_triangle_periodic(size=s)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), s * s)
        self.assertEqual(G.e(), 3 * s * s)
        with self.assertRaises(ValueError):
            self.graph_factory.make_triangle_periodic(size=2)

    def test_ladder(self):
        s = 4
        G = self.graph_factory.make_ladder(size=s)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), 2 * s)
        self.assertEqual(G.e(), 3 * s -2)
        with self.assertRaises(ValueError):
            self.graph_factory.make_ladder(size=2)

    def test_prism(self):
        s = 4
        G = self.graph_factory.make_prism(size=s)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), 2 * s)
        self.assertEqual(G.e(), 3 * s)
        with self.assertRaises(ValueError):
            self.graph_factory.make_prism(size=2)

    def test_antiprism(self):
        s = 4
        G = self.graph_factory.make_antiprism(size=s)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), 2 * s)
        self.assertEqual(G.e(), 4 * s)
        with self.assertRaises(ValueError):
            self.graph_factory.make_antiprism(size=2)

    def test_flow_network(self):
        G = self.graph_factory.make_flow_network(n=self.N)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertTrue(G.e() > self.N - 2)

    def test_necklace(self):
        G = self.graph_factory.make_necklace(n=self.N, directed=False)
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), 3 * self.N // 2)
        with self.assertRaises(ValueError):
            self.graph_factory.make_necklace(n=1)
        with self.assertRaises(ValueError):
            self.graph_factory.make_necklace(n=2)
        with self.assertRaises(ValueError):
            self.graph_factory.make_necklace(n=3)
        with self.assertRaises(ValueError):
            self.graph_factory.make_necklace(n=5)

    def test_wheel(self):
        G = self.graph_factory.make_wheel(n=self.N, directed=False)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), 2 * self.N - 2)
        self.assertTrue(is_wheel(G))
        with self.assertRaises(ValueError):
            self.graph_factory.make_wheel(n=1)
        with self.assertRaises(ValueError):
            self.graph_factory.make_wheel(n=2)
        with self.assertRaises(ValueError):
            self.graph_factory.make_wheel(n=3)

    def test_fake_wheel(self):
        G = self.graph_factory.make_fake_wheel(n=self.N, directed=False)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), 2 * self.N - 2)
        self.assertFalse(is_wheel(G))
        with self.assertRaises(ValueError):
            self.graph_factory.make_fake_wheel(n=1)
        with self.assertRaises(ValueError):
            self.graph_factory.make_fake_wheel(n=2)
        with self.assertRaises(ValueError):
            self.graph_factory.make_fake_wheel(n=3)
        with self.assertRaises(ValueError):
            self.graph_factory.make_fake_wheel(n=4)
        with self.assertRaises(ValueError):
            self.graph_factory.make_fake_wheel(n=5)
        with self.assertRaises(ValueError):
            self.graph_factory.make_fake_wheel(n=6)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
