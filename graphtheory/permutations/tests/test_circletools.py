#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.permutations.circletools import make_random_circle
from graphtheory.permutations.circletools import make_path_circle
from graphtheory.permutations.circletools import make_cycle_circle
from graphtheory.permutations.circletools import make_2tree_circle
from graphtheory.permutations.circletools import make_ktree_circle
from graphtheory.permutations.circletools import make_star_circle
from graphtheory.permutations.circletools import circle_has_edge
from graphtheory.permutations.circletools import circle_is_connected
from graphtheory.permutations.circletools import is_perm_graph
from graphtheory.permutations.circletools import circle2perm
from graphtheory.permutations.circletools import make_abstract_circle_graph

class TestCircleGraphs(unittest.TestCase):

    def setUp(self): pass

    def test_random_circle(self):
        n = 10
        perm = make_random_circle(n)
        self.assertEqual(len(perm), 2*n)
        self.assertEqual(set(perm), set(range(n)))
        #print("random {}".format(perm))

    def test_path_circle(self):
        n = 10
        perm = make_path_circle(n)
        self.assertEqual(len(perm), 2*n)
        self.assertEqual(set(perm), set(range(n)))
        self.assertEqual(make_path_circle(1), [0, 0])
        self.assertEqual(make_path_circle(2), [0, 1, 0, 1])
        self.assertEqual(make_path_circle(3), [0, 1, 0, 2, 1, 2])
        self.assertEqual(make_path_circle(4), [0, 1, 0, 2, 1, 3, 2, 3])
        #print("path {}".format(perm))

    def test_cycle_circle(self):
        n = 10
        perm = make_cycle_circle(n)
        self.assertEqual(len(perm), 2*n)
        self.assertEqual(set(perm), set(range(n)))
        self.assertRaises(ValueError, make_cycle_circle, 2)
        self.assertEqual(make_cycle_circle(3), [2, 1, 0, 2, 1, 0])
        self.assertEqual(make_cycle_circle(4), [3, 1, 0, 2, 1, 3, 2, 0])
        #print("cycle {}".format(perm))

    def test_2tree_circle(self):
        n = 10
        perm = make_2tree_circle(n)
        self.assertEqual(len(perm), 2*n)
        self.assertEqual(set(perm), set(range(n)))
        self.assertRaises(ValueError, make_2tree_circle, 1)
        self.assertEqual(make_2tree_circle(2), [0, 1, 0, 1])
        self.assertEqual(make_2tree_circle(3), [0, 1, 2, 0, 1, 2])
        self.assertEqual(make_2tree_circle(4), [0, 1, 2, 0, 3, 1, 2, 3])
        self.assertEqual(make_2tree_circle(5), [0, 1, 2, 0, 3, 1, 4, 2, 3, 4])
        #print("2tree {}".format(perm))

    def test_star_circle(self):
        n = 10
        perm = make_star_circle(n)
        self.assertEqual(len(perm), 2*n)
        self.assertEqual(set(perm), set(range(n)))
        self.assertRaises(ValueError, make_star_circle, 1)
        self.assertEqual(make_star_circle(2), [0, 1, 0, 1])
        self.assertEqual(make_star_circle(3), [0, 1, 2, 0, 2, 1])
        self.assertEqual(make_star_circle(4), [0, 1, 2, 3, 0, 3, 2, 1])

    def test_ktree_circle(self):
        n = 10
        perm = make_ktree_circle(n, n // 2)
        self.assertEqual(len(perm), 2*n)
        self.assertEqual(set(perm), set(range(n)))
        self.assertEqual(make_ktree_circle(3,2), [0, 1, 2, 0, 1, 2])
        self.assertEqual(make_ktree_circle(4,2), [0, 1, 2, 0, 3, 1, 2, 3])

    def test_circle_has_edge(self):
        perm = [3, 1, 0, 2, 1, 3, 2, 0]   # C_4
        self.assertTrue(circle_has_edge(perm, 0, 1))
        self.assertFalse(circle_has_edge(perm, 0, 2))

    def test_make_abstract_circle_graph(self):
        perm = [3, 1, 0, 2, 1, 3, 2, 0]   # C_4
        graph = make_abstract_circle_graph(perm)
        self.assertTrue(isinstance(graph, Graph))
        self.assertEqual(graph.v(), 4)
        self.assertEqual(graph.e(), 4)

    def test_circle_is_connected(self):
        self.assertTrue(circle_is_connected([0, 1, 0, 1]))   # P_2
        self.assertTrue(circle_is_connected(["A", "B", "A", "B"]))   # P_2
        self.assertTrue(circle_is_connected([3, 1, 0, 2, 1, 3, 2, 0]))   # C_4
        self.assertTrue(circle_is_connected([0, 1, 0, 2, 3, 1, 3, 2]))   # K_{1,3}
        self.assertTrue(circle_is_connected([4, 1, 0, 2, 1, 3, 2, 4, 3, 0]))   # C_5
        self.assertFalse(circle_is_connected([0, 1, 0, 1, 2, 3, 2, 3])) # P_2+P_2
        self.assertFalse(circle_is_connected([0, 1, 0, 1, 2, 2])) # P_2+P_1
        self.assertFalse(circle_is_connected([0, 1, 2, 0, 1, 2, 3, 4, 3, 4])) # C_3+P_2

    def test_is_perm_graph(self):
        self.assertTrue(is_perm_graph([0, 1, 0, 1])) # P_2
        self.assertTrue(is_perm_graph([3, 1, 0, 2, 1, 3, 2, 0])) # C_4
        self.assertFalse(is_perm_graph([4, 1, 0, 2, 1, 3, 2, 4, 3, 0])) # C_5
        # figure-8 graph (n=6)
        double_perm = list("cdbcabedfeaf")
        perm, n2l, l2n = circle2perm(double_perm)
        self.assertEqual(perm, [2, 4, 0, 5, 1, 3])
        self.assertEqual(n2l, {0: 'c', 1: 'a', 2: 'b', 3: 'e', 4: 'd', 5: 'f'})
        self.assertEqual(l2n, {'c': 0, 'a': 1, 'b': 2, 'e': 3, 'd': 4, 'f': 5})

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
