#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.planarity.halintools import make_halin
from graphtheory.planarity.halintools import make_halin_cubic


class TestHalinGraph(unittest.TestCase):

    def setUp(self): pass

    def test_halin(self):
        N = 9
        G = make_halin(n=N)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), N)
        self.assertTrue(G.e() <= 2 * N - 2)
        for node in G.iternodes():
            self.assertTrue(G.degree(node) > 2)
        #G.show()
        self.assertRaises(ValueError, make_halin, 1)
        self.assertRaises(ValueError, make_halin, 2)
        self.assertRaises(ValueError, make_halin, 3)

    def test_halin_cubic(self):
        N = 10   # N even
        G = make_halin_cubic(n=N)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), N)
        self.assertEqual(G.e() * 2, 3 * N)
        for node in G.iternodes():
            self.assertEqual(G.degree(node), 3)
        #G.show()
        self.assertRaises(ValueError, make_halin_cubic, 1)
        self.assertRaises(ValueError, make_halin_cubic, 2)
        self.assertRaises(ValueError, make_halin_cubic, 3)
        self.assertRaises(ValueError, make_halin_cubic, 5)
        self.assertRaises(ValueError, make_halin_cubic, 7)
        self.assertRaises(ValueError, make_halin_cubic, 9)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
