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
from graphtheory.permutations.permtools import make_abstract_perm_graph
from graphtheory.permutations.permtools import make_complement_perm
from graphtheory.permutations.permtools import perm_is_connected
from graphtheory.permutations.permtools import perm_connected_components

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

    def test_make_abstract_perm_graph(self):
        perm = list(range(4,-1,-1))   # K_5
        graph = make_abstract_perm_graph(perm)
        self.assertTrue(isinstance(graph, Graph))
        self.assertEqual(graph.v(), 5)   # K_5
        self.assertEqual(graph.e(), 10)   # K_5
        perm = [2, 3, 0, 1]   # C_4
        graph = make_abstract_perm_graph(perm)
        self.assertTrue(isinstance(graph, Graph))
        self.assertEqual(graph.v(), 4)   # C_4
        self.assertEqual(graph.e(), 4)   # C_4

    def test_complement_perm(self):
        perm = list(range(5))   # no edges
        perm2 = make_complement_perm(perm)
        self.assertEqual(perm2, list(reversed(perm)))
        self.assertFalse(perm_has_edge2(perm, 1, 2))
        self.assertTrue(perm_has_edge2(perm2, 1, 2))

    def test_perm_is_connected(self):
        self.assertTrue(perm_is_connected([4, 3, 2, 1, 0]))
        self.assertTrue(perm_is_connected([2, 3, 0, 1]))
        self.assertFalse(perm_is_connected([1, 0, 3, 2]))
        self.assertFalse(perm_is_connected([3, 2, 1, 0, 4]))

    def test_perm_connected_components(self):
        perm = [4, 3, 2, 1, 0]
        n_cc, cc = perm_connected_components(perm)
        self.assertEqual(n_cc, 1)
        self.assertEqual(set(cc[v] for v in cc), set([0]))
        perm = [1, 0, 3, 2]
        n_cc, cc = perm_connected_components(perm)
        self.assertEqual(n_cc, 2)
        self.assertEqual(set(cc[v] for v in cc), set([0, 1]))
        #print(cc)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
