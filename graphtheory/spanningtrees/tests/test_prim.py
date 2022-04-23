#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.spanningtrees.prim import PrimMST
from graphtheory.spanningtrees.prim import PrimMSTWithEdges
from graphtheory.spanningtrees.prim import PrimMatrixMST
from graphtheory.spanningtrees.prim import PrimMatrixMSTWithEdges
from graphtheory.spanningtrees.prim import PrimConnectedMST
from graphtheory.spanningtrees.prim import PrimTrivialMST


class TestPrim(unittest.TestCase):

    def setUp(self):
        # The graph (unique weights) from
        # http://en.wikipedia.org/wiki/Boruvka's_algorithm
        self.N = 7           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1, 7), Edge(1, 2, 11), Edge(0, 3, 4),
            Edge(3, 1, 9), Edge(4, 1, 10), Edge(2, 4, 5), Edge(3, 4, 15),
            Edge(3, 5, 6), Edge(5, 4, 12), Edge(5, 6, 13), Edge(4, 6, 8)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_prim(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 7), Edge(0, 3, 4), Edge(2, 4, 5), 
            Edge(1, 4, 10), Edge(4, 6, 8), Edge(3, 5, 6)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_with_edges(self):
        algorithm = PrimMSTWithEdges(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 7), Edge(0, 3, 4), Edge(2, 4, 5), 
            Edge(1, 4, 10), Edge(4, 6, 8), Edge(3, 5, 6)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_matrix(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimMatrixMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 7), Edge(0, 3, 4), Edge(2, 4, 5), 
            Edge(1, 4, 10), Edge(4, 6, 8), Edge(3, 5, 6)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_matrix_with_edges(self):
        algorithm = PrimMatrixMSTWithEdges(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 7), Edge(0, 3, 4), Edge(2, 4, 5), 
            Edge(1, 4, 10), Edge(4, 6, 8), Edge(3, 5, 6)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_connected(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimConnectedMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 7), Edge(0, 3, 4), Edge(2, 4, 5), 
            Edge(1, 4, 10), Edge(4, 6, 8), Edge(3, 5, 6)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_trivial(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimTrivialMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 7), Edge(0, 3, 4), Edge(2, 4, 5), 
            Edge(1, 4, 10), Edge(4, 6, 8), Edge(3, 5, 6)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def tearDown(self): pass


class TestPrimCormen(unittest.TestCase):

    def setUp(self):
        # The modified graph (unique weights) from Cormen.
        self.N = 9           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(1, 7, 11), Edge(1, 2, 12), 
            Edge(7, 8, 7), Edge(8, 2, 2), Edge(8, 6, 6), Edge(7, 6, 1),
            Edge(2, 3, 13), Edge(2, 5, 5), Edge(6, 5, 3),
            Edge(3, 5, 14), Edge(3, 4, 9), Edge(5, 4, 10)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G

    def test_prim(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 42
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(8, 2, 2), Edge(7, 6, 1), 
            Edge(2, 5, 5), Edge(6, 5, 3), Edge(3, 4, 9), Edge(5, 4, 10)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_with_edges(self):
        algorithm = PrimMSTWithEdges(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 42
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(8, 2, 2), Edge(7, 6, 1), 
            Edge(2, 5, 5), Edge(6, 5, 3), Edge(3, 4, 9), Edge(5, 4, 10)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_matrix(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimMatrixMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 42
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(8, 2, 2), Edge(7, 6, 1), 
            Edge(2, 5, 5), Edge(6, 5, 3), Edge(3, 4, 9), Edge(5, 4, 10)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_matrix_with_edges(self):
        algorithm = PrimMatrixMSTWithEdges(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 42
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(8, 2, 2), Edge(7, 6, 1), 
            Edge(2, 5, 5), Edge(6, 5, 3), Edge(3, 4, 9), Edge(5, 4, 10)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_connected(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimConnectedMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 42
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(8, 2, 2), Edge(7, 6, 1), 
            Edge(2, 5, 5), Edge(6, 5, 3), Edge(3, 4, 9), Edge(5, 4, 10)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_trivial(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimTrivialMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 42
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(8, 2, 2), Edge(7, 6, 1), 
            Edge(2, 5, 5), Edge(6, 5, 3), Edge(3, 4, 9), Edge(5, 4, 10)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def tearDown(self): pass


class TestPrimDisconnectedGraph(unittest.TestCase):

    def setUp(self):
        # The modified graph (unique weights) from Cormen.
        self.N = 9           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(1, 7, 11), Edge(1, 2, 12), 
            Edge(7, 8, 7), Edge(8, 2, 2), Edge(8, 6, 6), Edge(7, 6, 1),
            Edge(3, 5, 14), Edge(3, 4, 9), Edge(5, 4, 10)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G

    def test_prim(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-2) # 2 components
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(8, 2, 2), Edge(7, 6, 1), 
            Edge(6, 8, 6), Edge(3, 4, 9), Edge(5, 4, 10)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_with_edges(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimMSTWithEdges(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-2) # 2 components
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(8, 2, 2), Edge(7, 6, 1), 
            Edge(6, 8, 6), Edge(3, 4, 9), Edge(5, 4, 10)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_matrix(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = PrimMatrixMST(self.G)
        algorithm.run()
        algorithm.to_tree()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-2) # 2 components
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(8, 2, 2), Edge(7, 6, 1), 
            Edge(6, 8, 6), Edge(3, 4, 9), Edge(5, 4, 10)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def test_prim_connected(self):
        self.assertRaises(ValueError, PrimConnectedMST, self.G)

    def test_prim_trivial(self):
        self.assertRaises(ValueError, PrimTrivialMST, self.G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
