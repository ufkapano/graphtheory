#!/usr/bin/env python3

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
        #print ( "faces {}".format(faces) )
        #print("C_n face2edge {}".format(G.face2edge))
        #print("C_n edge2face {}".format(G.edge2face))
        edge1 = next(G.iteredges())
        #print ( edge1 )
        #print ( list(G.iterface(edge1)) )
        #print ( list(G.iterface(~edge1)) )
        self.assertEqual(len(list(G.iterface(edge1))), self.N)
        self.assertEqual(len(list(G.iterface(~edge1))), self.N)
        self.assertRaises(ValueError, self.graph_factory.make_cyclic, 1)
        # For n=1 and the Graph class we have
        # ValueError("loops are forbidden")
        self.assertRaises(ValueError, self.graph_factory.make_cyclic, 2)
        # For n=2 and the Graph class we have
        # ValueError("parallel edges are forbidden")
        #print ( G.edge2face )
        #print ( G.face2edge )
        self.assertEqual(len(G.edge2face), 2 * self.N)
        self.assertEqual(len(G.face2edge), 2)

    def test_wheel(self):
        G = self.graph_factory.make_wheel(n=self.N)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), self.N)
        self.assertEqual(G.e(), 2 * (self.N - 1))
        self.assertTrue(is_wheel(G))
        faces = list(G.iterfaces())
        self.assertEqual(G.f(), self.N)
        self.assertEqual(len(faces), self.N)
        #print ( "faces {}".format(faces) )
        #print("W_n face2edge {}".format(G.face2edge))
        #print("W_n edge2face {}".format(G.edge2face))
        self.assertRaises(ValueError, self.graph_factory.make_wheel, 1)
        self.assertRaises(ValueError, self.graph_factory.make_wheel, 2)
        self.assertRaises(ValueError, self.graph_factory.make_wheel, 3)
        #print ( G.edge2face )
        #print ( G.face2edge )
        self.assertEqual(len(G.edge2face), 4 * (self.N - 1))
        self.assertEqual(len(G.face2edge), self.N)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
