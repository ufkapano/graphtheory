#!/usr/bin/env python3

import unittest
from graphtheory.structures.unionfind import UnionFind


class TestUnionFind(unittest.TestCase):

    def setUp(self): pass

    def test_unionfind(self):
        algorithm = UnionFind()
        for node in range(10):
            algorithm.create(node)
        pairs = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (3, 1)]
        for a, b in pairs:
            algorithm.union(a, b)
        self.assertTrue(algorithm.find(1) == algorithm.find(2))
        self.assertTrue(algorithm.find(7) != algorithm.find(9))
        pairs = [(7, 5), (3, 7), (8, 7)]
        for a, b in pairs:
            algorithm.union(a, b)
        self.assertTrue(algorithm.find(0) == algorithm.find(6))
        self.assertTrue(algorithm.find(1) == algorithm.find(9))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
