#!/usr/bin/python
#
# test_edges.py
#
# Tests for edges.

import unittest
from edges import Edge


class TestEdge(unittest.TestCase):

    def setUp(self):
        self.edge1 = Edge(2, 4)
        self.edge2 = Edge("A", "B", 5)

    def test_init(self):
        self.assertEqual(repr(self.edge1), "Edge(2, 4, 1)")
        self.assertEqual(repr(self.edge2), "Edge('A', 'B', 5)")

    def test_hash(self):
        aset = set()
        aset.add(self.edge1)
        aset.add(self.edge1)
        aset.add(~self.edge1)
        aset.add(self.edge2)
        aset.add(~self.edge2)
        self.assertEqual(len(aset), 4)

    def tearDown(self): pass


if __name__ == "__main__":

    unittest.main()

# EOF
