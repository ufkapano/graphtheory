#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.peotools import find_peo_mcs
from graphtheory.chordality.tdtools import find_td_chordal
from graphtheory.chordality.tdtools import find_td_order
from graphtheory.chordality.tdtools import find_treewidth_min_deg # upper bound
from graphtheory.chordality.tdtools import find_treewidth_mmd # lower bound

# 0---1            2-tree
# | \ | \
# 3---2---4

class TestTreeDecomposition(unittest.TestCase):

    def setUp(self):
        self.N = 5   # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(0, 3), 
             Edge(0, 2), Edge(2, 4), Edge(1, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        self.order = find_peo_mcs(self.G)

    def test_find_td_chordal(self):
        T = find_td_chordal(self.G, self.order)
        #T.show()
        bags1 = set([(0, 1, 2), (0, 2, 3), (1, 2, 4)])
        bags2 = set(T.iternodes())
        self.assertEqual(T.v(), len(bags1))
        self.assertEqual(bags1, bags2)

    def test_find_td_order(self):
        T = find_td_order(self.G, [3, 0, 1, 2, 4])
        #T.show()
        bags1 = set([(0, 1, 2), (0, 2, 3), (1, 2, 4)])
        bags2 = set(T.iternodes())
        self.assertEqual(T.v(), len(bags1))
        self.assertEqual(bags1, bags2)

    def test_find_treewidth_min_deg(self):
        treewidth, order = find_treewidth_min_deg(self.G) # upper bound
        #print("min_deg", treewidth)
        self.assertTrue(treewidth >= 2) # 2 is the true treewidth

    def test_find_treewidth_mmd(self):
        treewidth, order = find_treewidth_mmd(self.G) # lower bound
        #print("mmd", treewidth)
        self.assertTrue(treewidth <= 2) # 2 is the true treewidth

    def tearDown(self): pass


class TestTreeDecomposition2(unittest.TestCase):

    def setUp(self): pass

# 2-------3   numeracja wg cyklu Hamiltona
# |\     /|   3-prism graph, Halin graph
# | 1---4 |   cubic, planar
# |/     \|   treewidth = 3
# 0-------5

    def test_find_td_order(self):
        G = Graph(6)
        edge_list = [Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(3, 4), 
            Edge(4, 5), Edge(0, 5), Edge(1, 4), Edge(2, 0), Edge(3, 5)]
        for edge in edge_list:
            G.add_edge(edge)
        T = find_td_order(G, [2,5,0,1,3,4])
        #T.show()
        bags1 = set([(0,1,2,3), (0,1,3,4), (0,3,4,5)])
        bags2 = set(T.iternodes())
        self.assertEqual(T.v(), len(bags1))
        self.assertEqual(bags1, bags2)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
