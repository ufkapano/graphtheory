#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.points import Point
from graphtheory.forests.treeplot import TreePlot

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

    def test_treeplot(self):
        self.assertEqual(self.G.e(), self.N-1)
        algorithm = TreePlot(self.G)
        algorithm.run()
        self.assertEqual(len(algorithm.point_dict), self.N)
        #print algorithm.point_dict

    def test_tree_two_nodes(self):
        T = Graph(2)
        T.add_node(0)
        T.add_node(1)
        T.add_edge(Edge(0, 1))
        algorithm = TreePlot(T)
        algorithm.run()
        self.assertEqual(len(algorithm.point_dict), 2)
        #print algorithm.point_dict

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
