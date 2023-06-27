#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.permutations.permtools import make_random_perm
from graphtheory.permutations.permtools import make_star_perm
from graphtheory.permutations.permtools import make_bipartite_perm
from graphtheory.permutations.permtools import make_path_perm
from graphtheory.permutations.permtools import perm_has_edge1
from graphtheory.permutations.permtools import perm_has_edge2
from graphtheory.permutations.permtools import make_complement_perm

class TestPermGraphs(unittest.TestCase):

    def setUp(self): pass

    def test_random_perm(self):
        n = 10
        perm = make_random_perm(n)
        self.assertEqual(len(perm), n)
        self.assertEqual(sorted(perm), list(range(n)))
        #print("random {}".format(perm))

    def test_star_perm(self):
        n = 10
        perm = make_star_perm(n)
        self.assertEqual(len(perm), n)
        self.assertEqual(sorted(perm), list(range(n)))
        #print("star {}".format(perm))

    def test_bipartite_perm(self):
        n = 5
        perm = make_bipartite_perm(n, n)
        self.assertEqual(len(perm), 2*n)
        self.assertEqual(sorted(perm), list(range(2*n)))
        #print("bipartite {}".format(perm))

    def test_path_perm(self):
        self.assertRaises(ValueError, make_path_perm, 0)
        self.assertEqual(make_path_perm(1), [0])
        self.assertEqual(make_path_perm(2), [1, 0])
        self.assertEqual(make_path_perm(3), [2, 0, 1])
        self.assertEqual(make_path_perm(4), [1, 3, 0, 2])
        self.assertEqual(make_path_perm(5), [2, 0, 4, 1, 3])
        self.assertEqual(make_path_perm(6), [1, 3, 0, 5, 2, 4])

    def test_has_edge(self):
        perm = [4, 0, 1, 2, 3]   # star graph
        self.assertTrue(perm_has_edge1(perm, 4, 0))
        self.assertFalse(perm_has_edge1(perm, 1, 0))
        self.assertTrue(perm_has_edge2(perm, 4, 0))
        self.assertFalse(perm_has_edge2(perm, 1, 0))

    def test_complement_perm(self):
        perm = list(range(5))   # no edges
        perm2 = make_complement_perm(perm)
        self.assertEqual(perm2, list(reversed(perm)))
        self.assertFalse(perm_has_edge2(perm, 1, 2))
        self.assertTrue(perm_has_edge2(perm2, 1, 2))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
