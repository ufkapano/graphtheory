#!/usr/bin/python
#
# test_unionfind.py
#
# Tests for Union-Find Problem.

from unionfind import UnionFind
import unittest


class TestUnionFind(unittest.TestCase):

    def setUp(self): pass

    def test_unionfind(self):
        uf = UnionFind()
        for node in range(10):
            uf.create(node)
        pairs = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (3, 1)]
        for a, b in pairs:
            uf.union(a, b)
        self.assertTrue(uf.find(1) == uf.find(2))
        self.assertTrue(uf.find(7) != uf.find(9))
        pairs = [(7, 5), (3, 7), (8, 7)]
        for a, b in pairs:
            uf.union(a, b)
        self.assertTrue(uf.find(0) == uf.find(6))
        self.assertTrue(uf.find(1) == uf.find(9))

    def tearDown(self): pass


if __name__ == "__main__":

    unittest.main()

# EOF
