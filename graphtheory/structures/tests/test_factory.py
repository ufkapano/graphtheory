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

    def test_cyclic(self):
        G = self.graph_factory.make_cyclic(n=self.N, directed=False)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))
        self.assertRaises(ValueError, self.graph_factory.make_cyclic, 1)
        self.assertRaises(ValueError, self.graph_factory.make_cyclic, 2)

    def test_cyclic_directed(self):
        G = self.graph_factory.make_cyclic(n=self.N, directed=True)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))
        self.assertRaises(ValueError, self.graph_factory.make_cyclic, 1)
        self.assertRaises(ValueError, self.graph_factory.make_cyclic, 2)

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
        G = self.graph_factory.make_bipartite(N1, N2, directed=False, edge_probability=0.1)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), N1 + N2)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))
        # We use the fact that nodes are in two sets
        # [0 ... N1-1], [N1 ... N1+N2-1].
        for edge in G.iteredges():
            self.assertEqual(edge.source < N1, edge.target >= N1)

    def test_grid(self):
        size = 4
        G = self.graph_factory.make_grid(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), size * size)
        self.assertEqual(G.e(), 2 * size * (size-1))
        self.assertRaises(ValueError, self.graph_factory.make_grid, 2)

    def test_grid_periodic(self):
        size = 4
        G = self.graph_factory.make_grid_periodic(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), size * size)
        self.assertEqual(G.e(), 2 * size * size)
        self.assertRaises(
            ValueError, self.graph_factory.make_grid_periodic, 2)

    def test_triangle(self):
        size = 4
        G = self.graph_factory.make_triangle(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), size * size)
        self.assertEqual(G.e(), 3 * size * size -4 * size + 1)
        self.assertRaises(ValueError, self.graph_factory.make_triangle, 2)

    def test_triangle_periodic(self):
        size = 4
        G = self.graph_factory.make_triangle_periodic(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), size * size)
        self.assertEqual(G.e(), 3 * size * size)
        self.assertRaises(
            ValueError, self.graph_factory.make_triangle_periodic, 2)

    def test_ladder(self):
        size = 4
        G = self.graph_factory.make_ladder(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), 2 * size)
        self.assertEqual(G.e(), 3 * size -2)
        self.assertRaises(ValueError, self.graph_factory.make_ladder, 2)

    def test_prism(self):
        size = 4
        G = self.graph_factory.make_prism(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), 2 * size)
        self.assertEqual(G.e(), 3 * size)
        self.assertRaises(
            ValueError, self.graph_factory.make_prism, 2)

    def test_antiprism(self):
        size = 4
        G = self.graph_factory.make_antiprism(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), 2 * size)
        self.assertEqual(G.e(), 4 * size)
        self.assertRaises(
            ValueError, self.graph_factory.make_antiprism, 2)

    def test_flow_network(self):
        G = self.graph_factory.make_flow_network(self.N)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertTrue(G.e() > self.N - 2)

    def test_necklace(self):
        G = self.graph_factory.make_necklace(n=self.N, directed=False)
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), 3 * self.N // 2)
        self.assertRaises(ValueError, self.graph_factory.make_necklace, 1)
        self.assertRaises(ValueError, self.graph_factory.make_necklace, 2)
        self.assertRaises(ValueError, self.graph_factory.make_necklace, 3)
        self.assertRaises(ValueError, self.graph_factory.make_necklace, 5)
        #G = self.graph_factory.make_necklace(n=6, directed=False)
        #G.show()

    def test_wheel(self):
        G = self.graph_factory.make_wheel(n=self.N, directed=False)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), 2 * self.N - 2)
        self.assertTrue(is_wheel(G))
        self.assertRaises(ValueError, self.graph_factory.make_wheel, 1)
        self.assertRaises(ValueError, self.graph_factory.make_wheel, 2)
        self.assertRaises(ValueError, self.graph_factory.make_wheel, 3)

    def test_fake_wheel(self):
        G = self.graph_factory.make_fake_wheel(n=self.N, directed=False)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), 2 * self.N - 2)
        self.assertFalse(is_wheel(G))
        self.assertRaises(ValueError, self.graph_factory.make_fake_wheel, 1)
        self.assertRaises(ValueError, self.graph_factory.make_fake_wheel, 2)
        self.assertRaises(ValueError, self.graph_factory.make_fake_wheel, 3)
        self.assertRaises(ValueError, self.graph_factory.make_fake_wheel, 4)
        self.assertRaises(ValueError, self.graph_factory.make_fake_wheel, 5)
        self.assertRaises(ValueError, self.graph_factory.make_fake_wheel, 6)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
