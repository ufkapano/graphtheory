#!/usr/bin/python
#
# test_graphs.py
#
# Tests for graphs.

import unittest
from edges import Edge
from graphs import Graph

# A --> B
# ^  /  ^
# | /.  |
# C --> D

class TestGraphDirected(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.edges = [Edge("A", "B", 2), Edge("B", "C", 4), Edge("C", "A", 6),
                      Edge("C", "D", 3), Edge("D", "B", 5)]
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_directed(self):
        self.assertTrue(self.G.is_directed())
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), 5)
        self.G.del_node("B")
        self.assertEqual(self.G.v(), 3)
        self.assertEqual(self.G.e(), 2)

    def test_cmp(self):
        T = Graph(self.N)
        self.assertFalse(T == self.G, "directed and undirected graphs")
        T = Graph(self.N, directed=True)
        for node in ["A", "B", "C", "X"]:
            T.add_node(node)
        self.assertFalse(T == self.G, "nodes are different")
        T.del_node("X")
        self.assertFalse(T == self.G, "numbers of nodes are different")
        T.add_node("D")
        T.add_edge(Edge("A", "B", 2))
        T.add_edge(Edge("B", "C", 4))
        T.add_edge(Edge("C", "A", 6))
        T.add_edge(Edge("C", "D", 3))
        self.assertFalse(T == self.G, "edge numbers are different")
        T.add_edge(Edge("D", "B", 7))
        self.assertFalse(T == self.G, "edge weights are different")
        T.del_edge(Edge("D", "B", 7))
        T.add_edge(Edge("B", "D", 5))
        self.assertFalse(T == self.G, "edge directions are different")
        T.del_edge(Edge("B", "D", 5))
        T.add_edge(Edge("D", "B", 5))
        self.assertTrue(T == self.G, "graphs are the same")

    def tearDown(self): pass


class TestGraphUndirected(unittest.TestCase):

    def setUp(self): pass

    def test_undirected(self): pass

    def tearDown(self): pass


# 0-2-4-6  graf nieskierowany z wagami
# | | | |  drabina
# 1-3-5-7

class TestGraphLadder(unittest.TestCase):

    def setUp(self):
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.edges = [Edge(0, 1, 2), Edge(0, 2, 1), Edge(2, 3, 5),
                      Edge(1, 3, 3), Edge(2, 4, 4), Edge(3, 5, 6), Edge(4, 6, 7),
                      Edge(4, 5, 8), Edge(5, 7, 9), Edge(6, 7, 10)]
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_basic(self):
        self.assertFalse(self.G.is_directed())
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), len(self.edges))

    def test_edges(self):
        for edge in self.edges:
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(self.G.weight(edge.source, edge.target), edge.weight)
        self.assertFalse(self.G.has_edge(Edge(0, 3)))
        self.assertEqual(self.G.weight(0, 3), 0)  # no edge

    def test_del(self):
        self.assertEqual(self.G.e(), 10)
        self.G.del_node(7)
        self.assertEqual(self.G.e(), 8)
        self.G.del_node(2)
        self.assertEqual(self.G.e(), 5)

    def test_adjacent(self):
        for node in self.G.iteradjacent(0):
            self.assertTrue(node in [1, 2])
        for node in self.G.iteradjacent(2):
            self.assertTrue(node in [0, 3, 4])

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestGraphDirected)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestGraphUndirected)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestGraphLadder)
    suite = unittest.TestSuite([suite1, suite2, suite3])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
