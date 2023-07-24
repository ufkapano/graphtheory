#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.coloring.edgecolorbipartite import CompleteBipartiteGraphEdgeColoring
from graphtheory.coloring.edgecolorbipartite import BipartiteGraphEdgeColoring


class TestEdgeColoring(unittest.TestCase):

    def setUp(self): pass

    def test_Kpq(self):
        N1 = 5
        N2 = 3
        gf = GraphFactory(Graph)
        G = gf.make_bipartite(N1, N2, False, 1)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), N1 + N2)
        self.assertEqual(G.e(), N1 * N2)
        algorithm = CompleteBipartiteGraphEdgeColoring(G)
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
        self.assertEqual(len(all_colors), max(N1, N2))

    def test_exceptions(self):
        self.assertRaises(ValueError, CompleteBipartiteGraphEdgeColoring,
            Graph(5, directed=True))
        gf = GraphFactory(Graph)
        G = gf.make_bipartite(2, 2, False, 1)
        #G.show()
        G.del_edge(Edge(0, 2))   # nie bedzie pelny dwudzielny
        self.assertRaises(ValueError, CompleteBipartiteGraphEdgeColoring, G)

    def tearDown(self): pass


class TestBipartiteEdgeColoring(unittest.TestCase):

    def setUp(self): pass

    def test_cyclic_graph(self):
        N = 8
        assert N % 2 == 0
        gf = GraphFactory(Graph)
        G = gf.make_cyclic(N)
        algorithm = BipartiteGraphEdgeColoring(G)
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
        self.assertEqual(len(all_colors), 2)

    def test_Kpq(self):
        N1 = 15
        N2 = 13
        gf = GraphFactory(Graph)
        G = gf.make_bipartite(N1, N2, False, 1)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), N1 + N2)
        self.assertEqual(G.e(), N1 * N2)
        algorithm = BipartiteGraphEdgeColoring(G)
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
        self.assertEqual(len(all_colors), max(N1, N2))

    def test_bipartite(self):
        N1 = 10
        N2 = 13
        gf = GraphFactory(Graph)
        G = gf.make_bipartite(N1, N2)
        algorithm = BipartiteGraphEdgeColoring(G)
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
        Delta = max(G.degree(node) for node in G.iternodes())
        self.assertEqual(len(all_colors), Delta)

    def test_exceptions(self):
        self.assertRaises(ValueError, BipartiteGraphEdgeColoring,
            Graph(5, directed=True))
        gf = GraphFactory(Graph)
        G = gf.make_cyclic(4)
        #G.show()
        G.add_edge(Edge(0, 2))   # nie bedzie dwudzielny
        self.assertRaises(ValueError, BipartiteGraphEdgeColoring, G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
