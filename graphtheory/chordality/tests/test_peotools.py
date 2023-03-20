#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.peotools import find_peo_mcs
from graphtheory.chordality.peotools import find_maximum_clique_peo
from graphtheory.chordality.peotools import find_all_maximal_cliques
from graphtheory.chordality.peotools import is_peo1, is_peo2
from graphtheory.chordality.peotools import find_maximum_independent_set

# 0---1            2-tree
# | \ | \     iset {3,4},{3,1},{4,0}
# 3---2---4

class TestChordalGraphs(unittest.TestCase):

    def setUp(self):
        self.N = 5
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(0, 3), 
             Edge(0, 2), Edge(2, 4), Edge(1, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_max_clique(self):
        order = find_peo_mcs(self.G)
        max_clique = find_maximum_clique_peo(self.G, order)
        clique1 = set([0, 1, 2])
        clique2 = set([0, 2, 3])
        clique3 = set([1, 2, 4])
        self.assertEqual(len(max_clique), 3)
        self.assertEqual(max_clique, clique1)

    def test_find_all_maximal_cliques(self):
        order = find_peo_mcs(self.G)
        cliques = find_all_maximal_cliques(self.G, order)
        expected = [set([1, 2, 4]), set([0, 2, 3]), set([0, 1, 2])]
        self.assertEqual(cliques, expected)
        # Obliczam rozmiar najwiekszej kliki (liczba chromatyczna).
        self.assertEqual(max(len(c) for c in cliques), 3)

    def test_is_peo(self):
        self.assertTrue(is_peo1(self.G, [4,3,2,1,0]))
        self.assertTrue(is_peo1(self.G, [4,1,3,2,0]))
        self.assertTrue(is_peo1(self.G, [3,0,1,2,4]))
        self.assertFalse(is_peo1(self.G, [0,4,3,2,1]))
        self.assertFalse(is_peo1(self.G, [4,0,3,2,1]))
        self.assertTrue(is_peo2(self.G, [4,3,2,1,0]))
        self.assertTrue(is_peo2(self.G, [4,1,3,2,0]))
        self.assertTrue(is_peo2(self.G, [3,0,1,2,4]))
        self.assertFalse(is_peo2(self.G, [0,4,3,2,1]))
        self.assertFalse(is_peo2(self.G, [4,0,3,2,1]))

    def test_max_iset(self):
        order = find_peo_mcs(self.G)
        iset = find_maximum_independent_set(self.G, order)
        #print("peo {}".format(order))
        #print("iset {}".format(iset))
        self.assertEqual(len(iset), 2)
        expected1 = set([3, 1])
        expected2 = set([3, 4])
        expected3 = set([4, 0])
        self.assertEqual(iset, expected2)
        for edge in self.G.iteredges():
            self.assertFalse(edge.source in iset and edge.target in iset)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
