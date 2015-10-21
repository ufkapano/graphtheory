#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.spanningtrees.boruvka import BoruvkaMST


class TestBoruvka(unittest.TestCase):

    def setUp(self):
        # The graph (unique weights) from
        # http://en.wikipedia.org/wiki/Boruvka's_algorithm
        self.N = 7           # number of nodes
        self.G = Graph(self.N)
        self.nodes = [0, 1, 2, 3, 4, 5, 6]
        self.edges = [
            Edge(0, 1, 7), Edge(1, 2, 11), Edge(0, 3, 4), Edge(3, 1, 9), 
            Edge(4, 1, 10), Edge(2, 4, 5), Edge(3, 4, 15), Edge(3, 5, 6), 
            Edge(5, 4, 12), Edge(5, 6, 13), Edge(4, 6, 8)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G

    def test_mst_wiki(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = BoruvkaMST(self.G)
        algorithm.run()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 7), Edge(0, 3, 4), Edge(2, 4, 5), Edge(1, 4, 10), 
            Edge(4, 6, 8), Edge(3, 5, 6)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))

    def tearDown(self): pass


class TestBoruvkaCormen(unittest.TestCase):

    def setUp(self):
        # The modified graph (unique weights) from Cormen.
        self.N = 9           # number of nodes
        self.G = Graph(self.N)
        self.nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.edges = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(1, 7, 11), Edge(1, 2, 12), 
            Edge(7, 8, 7), Edge(8, 2, 2), Edge(8, 6, 6), Edge(7, 6, 1),
            Edge(2, 3, 13), Edge(2, 5, 5), Edge(6, 5, 3), Edge(3, 5, 14), 
            Edge(3, 4, 9), Edge(5, 4, 10)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G

    def test_mst_cormen(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = BoruvkaMST(self.G)
        algorithm.run()
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


class TestBoruvkaDisconnectedGraph(unittest.TestCase):

    def setUp(self):
        # The modified graph (unique weights) from Cormen.
        self.N = 9           # number of nodes
        self.G = Graph(self.N)
        self.nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.edges = [
            Edge(0, 1, 4), Edge(0, 7, 8), Edge(1, 7, 11), Edge(1, 2, 12), 
            Edge(7, 8, 7), Edge(8, 2, 2), Edge(8, 6, 6), Edge(7, 6, 1),
            Edge(3, 5, 14), Edge(3, 4, 9), Edge(5, 4, 10)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G

    def test_mst_disconnected(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = BoruvkaMST(self.G)
        algorithm.run()
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

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBoruvka)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestBoruvkaCormen)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestBoruvkaDisconnectedGraph)
    suite = unittest.TestSuite([suite1, suite2, suite3])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
