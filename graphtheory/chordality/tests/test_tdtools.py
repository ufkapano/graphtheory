#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.peotools import find_peo_mcs
from graphtheory.chordality.tdtools import find_td_chordal

# 0---1            2-tree
# | \ | \
# 3---2---4

class TestTreeDecomposition(unittest.TestCase):

    def setUp(self):
        self.N = 5           # number of nodes
        self.G = Graph(self.N)
        self.nodes = list(range(self.N))
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

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
