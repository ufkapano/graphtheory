#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.planarity.planarfactory import PlanarGraphFactory
from graphtheory.planarity.wheels import is_wheel


class TestPlanarGraphFactory(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.graph_factory = PlanarGraphFactory(Graph)

    def test_cyclic(self):
        G = self.graph_factory.make_cyclic(n=self.N)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), self.N)
        aset = set(edge.weight for edge in G.iteredges())
        self.assertEqual(G.e(), len(aset))
        faces = list(G.iterfaces())
        self.assertEqual(G.f(), 2)
        self.assertEqual(len(faces), 2)
        #print "faces", faces
        self.assertRaises(ValueError, self.graph_factory.make_cyclic, 1)
        self.assertRaises(ValueError, self.graph_factory.make_cyclic, 2)

    def test_wheel(self):
        G = self.graph_factory.make_wheel(n=self.N)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), 2 * self.N - 2)
        self.assertTrue(is_wheel(G))
        faces = list(G.iterfaces())
        self.assertEqual(G.f(), self.N)
        self.assertEqual(len(faces), self.N)
        #print "faces", faces
        self.assertRaises(ValueError, self.graph_factory.make_wheel, 1)
        self.assertRaises(ValueError, self.graph_factory.make_wheel, 2)
        self.assertRaises(ValueError, self.graph_factory.make_wheel, 3)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
