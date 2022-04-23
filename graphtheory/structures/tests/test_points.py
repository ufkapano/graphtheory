#!/usr/bin/env python3

import unittest
from fractions import Fraction
from graphtheory.structures.points import Point

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(3.4, 5.6)
        self.p2 = Point(4.5, 2.1)
        self.p3 = Point(Fraction(1, 2), Fraction(2, 3))

    def test_print(self):
        self.assertEqual(repr(self.p2),"Point(4.5, 2.1)")
        self.assertEqual(repr(self.p1),"Point(3.4, 5.6)")
        self.assertEqual(repr(self.p3),"Point(Fraction(1, 2), Fraction(2, 3))")

    def test_add(self):
        self.assertAlmostEqual(self.p1 + self.p2, Point(7.9, 7.7))

    def test_sub(self):
        self.assertAlmostEqual(self.p1 - self.p2, Point(-1.1, 3.5))

    def test_mul(self):
        self.assertAlmostEqual(self.p1 * self.p2, 27.06)
        self.assertAlmostEqual(self.p1 * 2, Point(6.8, 11.2))
        self.assertAlmostEqual(2 * self.p1, Point(6.8, 11.2))
        self.assertAlmostEqual(Point(2, 3) * 1.5, Point(3.0, 4.5))
        self.assertAlmostEqual(1.5 * Point(2, 3), Point(3.0, 4.5))
        self.assertAlmostEqual(self.p1.cross(self.p2), -18.06)
        self.assertAlmostEqual(Point(1, 0).cross(Point(0, 1)), 1)
        self.assertAlmostEqual(Point(0, 1).cross(Point(1, 0)), -1)

    def test_copy(self):
        p3 = self.p1.copy()
        self.assertEqual(p3, self.p1)
        self.assertNotEqual(id(p3), id(self.p1))   # different objects

    def test_length(self):
        self.assertAlmostEqual(Point(3, 4).length(), 5.0)

    def test_cmp(self):
        self.assertTrue(self.p1 == Point(3.4, 5.6))
        self.assertFalse(self.p1 == self.p2)
        self.assertTrue(self.p1 != self.p2)
        self.assertFalse(self.p1 != self.p1)
        self.assertTrue(self.p1 < self.p2)
        self.assertTrue(self.p1 <= self.p2)

    def test_alpha(self):
        self.assertEqual(Point(5, 5).alpha(), Fraction(1, 2))
        self.assertEqual(Point(-3, 2).alpha(), Fraction(8, 5))
        self.assertEqual(Point(-5, -1).alpha(), Fraction(13, 6))
        self.assertEqual(Point(1, -3).alpha(), Fraction(13, 4))
        self.assertEqual(self.p3.alpha(), Fraction(4, 7))

    def test_hash(self):
        aset = set()
        aset.add(self.p1)
        aset.add(self.p1)   # ignored
        self.assertEqual(len(aset), 1)
        aset.add(self.p2)
        self.assertEqual(len(aset), 2)
        aset.add(Point(1, 2))
        aset.add(Point(1.0, 2.0))   # ignored, float
        self.assertEqual(len(aset), 3)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
