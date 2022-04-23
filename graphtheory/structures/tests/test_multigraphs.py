#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.multigraphs import MultiGraph

# o     o
# |     |
# 1 o-- 2-o
# o o
# |  \
# |   \
# 0 ==o 3

class TestMultiGraphDirected(unittest.TestCase):

    def setUp(self):
        self.N = 4   # number of nodes
        self.G = MultiGraph(self.N, directed=True)
        self.nodes = [0, 1, 2, 3]
        self.edges = [
            Edge(0, 1, 2), Edge(0, 3, 3), Edge(0, 3, 4), Edge(1, 1, 11), 
            Edge(3, 1, 31), Edge(2, 1, 21), Edge(2, 2, 220), Edge(2, 2, 221)]
        # 0-3 parallel edge
        # 1-1 loop
        # 2-2 parallel loop
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_basic(self):
        self.assertTrue(self.G.is_directed())
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), len(self.edges))
        self.assertRaises(ValueError, self.G.add_edge, Edge(0, 1, 2))
        #self.G.show()

    def test_weight(self):
        self.assertEqual(self.G.weight(Edge(3, 3)), 0)
        self.assertEqual(self.G.weight(Edge(1, 1)), 1)
        self.assertEqual(self.G.weight(Edge(2, 2)), 2)
        self.assertEqual(self.G.weight(Edge(3, 2)), 0)
        self.assertEqual(self.G.weight(Edge(2, 1)), 1)
        self.assertEqual(self.G.weight(Edge(0, 3)), 2)
        self.assertEqual(self.G.weight((0, 3)), 2)

    def test_del_edge(self):
        edge1 = Edge(2, 3, 23)
        self.G.add_edge(edge1)
        self.assertTrue(self.G.has_edge(edge1))
        self.assertTrue(self.G.has_edge((2, 3)))
        self.assertEqual(self.G.e(), len(self.edges) + 1)
        self.G.del_edge(edge1)
        self.assertEqual(self.G.e(), len(self.edges))
        edge2 = Edge(1, 1, 11)
        self.assertTrue(self.G.has_edge(edge2))
        self.assertTrue(self.G.has_edge((1, 1)))
        self.G.del_edge(edge2)
        self.assertFalse(self.G.has_edge(edge2))

    def test_copy(self):
        T = self.G.copy()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertTrue(self.G.weight(edge), T.weight(edge))

    def test_transpose(self):
        T = self.G.transpose()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertTrue(self.G.weight(~edge), T.weight(edge))

    def test_complement(self):
        T = self.G.complement()
        self.assertEqual(T.v(), self.G.v())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
            self.assertFalse(T.has_edge(Edge(node, node)))   # no loops
        for edge in T.iteredges():
            self.assertFalse(self.G.has_edge(edge))
        for edge in self.G.iteredges():
            self.assertFalse(T.has_edge(edge))

    def test_subgraph(self):
        T = self.G.subgraph([0, 1, 2])
        self.assertEqual(T.v(), 3)
        self.assertEqual(T.e(), 5)
        for edge in T.iteredges():
            self.assertTrue(self.G.has_edge(edge))

    def test_degree(self):
        self.assertRaises(ValueError, self.G.degree, 2)
        self.assertEqual(self.G.indegree(2), 2)
        self.assertEqual(self.G.indegree(1), 4)
        self.assertEqual(self.G.indegree(0), 0)
        self.assertEqual(self.G.outdegree(2), 3)
        self.assertEqual(self.G.outdegree(1), 1)
        self.assertEqual(self.G.outdegree(0), 3)

    def tearDown(self): pass

# o   o
# |   |
# 1---2-o
# | \
# 0===3

class TestMultiGraphUndirected(unittest.TestCase):

    def setUp(self):
        self.N = 4   # number of nodes
        self.G = MultiGraph(self.N, directed=False)
        self.nodes = [0, 1, 2, 3]
        self.edges = [
            Edge(0, 1, 2), Edge(0, 3, 3), Edge(0, 3, 4), Edge(1, 1, 11), 
            Edge(3, 1, 31), Edge(2, 1, 21), Edge(2, 2, 220), Edge(2, 2, 221)]
        # 0-3 parallel edge
        # 1-1 loop
        # 2-2 parallel loop
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_basic(self):
        self.assertFalse(self.G.is_directed())
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), len(self.edges))
        #self.G.show()

    def test_weight(self):
        self.assertEqual(self.G.weight(Edge(3, 3)), 0)
        self.assertEqual(self.G.weight(Edge(1, 1)), 1)
        self.assertEqual(self.G.weight(Edge(2, 2)), 2)
        self.assertEqual(self.G.weight(Edge(3, 2)), 0)
        self.assertEqual(self.G.weight(Edge(1, 2)), 1)
        self.assertEqual(self.G.weight(Edge(0, 3)), 2)
        self.assertEqual(self.G.weight((0, 3)), 2)

    def test_del_edge(self):
        edge1 = Edge(2, 3, 23)
        self.G.add_edge(edge1)
        self.assertTrue(self.G.has_edge(edge1))
        self.assertTrue(self.G.has_edge((2, 3)))
        self.assertEqual(self.G.e(), len(self.edges) + 1)
        self.G.del_edge(edge1)
        self.assertEqual(self.G.e(), len(self.edges))
        edge2 = Edge(1, 1, 11)
        self.assertTrue(self.G.has_edge(edge2))
        self.assertTrue(self.G.has_edge((1, 1)))
        self.G.del_edge(edge2)
        #self.G.del_edge((1, 1))   # ERROR, the edge should have the weight
        self.assertFalse(self.G.has_edge(edge2))

    def test_copy(self):
        T = self.G.copy()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertEqual(self.G.weight(edge), T.weight(edge))

    def test_transpose(self):
        T = self.G.transpose()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertTrue(self.G.weight(~edge), T.weight(edge))

    def test_complement(self):
        T = self.G.complement()
        self.assertEqual(T.v(), self.G.v())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
            self.assertFalse(T.has_edge(Edge(node, node)))   # no loops
        for edge in T.iteredges():
            self.assertFalse(self.G.has_edge(edge))
        for edge in self.G.iteredges():
            self.assertFalse(T.has_edge(edge))

    def test_subgraph(self):
        T = self.G.subgraph([0, 1, 2])
        self.assertEqual(T.v(), 3)
        self.assertEqual(T.e(), 5)
        for edge in T.iteredges():
            self.assertTrue(self.G.has_edge(edge))

    def test_degree(self):
        self.assertEqual(self.G.degree(2), 5)
        self.assertEqual(self.G.degree(1), 5)
        self.assertEqual(self.G.degree(0), 3)
        self.assertEqual(self.G.indegree(2), 5)
        self.assertEqual(self.G.indegree(1), 5)
        self.assertEqual(self.G.indegree(0), 3)
        self.assertEqual(self.G.outdegree(2), 5)
        self.assertEqual(self.G.outdegree(1), 5)
        self.assertEqual(self.G.outdegree(0), 3)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
