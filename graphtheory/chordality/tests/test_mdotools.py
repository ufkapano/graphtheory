#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.mdotools import find_mdo
from graphtheory.chordality.mdotools import find_maximum_clique_mdo

# 0---1            2-tree
# | \ | \
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

    def test_find_mdo(self):
        order = find_mdo(self.G)
        self.assertEqual(len(order), self.N)
        self.assertTrue(order[0] in (3, 4))
        #self.assertEqual(order, [3, 0, 1, 2, 4]) # Py2
        #self.assertEqual(order, [3, 4, 0, 1, 2]) # Py3
        #self.assertEqual(order, [4, 1, 0, 2, 3]) # possible
        #self.assertEqual(order, [4, 3, 0, 1, 2]) # possible

    def test_find_maximum_clique_mdo(self):
        max_clique = find_maximum_clique_mdo(self.G)
        clique1 = set([0, 1, 2])
        clique2 = set([0, 2, 3])
        clique3 = set([1, 2, 4])
        self.assertEqual(len(max_clique), 3)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
