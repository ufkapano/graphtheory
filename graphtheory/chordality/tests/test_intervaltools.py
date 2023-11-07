#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.intervaltools import make_random_interval
from graphtheory.chordality.intervaltools import make_path_interval
from graphtheory.chordality.intervaltools import make_tepee_interval
from graphtheory.chordality.intervaltools import make_2tree_interval
from graphtheory.chordality.intervaltools import make_star_interval
from graphtheory.chordality.intervaltools import make_ktree_interval
from graphtheory.chordality.intervaltools import interval_has_edge
from graphtheory.chordality.intervaltools import make_abstract_interval_graph
from graphtheory.chordality.intervaltools import print_intervals
from graphtheory.chordality.intervaltools import interval_is_connected
from graphtheory.chordality.intervaltools import find_peo_cliques
from graphtheory.chordality.intervaltools import find_max_clique_size
from graphtheory.chordality.intervaltools import interval_node_color
from graphtheory.chordality.intervaltools import interval_maximum_iset

class TestIntervalGraphs(unittest.TestCase):

    def setUp(self): pass

    def test_random_interval(self):
        n = 10
        perm = make_random_interval(n)
        self.assertEqual(len(perm), 2*n)
        self.assertEqual(sorted(perm), sorted(i % n for i in range(2*n)))
        #print(perm)

    def test_path_interval(self):
        self.assertEqual(make_path_interval(2), [0, 1, 0, 1])
        self.assertEqual(make_path_interval(3), [0, 1, 0, 2, 1, 2])
        self.assertEqual(make_path_interval(4), [0, 1, 0, 2, 1, 3, 2, 3])

    def test_tepee_interval(self):
        self.assertEqual(make_tepee_interval(2), [1, 0, 0, 1])
        self.assertEqual(make_tepee_interval(3), [2, 0, 1, 0, 1, 2])
        self.assertEqual(make_tepee_interval(4), [3, 0, 1, 0, 2, 1, 2, 3])

    def test_2tree_interval(self):
        self.assertEqual(make_2tree_interval(3), [0, 1, 2, 0, 1, 2])
        self.assertEqual(make_2tree_interval(4), [0, 1, 2, 0, 3, 1, 2, 3])
        self.assertEqual(make_2tree_interval(5), [0, 1, 2, 0, 3, 1, 4, 2, 3, 4])

    def test_star_interval(self):
        self.assertEqual(make_star_interval(2), [0, 1, 1, 0])
        self.assertEqual(make_star_interval(3), [0, 1, 1, 2, 2, 0])
        self.assertEqual(make_star_interval(4), [0, 1, 1, 2, 2, 3, 3, 0])

    def test_ktree_interval(self):
        n = 10
        self.assertEqual(len(make_ktree_interval(n, n // 2)), 2*n)
        self.assertEqual(make_ktree_interval(5, 1), [0,1,0,2,1,3,2,4,3,4])
        self.assertEqual(make_ktree_interval(5, 2), [0,1,2,0,3,1,4,2,3,4])
        self.assertEqual(make_ktree_interval(5, 3), [0,1,2,3,0,4,1,2,3,4])

    def test_interval_has_edge(self):
        self.assertTrue(interval_has_edge([1,2,3,1,4,2,3,4], 1, 3)) # diamond
        self.assertFalse(interval_has_edge([1,2,3,1,4,2,3,4], 1, 4)) # diamond
        self.assertTrue(interval_has_edge([1,2,1,3,2,4,3,4], 2, 3)) # P_4
        self.assertFalse(interval_has_edge([1,2,1,3,2,4,3,4], 1, 4)) # P_4

    def test_make_abstract_interval_graph(self):
        #   1
        #  / \
        # 2---3---0
        perm = [1,2,3,1,2,0,3,0]   # stop
        G = make_abstract_interval_graph(perm)
        #G.show()
        self.assertEqual(set(G.iteredges()),
            set([Edge(1, 2), Edge(1, 3), Edge(2, 3), Edge(0, 3)]))
        self.assertEqual(G.v(), 4)
        self.assertEqual(G.e(), 4)

    def test_interval_is_connected(self):
        self.assertTrue(interval_is_connected([0,1,0,1]))   # P_2
        self.assertTrue(interval_is_connected([0,1,2,0,1,2]))   # K_3
        self.assertFalse(interval_is_connected([0,0,1,1]))   # P_1 + P_1

    def test_find_peo_cliques(self):
        #   1
        #  / \
        # 2---3---4
        perm = [1,2,3,1,2,4,3,4]   # stop
        peo, cliques = find_peo_cliques(perm)
        #print()
        #print(print_intervals(cliques))
        self.assertEqual(peo, [1, 2, 3, 4])
        self.assertEqual(cliques, [{1, 2, 3}, {3, 4}]) # ordered cliques

    def test_find_max_clique_size(self):
        perm = [1,2,3,1,2,4,3,4]   # stop
        self.assertEqual(find_max_clique_size(perm), 3)

    def test_interval_node_color(self):
        n = 10
        perm = make_path_interval(n)   # P_n
        color = interval_node_color(perm)
        self.assertEqual(set(color.values()), {0, 1})

        perm = list(range(n)) * 2   # K_n
        color = interval_node_color(perm)
        self.assertEqual(set(color.values()), set(range(n)))

    def test_interval_maximum_iset(self):
        n = 10
        perm = list(range(n)) * 2   # K_n graph
        iset = interval_maximum_iset(perm)
        self.assertEqual(len(iset), 1)

        perm = make_path_interval(n)   # P_n graph
        iset = interval_maximum_iset(perm)
        self.assertEqual(len(iset), (n+1) // 2)

        perm = make_tepee_interval(n)
        iset = interval_maximum_iset(perm)
        self.assertEqual(len(iset), n // 2)

        perm = make_2tree_interval(n)
        iset = interval_maximum_iset(perm)
        self.assertEqual(len(iset), (n+2) // 3)

        perm = make_star_interval(n)   # K_{1,n-1} star graph
        iset = interval_maximum_iset(perm)
        self.assertEqual(len(iset), n-1)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
