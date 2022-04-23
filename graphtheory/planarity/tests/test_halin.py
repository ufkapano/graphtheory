#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.halin import HalinGraph


class TestHalinGraph(unittest.TestCase):

    def setUp(self):
        self.graph_factory = GraphFactory(Graph)

    def test_k4(self):    # graf K4 = W4
        G = self.graph_factory.make_complete(n=4, directed=False)
        # Sa 4 mozliwosci narysowania K4 na plaszczyznie bez przeciec.
        algorithm = HalinGraph(G)
        algorithm.run()
        self.assertTrue(algorithm.is_outer_k4())

# 2---3    numeracja wg cyklu Hamiltona
# |\ /|    wheel graph W_5
# | 0 |
# |/ \|
# 1---4
    def test_wheel5(self):
        N = 5
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 2), Edge(0, 3), Edge(0, 4), 
            Edge(1, 2), Edge(2, 3), Edge(3, 4), Edge(4, 1)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "wheel5 outer", algorithm.outer
        self.assertEqual(algorithm.outer, set([1, 2, 3, 4]))
        self.assertTrue(algorithm.is_outer_k4())

# 2-------3   numeracja wg cyklu Hamiltona
# |\     /|   3-prism graph
# | 1---4 |   cubic, planar
# |/     \|
# 0-------5
    def test_3prism(self):
        N = 6
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(3, 4), 
            Edge(4, 5), Edge(0, 5), Edge(1, 4), Edge(2, 0), Edge(3, 5)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "3prism outer", algorithm.outer
        #self.assertEqual(algorithm.outer, set([0, 2, 3, 5]))
        self.assertEqual(algorithm.outer, set([0, 1, 4, 5]))
        #self.assertEqual(algorithm.outer, set([1, 2, 3, 4]))
        self.assertTrue(algorithm.is_outer_k4())

#  4-------5   4-prism graph
#  |\     /|   non-Halin graph
#  | 0---1 |   Hamiltonian [0, 1, 2, 3, 7, 6, 5, 4]
#  | |   | |   cubic, planar
#  | 3---2 |
#  |/     \|
#  7-------6
    def test_4prism(self):
        N = 8
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(3, 0), 
            Edge(4, 5), Edge(5, 6), Edge(6, 7), Edge(7, 4), 
            Edge(0, 4), Edge(1, 5), Edge(2, 6), Edge(3, 7)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        #G.show()
        algorithm = HalinGraph(G)
        self.assertRaises(ValueError, algorithm.run)

# 2-------3       numeracja wg cyklu Hamiltona
# |\     / \     heptahedral graph 2
# | 1---4---5   http://mathworld.wolfram.com/HalinGraph.html
# |/     \ /
# 0-------6
    def test_halin7(self):
        N = 7
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 2), Edge(0, 6), Edge(1, 2), 
            Edge(1, 4), Edge(2, 3), Edge(3, 4), Edge(3, 5), 
            Edge(4, 5), Edge(4, 6), Edge(5, 6)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "halin7 outer", algorithm.outer
        self.assertEqual(algorithm.outer, set([0, 2, 3, 5, 6]))
        self.assertTrue(algorithm.is_outer_k4())

# 0-----7-----6  numeracja wg cyklu Hamiltona
# |\    |    /|
# | 2---3---4 |
# |/         \|
# 1-----------5
    def test_halin8a(self):
        N = 8
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 2), Edge(0, 7), Edge(1, 2), 
            Edge(1, 5), Edge(2, 3), Edge(3, 4), Edge(3, 7), 
            Edge(4, 5), Edge(4, 6), Edge(5, 6), Edge(6, 7)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "halin8a outer", algorithm.outer
        # Sa dwie mozliwosci narysowania tego grafu.
        self.assertEqual(algorithm.outer, set([0, 1, 5, 6, 7]))
        #self.assertEqual(algorithm.outer, set([1, 2, 3, 4, 5]))
        self.assertTrue(algorithm.is_outer_k4())

#   2-------3      numeracja wg cyklu Hamiltona
#  / \     / \
# 1---7---6---4
#  \ /     \ /
#   0-------5
    def test_halin8b(self):
        N = 8
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 5), Edge(0, 7), Edge(1, 2), 
            Edge(1, 7), Edge(2, 3), Edge(2, 7), Edge(3, 4), 
            Edge(3, 6), Edge(4, 5), Edge(4, 6), Edge(5, 6), Edge(6, 7)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "halin8b outer", algorithm.outer
        self.assertEqual(algorithm.outer, set([0, 1, 2, 3, 4, 5]))
        self.assertTrue(algorithm.is_outer_k4())

# 1---2---3    numeracja wg cyklu Hamiltona
# |\   \ /|
# | 7---6 |
# |/   / \|
# 0---5---4
    def test_halin8c(self):
        N = 8
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 5), Edge(0, 7), Edge(1, 2), 
            Edge(1, 7), Edge(2, 3), Edge(2, 6), Edge(3, 4), Edge(3, 6), 
            Edge(4, 5), Edge(4, 6), Edge(5, 6), Edge(6, 7)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "halin8c outer", algorithm.outer
        self.assertEqual(algorithm.outer, set([0, 1, 2, 3, 4, 5]))
        self.assertTrue(algorithm.is_outer_k4())

# 1-----4---5-----8    numeracja wg cyklu Hamiltona
# |\    |   |    /|    graf kubiczny
# | 2---3---6---7 |
# |/             \|
# 0---------------9
    def test_halin10j(self):
        N = 10
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 2), Edge(0, 9), Edge(1, 2), 
            Edge(1, 4), Edge(2, 3), Edge(3, 4), Edge(3, 6), 
            Edge(4, 5), Edge(5, 6), Edge(5, 8), Edge(6, 7), 
            Edge(7, 8), Edge(7, 9), Edge(8, 9)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "halin10j outer", algorithm.outer
        self.assertEqual(algorithm.outer, set([0, 1, 4, 5, 8, 9]))
        self.assertTrue(algorithm.is_outer_k4())

# 1-----4---------5    numeracja wg cyklu Hamiltona
# |\    |        /|    graf kubiczny
# | 2---3---8---7 |
# |/        |    \|
# 0---------9-----6
    def test_halin10k(self):
        N = 10
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 2), Edge(0, 9), Edge(1, 2), 
            Edge(1, 4), Edge(2, 3), Edge(3, 4), Edge(3, 8), 
            Edge(4, 5), Edge(5, 6), Edge(5, 7), Edge(6, 7), 
            Edge(6, 9), Edge(7, 8), Edge(8, 9)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "halin10k outer", algorithm.outer
        self.assertEqual(algorithm.outer, set([0, 1, 4, 5, 6, 9]))
        self.assertTrue(algorithm.is_outer_k4())

#   --4---5--
#  /   \ /   \
# 0     3     6    numeracja wg cyklu Hamiltona
# |\    |    /|    graf kubiczny
# | 1---2---7 |
# |/         \|
# 9-----------8
    def test_halin10l(self):
        N = 10
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 4), Edge(0, 9), Edge(1, 2), 
            Edge(1, 9), Edge(2, 3), Edge(2, 7), Edge(3, 4), 
            Edge(3, 5), Edge(4, 5), Edge(5, 6), Edge(6, 7), 
            Edge(6, 8), Edge(7, 8), Edge(8, 9)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "halin10l outer", algorithm.outer
        self.assertEqual(algorithm.outer, set([0, 4, 5, 6, 8, 9]))
        self.assertTrue(algorithm.is_outer_k4())

#   -----------11
#  /           / \
# 0-------1--10---9    numeracja wg cyklu Hamiltona
# |       |       |    cubic Frucht graph
# 4---3---2---7---8
#  \ /         \ /
#   5-----------6
    def test_frucht12(self):
        N = 10
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 4), Edge(0, 11), Edge(1, 2), 
            Edge(1, 10), Edge(2, 3), Edge(2, 7), Edge(3, 4), 
            Edge(3, 5), Edge(4, 5), Edge(5, 6), Edge(6, 7), 
            Edge(6, 8), Edge(7, 8), Edge(8, 9), Edge(9, 10), 
            Edge(9, 11), Edge(10, 11)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraph(G)
        algorithm.run()
        #print "frucht12 outer", algorithm.outer
        self.assertEqual(algorithm.outer, set([0, 4, 5, 6, 8, 9, 11]))
        self.assertTrue(algorithm.is_outer_k4())

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
