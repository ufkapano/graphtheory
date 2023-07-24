#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.coloring.edgecolorcomplete import CompleteGraphEdgeColoring

class TestEdgeColoring(unittest.TestCase):

    def setUp(self): pass

    def test_Kn_odd(self):
        N = 7
        self.assertEqual(N % 2, 1)
        gf = GraphFactory(Graph)
        G = gf.make_complete(N)
        algorithm = CompleteGraphEdgeColoring(G)
        algorithm.run()
        for edge in G.iteredges():
            self.assertNotEqual(algorithm.color[edge], None)
        for node in G.iternodes():
            color_set = set()
            for edge in G.iteroutedges(node):
                if edge.source > edge.target:
                    color_set.add(algorithm.color[~edge])
                else:
                    color_set.add(algorithm.color[edge])
            self.assertEqual(len(color_set), G.degree(node))
        #print algorithm.color
        #algorithm.show_colors()
        all_colors = set(algorithm.color.values())
        self.assertEqual(len(all_colors), N)

    def test_Kn_even(self):
        N = 10
        self.assertEqual(N % 2, 0)
        gf = GraphFactory(Graph)
        G = gf.make_complete(N)
        algorithm = CompleteGraphEdgeColoring(G)
        algorithm.run()
        for edge in G.iteredges():
            self.assertNotEqual(algorithm.color[edge], None)
        for node in G.iternodes():
            color_set = set()
            for edge in G.iteroutedges(node):
                if edge.source > edge.target:
                    color_set.add(algorithm.color[~edge])
                else:
                    color_set.add(algorithm.color[edge])
            self.assertEqual(len(color_set), G.degree(node))
        #print algorithm.color
        #algorithm.show_colors()
        all_colors = set(algorithm.color.values())
        self.assertEqual(len(all_colors), N-1)

    def test_exceptions(self):
        self.assertRaises(ValueError, CompleteGraphEdgeColoring,
            Graph(5, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
