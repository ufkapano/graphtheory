#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.coloring.nodecolorcs import ConnectedSequentialNodeColoring

# 0 --- 1 --- 2   outerplanar, chordal, 2-tree
# |   / |   / |
# |  /  |  /  |
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

    def test_cs_node_coloring(self):
        algorithm = ConnectedSequentialNodeColoring(self.G)
        algorithm.run()
        for node in self.G.iternodes():
            self.assertNotEqual(algorithm.color[node], None)
        for edge in self.G.iteredges():
            self.assertNotEqual(algorithm.color[edge.source],
                                algorithm.color[edge.target])
        all_colors = set(algorithm.color.values())
        self.assertTrue(len(all_colors) <= 4)
        # 3 in Py3, 4 in Py2, different order

    def test_exceptions(self):
        self.assertRaises(ValueError, ConnectedSequentialNodeColoring,
            Graph(5, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
