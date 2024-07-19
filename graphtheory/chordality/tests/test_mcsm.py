#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.mcsm import MCS_M

class TestMCSM(unittest.TestCase):

    def setUp(self): pass

    def test_c5(self):
        G = Graph()   # C_5
        edge_list = [Edge("A","B"), Edge("B","C"), Edge("C","D"),
            Edge("D","E"), Edge("A","E")]
        for edge in edge_list:
            G.add_edge(edge)
        #G.show()
        algorithm = MCS_M(G)
        algorithm.run()
        #print("C_5 graph ...")
        #print(algorithm.order)   # ['D', 'C', 'E', 'B', 'A']
        #print(algorithm.new_edges)   # [Edge('B', 'E'), Edge('E', 'C')]
        self.assertEqual(len(algorithm.order), G.v())
        self.assertEqual(len(algorithm.new_edges), 2) # best possible

#   ----J----
#  /         \
# F---G       H---I
# |     \   /     |
# A---B---C---D---E
    def test_berry(self):
        G = Graph()   # graph from [2004 Berry]
        edge_list = [Edge("A","B"),Edge("B","C"),Edge("C","G"),Edge("G","F"),
            Edge("A","F"),Edge("C","D"),Edge("D","E"),Edge("E","I"),
            Edge("I","H"),Edge("C","H"),Edge("F","J"),Edge("H","J"),]
        for edge in edge_list:
            G.add_edge(edge)
        #G.show()
        algorithm = MCS_M(G)
        algorithm.run()
        #print("Berry graph ...")
        #print(algorithm.order)
        # ['E', 'I', 'D', 'H', 'J', 'G', 'C', 'F', 'B', 'A']
        #print(algorithm.new_edges)
        # [Edge('B', 'F'), Edge('F', 'C'), Edge('C', 'J'), Edge('H', 'D'),
        # Edge('D', 'I')]
        self.assertEqual(len(algorithm.order), G.v())
        self.assertEqual(len(algorithm.new_edges), 5) # best possible

# A---B---C
# |   |   |
# D---E---F
# |   |   |
# G---H---I
    def test_grid_3x3(self):
        G = Graph()   # grid graph
        edge_list = [Edge("A","B"),Edge("B","C"),Edge("A","D"),Edge("B","E"),
            Edge("C","F"),Edge("D","E"),Edge("E","F"),Edge("D","G"),
            Edge("E","H"),Edge("F","I"),Edge("G","H"),Edge("H","I"),]
        for edge in edge_list:
            G.add_edge(edge)
        #G.show()
        algorithm = MCS_M(G)
        algorithm.run()
        #print("grid graph 3x3 ...")
        #print(algorithm.order)
        # ['I', 'H', 'F', 'G', 'E', 'C', 'D', 'B', 'A']
        #print(algorithm.new_edges)
        # [Edge('B', 'D'), Edge('D', 'C'), Edge('C', 'G'), Edge('C', 'E'),
        # Edge('E', 'G'), Edge('G', 'F'), Edge('F', 'H')]
        self.assertEqual(len(algorithm.order), G.v())
        self.assertEqual(len(algorithm.new_edges), 7)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
