#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.spanningtrees.prim import PrimMST
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.halintd import HalinGraphTreeDecomposition


class TestHalinGraphTreeDecomposition(unittest.TestCase):

    def setUp(self):
        self.graph_factory = GraphFactory(Graph)

    def test_k4(self):    # graf K4 = W4
        G = self.graph_factory.make_complete(n=4, directed=False)
        # Sa 4 mozliwosci narysowania K4 na plaszczyznie bez przeciec.
        #print "k4 ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([1, 2, 3]))
        algorithm.run()
        parent = {0: None, 1: 0, 2: 0, 3: 0}
        self.assertEqual(algorithm.parent, parent)
        order = [1, 2, 3, 0]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "wheel5 ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([1, 2, 3, 4]))
        algorithm.run()
        #print "wheel5 outer", algorithm.outer
        #print "wheel5 cycle", algorithm.cycle
        parent = {0: None, 1: 0, 2: 0, 3: 0, 4: 0}
        self.assertEqual(algorithm.parent, parent)
        order = [1, 2, 3, 4, 0]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "3prism ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 2, 3, 5]))
        #algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 1, 4, 5]))
        #algorithm = HalinGraphTreeDecomposition(G, outer=set([1, 2, 3, 4]))
        algorithm.run()
        #print "3prism outer", algorithm.outer
        parent = {0: 1, 1: None, 2: 1, 3: 4, 4: 1, 5: 4}
        self.assertEqual(algorithm.parent, parent)
        #order = [1, 0, 2, 3, 5, 4]
        order = [4, 0, 2, 3, 5, 1]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "halin7 ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 2, 3, 5, 6]))
        algorithm.run()
        #print "halin7 outer", algorithm.outer
        parent = {0: 1, 1: None, 2: 1, 3: 4, 4: 1, 5: 4, 6: 4}
        self.assertEqual(algorithm.parent, parent)
        #order = [1, 0, 2, 3, 5, 6, 4]
        order = [5, 4, 0, 2, 3, 6, 1]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "halin8a ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 7, 6, 5, 1]))
        algorithm.run()
        #print "halin8a outer", algorithm.outer
        parent = {0: 2, 1: 2, 2: None, 3: 2, 4: 3, 5: 4, 6: 4, 7: 3}
        self.assertEqual(algorithm.parent, parent)
        #order = [2, 4, 0, 1, 5, 6, 7, 3]
        order = [4, 2, 0, 1, 5, 6, 7, 3]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "halin8b ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 1, 2, 3, 4, 5]))
        algorithm.run()
        #print "halin8b outer", algorithm.outer
        parent = {0: 7, 1: 7, 2: 7, 3: 6, 4: 6, 5: 6, 6: None, 7: 6}
        self.assertEqual(algorithm.parent, parent)
        #order = [1, 7, 0, 2, 3, 4, 5, 6]
        order = [4, 6, 0, 1, 2, 3, 5, 7]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "halin8c ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 1, 2, 3, 4, 5]))
        algorithm.run()
        #print "halin8c outer", algorithm.outer
        parent = {0: 7, 1: 7, 2: 6, 3: 6, 4: 6, 5: 6, 6: None, 7: 6}
        self.assertEqual(algorithm.parent, parent)
        #order = [7, 0, 1, 2, 3, 4, 5, 6]   # wersja z indeksami
        order = [3, 4, 6, 0, 1, 2, 5, 7]   # wersja z linkami
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "halin10j ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 1, 4, 5, 8, 9]))
        algorithm.run()
        #print "halin10j outer", algorithm.outer
        parent = {0: 2, 1: 2, 2: None, 3: 2, 4: 3, 5: 6, 6: 3, 7: 6, 8: 7, 9: 7}
        self.assertEqual(algorithm.parent, parent)
        order = [7, 2, 8, 6, 0, 1, 4, 5, 9, 3]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "halin10k ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 1, 4, 5, 6, 9]))
        algorithm.run()
        #print "halin10k outer", algorithm.outer
        parent = {0: 2, 1: 2, 2: None, 3: 2, 4: 3, 5: 7, 6: 7, 7: 8, 8: 3, 9: 8}
        self.assertEqual(algorithm.parent, parent)
        order = [7, 2, 6, 8, 0, 1, 4, 5, 9, 3]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "halin10l ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 4, 5, 6, 8, 9]))
        algorithm.run()
        #print "halin10l outer", algorithm.outer
        parent = {0: 1, 1: None, 2: 1, 3: 2, 4: 3, 5: 3, 6: 7, 7: 2, 8: 7, 9: 1}
        self.assertEqual(algorithm.parent, parent)
        #order = [3, 1, 7, 0, 4, 5, 6, 8, 9, 2]
        order = [3, 7, 1, 0, 4, 5, 6, 8, 9, 2]
        #self.assertEqual(algorithm.order, order) # difference in Py3
        self.assertEqual(len(algorithm.cliques), G.v()-3)

#    10---8---7     wachlarz nieparzysty
#    /  \ | /  \
#   /     9     \
#  /      |      \
# 0---2---3---4---6
#  \ /         \ /
#   1-----------5
    def test_halin11(self):
        N = 11
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 2), Edge(0, 10), Edge(1, 2), 
            Edge(1, 5), Edge(2, 3), Edge(3, 4), Edge(3, 9), 
            Edge(4, 5), Edge(4, 6), Edge(5, 6), Edge(6, 7), 
            Edge(7, 8), Edge(7, 9), Edge(8, 9), Edge(8, 10),
            Edge(9, 10)]   # E=17
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 1, 5, 6, 7, 8, 10]))
        algorithm.run()
        #print "halin11 ..."
        #print "halin11 outer", algorithm.outer
        parent = {0: 2, 1: 2, 2: None, 3: 2, 4: 3, 5: 4, 6: 4, 7: 9, 8: 9, 9: 3, 10: 9}
        self.assertEqual(algorithm.parent, parent)
        order = [4, 8, 9, 2, 0, 1, 5, 6, 7, 10, 3]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

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
        #print "frucht12 ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 4, 5, 6, 8, 9, 11]))
        algorithm.run()
        #print "frucht12 outer", algorithm.outer
        parent = {0: 1, 1: None, 2: 1, 3: 2, 4: 3, 5: 3, 6: 7, 7: 2, 8: 7, 9: 10, 10: 1, 11: 10}
        self.assertEqual(algorithm.parent, parent)
        #order = [10, 3, 7, 11, 1, 0, 4, 5, 6, 8, 9, 2]
        order = [10, 7, 3, 11, 1, 0, 4, 5, 6, 8, 9, 2]
        #self.assertEqual(algorithm.order, order) # difference in Py3
        self.assertEqual(len(algorithm.cliques), G.v()-3)

#   0---------15--------14        cubic
#  / \        |        / \
# 2---1---6---7---8---13--12
#  \     /         \     /
#   3---5           9---11
#    \ /             \ /
#     4---------------10
    def test_halin16(self):
        N = 16
        G = Graph(N, False)
        edges = [Edge(0, 1), Edge(0, 2), Edge(0, 15), Edge(1, 2), 
            Edge(1, 6), Edge(2, 3), Edge(3, 4), Edge(3, 5), 
            Edge(4, 5), Edge(4, 10), Edge(5, 6), Edge(6, 7), 
            Edge(7, 8), Edge(7, 15), Edge(8, 9), Edge(8, 13), 
            Edge(9, 10), Edge(9, 11), Edge(10, 11), Edge(11, 12), 
            Edge(12, 13), Edge(12, 14), Edge(13, 14), Edge(14, 15)]
        for node in range(N):
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        #print "halin16 ..."
        algorithm = HalinGraphTreeDecomposition(G, outer=set([0, 2, 3, 4, 10, 11, 12, 14, 15]))
        algorithm.run()
        #print "halin16 outer", algorithm.outer
        parent = {0: 1, 1: None, 2: 1, 3: 5, 4: 5, 5: 6, 6: 1, 7: 6, 
            8: 7, 9: 8, 10: 9, 11: 9, 12: 13, 13: 8, 14: 13, 15: 7}
        self.assertEqual(algorithm.parent, parent)
        order = [5, 9, 13, 1, 11, 12, 8, 2, 3, 6, 0, 4, 10, 14, 15, 7]
        self.assertEqual(algorithm.order, order)
        self.assertEqual(len(algorithm.cliques), G.v()-3)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
