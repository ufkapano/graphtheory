#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge


class TestDirectedEdge(unittest.TestCase):

    def setUp(self):
        self.edge1 = Edge(2, 4)
        self.edge2 = Edge("A", "B", 5)
        self.edge3 = Edge(1, 3, 2)
        self.edge4 = Edge(1, 2)

    def test_repr(self):
        self.assertEqual(repr(self.edge1), "Edge(2, 4)")
        self.assertEqual(repr(~self.edge1), "Edge(4, 2)")
        self.assertEqual(repr(self.edge2), "Edge('A', 'B', 5)")
        self.assertEqual(repr(~self.edge2), "Edge('B', 'A', 5)")
        self.assertEqual(repr(self.edge3), "Edge(1, 3, 2)")
        self.assertEqual(repr(~self.edge3), "Edge(3, 1, 2)")

    def test_cmp(self):
        self.assertTrue(self.edge1 == Edge(2, 4))
        self.assertFalse(self.edge1 == self.edge3)
        self.assertTrue(self.edge1 != self.edge3)
        self.assertFalse(self.edge1 != Edge(2, 4))
        self.assertTrue(self.edge1 < self.edge3)
        self.assertFalse(self.edge3 < self.edge4)
        self.assertTrue(self.edge1 <= self.edge3)
        self.assertFalse(self.edge1 <= self.edge4)
        self.assertTrue(self.edge1 > self.edge4)
        self.assertFalse(self.edge1 > self.edge3)
        self.assertTrue(self.edge3 >= self.edge4)
        self.assertFalse(self.edge1 >= self.edge3)

    def test_hash(self):
        aset = set()
        aset.add(self.edge1)
        aset.add(self.edge1)   # ignored
        aset.add(self.edge1)   # ignored
        self.assertEqual(len(aset), 1)
        aset.add(~self.edge1)
        aset.add(self.edge2)
        aset.add(~self.edge2)
        self.assertEqual(len(aset), 4)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
