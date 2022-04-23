#!/usr/bin/env python3

import unittest
from fractions import Fraction
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.points import Point
from graphtheory.forests.treeplot import TreePlot
from graphtheory.forests.treeplot import TreePlotRadiusAngle

# 0     3
# |     |
# |     |
# 1 --- 4 --- 5 --- 6
# |
# |
# 2

class TestTreePlot(unittest.TestCase):

    def setUp(self):
        self.N = 7           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(1, 2), Edge(1, 4),
            Edge(3, 4), Edge(4, 5), Edge(5, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_tree_plot(self):
        self.assertEqual(self.G.e(), self.N-1)
        algorithm = TreePlot(self.G)
        algorithm.run()
        self.assertEqual(len(algorithm.point_dict), self.N)
        #print ( algorithm.point_dict )

    def test_tree_plot_radius_angle(self):
        self.assertEqual(self.G.e(), self.N-1)
        algorithm = TreePlotRadiusAngle(self.G)
        algorithm.run()
        self.assertEqual(len(algorithm.point_dict), self.N)
        #print ( algorithm.point_dict )
        self.assertEqual(algorithm.point_dict,
            {0: (2, Fraction(1, 2)),
            1: (1, Fraction(1, 1)), 
            2: (2, Fraction(3, 2)), 
            3: (1, Fraction(3, 1)), 
            4: (0, Fraction(3, 1)), 
            5: (1, Fraction(5, 1)), 
            6: (2, Fraction(5, 1))})

    def test_tree_three_nodes(self):
        T = Graph(3)
        for node in (0, 1, 2):
            T.add_node(node)
        for edge in (Edge(0, 1), Edge(1, 2)):
            T.add_edge(edge)
        algorithm = TreePlot(T)
        algorithm.run()
        self.assertEqual(len(algorithm.point_dict), 3)
        #print ( algorithm.point_dict )

    def test_tree_three_nodes_radius_angle(self):
        T = Graph(3)
        for node in (0, 1, 2):
            T.add_node(node)
        for edge in (Edge(0, 1), Edge(1, 2)):
            T.add_edge(edge)
        algorithm = TreePlotRadiusAngle(T)
        algorithm.run()
        self.assertEqual(len(algorithm.point_dict), 3)
        #print ( algorithm.point_dict )
        self.assertEqual(algorithm.point_dict,
            {0: (1, Fraction(3, 2)),
            1: (0, Fraction(3, 1)), 
            2: (1, Fraction(9, 2))})

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
