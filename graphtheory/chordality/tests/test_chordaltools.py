#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.peotools import find_peo_mcs
from graphtheory.chordality.chordaltools import make_random_ktree
from graphtheory.chordality.chordaltools import make_random_chordal

class TestChordalGraphs(unittest.TestCase):

    def setUp(self): pass

    def test_make_random_ktree(self):
        n, k = 10, 4
        G = make_random_ktree(n, k)
        order = find_peo_mcs(G)
        self.assertEqual(len(order), n)

    def test_make_random_chordal(self):
        n = 10
        G = make_random_chordal(n)
        order = find_peo_mcs(G)
        self.assertEqual(len(order), n)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
