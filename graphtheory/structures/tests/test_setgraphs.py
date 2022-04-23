#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.setgraphs import Graph

# A --o B
# o   / o
# |  /  |
# | o   |
# C --o D

class TestGraphDirected(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["A", "B", "C", "D"]
        self.edges = [
            Edge("A", "B"), Edge("B", "C"), Edge("C", "A"), 
            Edge("C", "D"), Edge("D", "B")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_directed(self):
        self.assertTrue(self.G.is_directed())
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), 5)
        self.G.del_node("B")
        self.assertEqual(self.G.v(), 3)
        self.assertEqual(self.G.e(), 2)
        self.assertTrue(self.G.has_edge(("C", "A")))
        self.assertEqual(self.G.weight(("C", "A")), 1)
        self.G.del_edge(("C", "A"))
        self.assertFalse(self.G.has_edge(("C", "A")))

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
        T.add_edge(Edge("A", "B"))
        T.add_edge(Edge("B", "C"))
        T.add_edge(Edge("C", "A"))
        T.add_edge(Edge("C", "D"))
        self.assertFalse(T == self.G, "edge numbers are different")
        T.add_edge(Edge("B", "D"))
        self.assertFalse(T == self.G, "edge directions are different")
        T.del_edge(Edge("B", "D"))
        T.add_edge(Edge("D", "B"))
        #self.G.show()
        #T.show()
        self.assertTrue(T == self.G, "graphs are the same")

    def test_iteredges(self):
        inedges_B = list(self.G.iterinedges("B"))
        outedges_B = list(self.G.iteroutedges("B"))
        #print inedges_B, outedges_B
        self.assertEqual(len(inedges_B), 2)
        self.assertEqual(len(outedges_B), 1)

    def test_copy(self):
        T = self.G.copy()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertTrue(self.G.has_edge(edge))

    def test_transpose(self):
        T = self.G.transpose()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertTrue(self.G.has_edge(~edge))

    def test_complement(self):
        T = self.G.complement()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.N*(self.N-1) - self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertFalse(self.G.has_edge(edge))
        for edge in self.G.iteredges():
            self.assertFalse(T.has_edge(edge))

    def test_add_graph_directed(self):
        T = Graph(self.N, directed=True)
        for node in self.nodes:
            T.add_node(node)
        T.add_edge(Edge("A", "D"))
        self.assertEqual(T.v(), self.N)
        self.assertEqual(T.e(), 1)
        self.G.add_graph(T)
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), 6)

    def test_degree(self):
        self.assertEqual(self.G.indegree("A"), 1)
        self.assertEqual(self.G.indegree("B"), 2)
        self.assertEqual(self.G.indegree("C"), 1)
        self.assertEqual(self.G.indegree("D"), 1)
        self.assertEqual(self.G.outdegree("A"), 1)
        self.assertEqual(self.G.outdegree("B"), 1)
        self.assertEqual(self.G.outdegree("C"), 2)
        self.assertEqual(self.G.outdegree("D"), 1)

    def test_exceptions(self):
        self.assertRaises(ValueError, self.G.add_edge, Edge("A", "A"))
        self.assertRaises(ValueError, self.G.add_edge, Edge("A", "B"))
        self.assertRaises(ValueError, self.G.degree, "A")

    def tearDown(self): pass

# A --- B
# |  /  |
# | /   |
# C --- D

class TestGraphUndirected(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N)
        self.nodes = ["A", "B", "C", "D"]
        self.edges = [
            Edge("A", "B"), Edge("B", "C"), Edge("C", "A"), 
            Edge("C", "D"), Edge("D", "B")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_undirected(self):
        self.assertFalse(self.G.is_directed())
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), 5)
        self.G.del_node("B")
        self.assertEqual(self.G.v(), 3)
        self.assertEqual(self.G.e(), 2)
        self.assertTrue(self.G.has_edge(("C", "A")))
        self.assertEqual(self.G.weight(("C", "A")), 1)
        self.G.del_edge(("C", "A"))
        self.assertFalse(self.G.has_edge(("C", "A")))

    def test_iteredges(self):
        inedges_B = list(self.G.iterinedges("B"))
        outedges_B = list(self.G.iteroutedges("B"))
        #print inedges_B, outedges_B
        self.assertEqual(len(inedges_B), 3)
        self.assertEqual(len(outedges_B), 3)

    def test_copy(self):
        T = self.G.copy()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertTrue(self.G.has_edge(edge))

    def test_transpose(self):
        T = self.G.transpose()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertTrue(self.G.has_edge(~edge))

    def test_complement(self):
        T = self.G.complement()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.N*(self.N-1) // 2 - self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertFalse(self.G.has_edge(edge))
        for edge in self.G.iteredges():
            self.assertFalse(T.has_edge(edge))

    def test_degree(self):
        self.assertEqual(self.G.degree("A"), 2)
        self.assertEqual(self.G.degree("B"), 3)
        self.assertEqual(self.G.degree("C"), 3)
        self.assertEqual(self.G.degree("D"), 2)

    def test_add_graph_undirected(self):
        T = Graph(self.N)
        for node in self.nodes:
            T.add_node(node)
        T.add_edge(Edge("A", "D"))
        self.assertEqual(T.v(), self.N)
        self.assertEqual(T.e(), 1)
        self.G.add_graph(T)
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), 6)

    def tearDown(self): pass

# 0-2-4-6
# | | | |  ladder
# 1-3-5-7

class TestGraphLadder(unittest.TestCase):

    def setUp(self):
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.edges = [
            Edge(0, 1), Edge(0, 2), Edge(2, 3), Edge(1, 3), 
            Edge(2, 4), Edge(3, 5), Edge(4, 6), Edge(4, 5), 
            Edge(5, 7), Edge(6, 7)]
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_basic(self):
        self.assertFalse(self.G.is_directed())
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), len(self.edges))

    def test_edges(self):
        for edge in self.edges:
            self.assertTrue(self.G.has_edge(edge))
            self.assertEqual(self.G.weight(edge), edge.weight)
        self.assertFalse(self.G.has_edge(Edge(0, 3)))
        self.assertEqual(self.G.weight(Edge(0, 3)), 0)  # no edge

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

    unittest.main()

# EOF
