#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.nodecolorouterplanar import OuterplanarNodeColoring

# 0 --- 1 --- 2 nie jest dwudzielny, bo sa trojkaty
# |   / |   /
# |  /  |  /
# | /   | /
# 3 --- 4

class TestNodeColoring(unittest.TestCase):

    def setUp(self):
        self.N = 5
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(0, 3), Edge(1, 3), Edge(1, 4),
            Edge(1, 2), Edge(2, 4), Edge(3, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_outerplanar_node_coloring(self):
        algorithm = OuterplanarNodeColoring(self.G)
        algorithm.run()
        # Sprawdzenie, czy kazdy wierzcholek ma kolor.
        for node in self.G.iternodes():
            self.assertNotEqual(algorithm.color[node], None)
        for edge in self.G.iteredges():
            self.assertNotEqual(algorithm.color[edge.source],
                                algorithm.color[edge.target])
        all_colors = set(algorithm.color[node] for node in self.G.iternodes())
        self.assertEqual(len(all_colors), 3)

    def test_cycle_node_coloring(self):
        gf = GraphFactory(Graph)
        self.G = gf.make_cyclic(2 * self.N)   # bipartite
        algorithm = OuterplanarNodeColoring(self.G)
        algorithm.run()
        # Sprawdzenie, czy kazdy wierzcholek ma kolor.
        for node in self.G.iternodes():
            self.assertNotEqual(algorithm.color[node], None)
        for edge in self.G.iteredges():
            self.assertNotEqual(algorithm.color[edge.source],
                                algorithm.color[edge.target])
        all_colors = set(algorithm.color[node] for node in self.G.iternodes())
        self.assertEqual(len(all_colors), 2)

# 0   3---4
# | \
# 1---2
    def test_not_connected(self):
        self.G = Graph()
        edge_list = [Edge(0, 1), Edge(0, 2), Edge(1, 2), Edge(3, 4)]
        for edge in edge_list:
            self.G.add_edge(edge)
        algorithm = OuterplanarNodeColoring(self.G)
        algorithm.run()
        # Sprawdzenie, czy kazdy wierzcholek ma kolor.
        for node in self.G.iternodes():
            self.assertNotEqual(algorithm.color[node], None)
        for edge in self.G.iteredges():
            self.assertNotEqual(algorithm.color[edge.source],
                                algorithm.color[edge.target])
        all_colors = set(algorithm.color[node] for node in self.G.iternodes())
        #print(algorithm.color)
        self.assertEqual(len(all_colors), 3)

    def test_exceptions(self):
        self.assertRaises(ValueError, OuterplanarNodeColoring,
            Graph(5, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
