#!/usr/bin/python

import unittest
from edges import Edge
from matrixgraphs import Graph

# 0 --> 1
# ^  /  ^
# | /.  |
# 2 --> 3

class TestGraphDirected(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.edges = [Edge(0, 1, 2), Edge(1, 2, 4), 
        Edge(2, 0, 6), Edge(2, 3, 3), Edge(3, 1, 5)]
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_directed(self):
        self.assertTrue(self.G.is_directed())
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), 5)
        self.G.del_node(1)
        self.assertEqual(self.G.v(), self.N) # no changes
        self.assertEqual(self.G.e(), 2)

    def test_cmp(self):
        T = Graph(self.N)
        self.assertFalse(T == self.G, "directed and undirected graphs")
        T = Graph(self.N, directed=True)
        for node in [0, 1, 2, 3]:
            T.add_node(node)
        self.assertFalse(T == self.G, "nodes are different")
        T.del_node(3)
        self.assertFalse(T == self.G, "numbers of nodes are different")
        T.add_node(3)
        T.add_edge(Edge(0, 1, 2))
        T.add_edge(Edge(1, 2, 4))
        T.add_edge(Edge(2, 0, 6))
        T.add_edge(Edge(2, 3, 3))
        self.assertFalse(T == self.G, "edge numbers are different")
        T.add_edge(Edge(3, 1, 7))
        self.assertFalse(T == self.G, "edge weights are different")
        T.del_edge(Edge(3, 1, 7))
        T.add_edge(Edge(1, 3, 5))
        self.assertFalse(T == self.G, "edge directions are different")
        T.del_edge(Edge(1, 3, 5))
        T.add_edge(Edge(3, 1, 5))
        self.assertTrue(T == self.G, "graphs are the same")

    def test_iteredges(self):
        inedges_B = list(self.G.iterinedges(1))
        outedges_B = list(self.G.iteroutedges(1))
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

    def test_add_graph_directed(self):
        T = Graph(self.N, directed=True)
        T.add_edge(Edge(0, 3, 9))
        self.assertEqual(T.v(), self.N)
        self.assertEqual(T.e(), 1)
        self.G.add_graph(T)
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), 6)

    def test_degree(self):
        self.assertEqual(self.G.indegree(0), 1)
        self.assertEqual(self.G.indegree(1), 2)
        self.assertEqual(self.G.indegree(2), 1)
        self.assertEqual(self.G.indegree(3), 1)
        self.assertEqual(self.G.outdegree(0), 1)
        self.assertEqual(self.G.outdegree(1), 1)
        self.assertEqual(self.G.outdegree(2), 2)
        self.assertEqual(self.G.outdegree(3), 1)

    def test_exceptions(self):
        self.assertRaises(ValueError, self.G.add_edge, Edge(0, 0, 1))
        self.assertRaises(ValueError, self.G.add_edge, Edge(0, 1, 2))
        self.assertRaises(ValueError, self.G.degree, 0)

    def tearDown(self): pass

# 0 --- 1
# |  /  |
# | /   |
# 2 --- 3

class TestGraphUndirected(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N)
        self.edges = [Edge(0, 1, 2), Edge(1, 2, 4), 
        Edge(2, 0, 6), Edge(2, 3, 3), Edge(3, 1, 5)]
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_undirected(self):
        self.assertFalse(self.G.is_directed())
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), 5)
        self.G.del_node(1)   # node become isolated
        self.assertEqual(self.G.v(), self.N)
        self.assertEqual(self.G.e(), 2)

    def test_iteredges(self):
        inedges = list(self.G.iterinedges(1))
        outedges = list(self.G.iteroutedges(1))
        #print inedges, outedges
        self.assertEqual(len(inedges), 3)
        self.assertEqual(len(outedges), 3)

    def test_copy(self):
        T = self.G.copy()
        self.assertEqual(T.v(), self.G.v())
        self.assertEqual(T.e(), self.G.e())
        for node in T.iternodes():
            self.assertTrue(self.G.has_node(node))
        for edge in T.iteredges():
            self.assertTrue(self.G.has_edge(edge))

    def test_degree(self):
        self.assertEqual(self.G.degree(0), 2)
        self.assertEqual(self.G.degree(1), 3)
        self.assertEqual(self.G.degree(2), 3)
        self.assertEqual(self.G.degree(3), 2)

    def test_add_graph_undirected(self):
        T = Graph(self.N)
        T.add_edge(Edge(0, 3, 9))
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


class TestGraphFactory(unittest.TestCase):

    def setUp(self):
        self.N = 10

    def test_complete(self):
        G = Graph.make_complete(self.N)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N * (self.N-1) / 2)
        #print
        #G.show()

    def test_sparse(self):
        m_edges = 2 * self.N
        G = Graph.make_sparse(n=self.N, m=m_edges)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), m_edges)
        #print
        #G.show()

    def test_tree(self):
        G = Graph.make_tree(n=self.N)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N-1)
        #print
        #G.show()

    def test_connected(self):
        m_edges = 2 * self.N
        G = Graph.make_connected(n=self.N, m=m_edges)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), m_edges)
        #print
        #G.show()

    def test_random(self):
        G = Graph.make_random(n=self.N, directed=True, edge_probability=0.1)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)
        #print
        #G.show()

    def test_grid(self):
        size = 4
        G = Graph.make_grid(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), size * size)
        self.assertEqual(G.e(), 2 * size * size)
        self.assertRaises(ValueError, lambda: Graph.make_grid(2))
        #print
        #G.show()

    def test_triangle(self):
        size = 4
        G = Graph.make_triangle(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), size * size)
        self.assertEqual(G.e(), 3 * size * size)
        self.assertRaises(ValueError, lambda: Graph.make_triangle(2))
        #print
        #G.show()

    def test_ladder(self):
        size = 4
        G = Graph.make_ladder(size)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), 2 * size)
        self.assertEqual(G.e(), 3 * size)
        self.assertRaises(ValueError, lambda: Graph.make_ladder(2))
        #print
        #G.show()

    def test_flow_network(self):
        G = Graph.make_flow_network(self.N)
        self.assertTrue(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertTrue(G.e() > self.N - 2)
        #print
        #G.show()

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestGraphDirected)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestGraphUndirected)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestGraphLadder)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(TestGraphFactory)
    suite = unittest.TestSuite([suite1, suite2, suite3, suite4])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
