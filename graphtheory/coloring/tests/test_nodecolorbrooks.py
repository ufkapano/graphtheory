#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.coloring.nodecolorbrooks import BrooksNodeColoring

# 0 --- 1 --- 2 nie jest dwudzielny, bo sa trojkaty
# |   / |   / |
# |  /  |  /  | jest dwuspojny (biconnected)
# | /   | /   |
# 3 --- 4 --- 5
# Best node coloring - 3 colors.
# color = {0:a, 1:b, 2:c, 3:c, 4:a, 5:b}

class TestNodeColoring(unittest.TestCase):

    def setUp(self):
        self.N = 6
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(0, 3), Edge(1, 3), Edge(1, 4), Edge(1, 2), 
            Edge(2, 4), Edge(2, 5), Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_brooks_node_coloring(self):
        algorithm = BrooksNodeColoring(self.G)
        algorithm.run()
        for node in self.G.iternodes():
            self.assertNotEqual(algorithm.color[node], None)
        for edge in self.G.iteredges():
            self.assertNotEqual(algorithm.color[edge.source],
                                algorithm.color[edge.target])
        #print algorithm.color
        all_colors = set(algorithm.color[node] for node in self.G.iternodes())
        self.assertEqual(len(all_colors), 4)

    def test_brooks_node_coloring_regular(self):
        # Buduje graf 4-regularny planarny z Delta=4.
        # Graf jest 3-connected, dlatego algorytm dziala.
        self.G.add_edge(Edge(0, 2))
        self.G.add_edge(Edge(3, 5))
        self.G.add_edge(Edge(0, 5))
        algorithm = BrooksNodeColoring(self.G)
        algorithm.run()
        for node in self.G.iternodes():
            self.assertNotEqual(algorithm.color[node], None)
        for edge in self.G.iteredges():
            self.assertNotEqual(algorithm.color[edge.source],
                                algorithm.color[edge.target])
        #print algorithm.color
        all_colors = set(algorithm.color[node] for node in self.G.iternodes())
        self.assertEqual(len(all_colors), 3)  # best

    def test_exceptions(self):
        self.assertRaises(ValueError, BrooksNodeColoring,
            Graph(5, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
