#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.peotools import is_peo1
from graphtheory.permutations.permtools import make_random_perm
from graphtheory.permutations.permtools import make_star_perm
from graphtheory.permutations.permtools import make_bipartite_perm
from graphtheory.permutations.permtools import make_path_perm
from graphtheory.permutations.permtools import make_abstract_perm_graph
from graphtheory.permutations.permtools import make_complement_perm
from graphtheory.permutations.permtools import perm_is_connected
from graphtheory.permutations.permtools import perm_connected_components
from graphtheory.permutations.permpeo import PermGraphPEO

class TestPermGraphPEO(unittest.TestCase):

    def setUp(self): pass

    def test_perm_c4(self):
        n = 4
        perm = make_bipartite_perm(n // 2, n-(n // 2))
        self.assertEqual(len(perm), n)
        self.assertEqual(sorted(perm), list(range(n)))
        algorithm = PermGraphPEO(perm)
        algorithm.run()
        self.assertTrue(is_peo1(algorithm.graph, algorithm.order))
        #print("new_edges", algorithm.new_edges)
        #print("order", algorithm.order)
        self.assertEqual(len(algorithm.new_edges), 1)
        self.assertEqual(sorted(algorithm.order), list(range(n)))

    def test_perm_house(self):
        n = 5
        perm = (2,4,0,3,1)   # house, 1 cykl (2,0,4,1)
        algorithm = PermGraphPEO(perm)
        algorithm.run()
        self.assertTrue(is_peo1(algorithm.graph, algorithm.order))
        #print("new_edges", algorithm.new_edges)
        #print("order", algorithm.order)
        self.assertEqual(len(algorithm.new_edges), 1)
        self.assertEqual(sorted(algorithm.order), list(range(n)))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
