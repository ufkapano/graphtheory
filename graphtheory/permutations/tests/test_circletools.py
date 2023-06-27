#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.permutations.circletools import make_random_circle
from graphtheory.permutations.circletools import make_path_circle
from graphtheory.permutations.circletools import make_cycle_circle

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

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
