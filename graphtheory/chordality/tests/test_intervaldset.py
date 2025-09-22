#!/usr/bin/env python3

import unittest
from graphtheory.chordality.intervaltools import make_abstract_interval_graph
from graphtheory.chordality.intervaltools import make_2tree_interval
from graphtheory.chordality.intervaldset import IntervalDominatingSet

class TestDominatingSet(unittest.TestCase):

    def setUp(self): pass

    def test_interval_dset1(self):
        #   1     dset {3}
        #  / \     2-stable set - single node
        # 2---3---0
        perm = [1,2,3,1,2,0,3,0]   # stop graph
        algorithm = IntervalDominatingSet(perm)
        algorithm.run()
        expected1 = {3}
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        G = make_abstract_interval_graph(perm)
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(G.iteradjacent(node))
        self.assertEqual(len(neighbors), G.v())

    def test_interval_dset2(self):
        # 1---2  dset {2} lub {3}
        # | / |
        # 3---4
        perm = [1,2,3,1,4,2,3,4]   # diamond
        algorithm = IntervalDominatingSet(perm)
        algorithm.run()
        expected1 = {2}
        expected1 = {3}
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        G = make_abstract_interval_graph(perm)
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(G.iteradjacent(node))
        self.assertEqual(len(neighbors), G.v())

    def test_interval_dset3(self):
        # 1---2  dset {3, 5}, 2-stable set {1, 5}
        # | / |
        # 3---4---5
        perm = [1,2,3,1,4,2,3,5,4,5]   # diamond with a leaf
        algorithm = IntervalDominatingSet(perm)
        algorithm.run()
        expected1 = {3, 5}
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        G = make_abstract_interval_graph(perm)
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(G.iteradjacent(node))
        self.assertEqual(len(neighbors), G.v())

    def test_interval_dset4(self):
        # dset {2, 7}, 2-stable set {0, 5}
        perm = make_2tree_interval(8)
        algorithm = IntervalDominatingSet(perm)
        algorithm.run()
        expected1 = {2, 7}
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected1)
        # Testing dset.
        G = make_abstract_interval_graph(perm)
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(G.iteradjacent(node))
        self.assertEqual(len(neighbors), G.v())

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
