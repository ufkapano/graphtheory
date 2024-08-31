#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.asteroidal.atfreedset import ATFreeDominatingSet


class TestATFreeDominatingSet(unittest.TestCase):

    def setUp(self): pass

# 1-------0   dsets 1|2|5 plus 0|3|4
# |\     /|
# | 2---3 |
# |/     \|
# 5-------4
    def test_Halin_3prism(self):
        G = Graph(directed=False)
        edges = {Edge(0, 1), Edge(1, 2), Edge(2, 3),
            Edge(3, 0), Edge(4, 5), Edge(0, 4),
            Edge(3, 4), Edge(5, 1), Edge(2, 5)}
        for edge in edges:
            G.add_edge(edge)
        self.assertEqual(set(G.iternodes()), set(range(6)))
        algorithm = ATFreeDominatingSet(G)
        algorithm.run()
        dsets = [{1,0},{1,3},{1,4},{2,0},{2,3},{2,4},{5,0},{5,3},{5,4}]
        self.assertTrue(algorithm.dominating_set in dsets)
        self.assertEqual(algorithm.cardinality, 2)

# 1---4---5---6   dsets {5,1} {5,2}
# |   | /
# 2---3
    def test_house_with_edge(self):
        G = Graph(directed=False)
        edges = [Edge("1", "2"), Edge("1", "4"), Edge("2", "3"),
            Edge("3", "4"), Edge("4", "5"), Edge("3", "5"), Edge("5", "6")]
        for edge in edges:
            G.add_edge(edge)
        self.assertEqual(set(G.iternodes()), set("123456"))
        algorithm = ATFreeDominatingSet(G)
        algorithm.run()
        dsets = [{"5", "1"}, {"5", "2"}]
        self.assertTrue(algorithm.dominating_set in dsets)
        self.assertEqual(algorithm.cardinality, 2)

# 1---4---5   dsets {3,4} {1,6} {2,5}
# |   |   |
# 2---3---6
    def test_ladder_n6(self):
        G = Graph(directed=False)
        edges = [Edge("1", "2"), Edge("1", "4"), Edge("2", "3"),
            Edge("3", "4"), Edge("4", "5"), Edge("3", "6"), Edge("5", "6")]
        for edge in edges:
            G.add_edge(edge)
        self.assertEqual(set(G.iternodes()), set("123456"))
        algorithm = ATFreeDominatingSet(G)
        algorithm.run()
        dsets = [{"3", "4"}, {"1", "6"}, {"2", "5"}]
        self.assertTrue(algorithm.dominating_set in dsets)
        self.assertEqual(algorithm.cardinality, 2)

# 0---1---2---3---4   dsets {0,7,4} {5,2,9}
# |   |   |   |   |
# 5---6---7---8---9
    def test_ladder_n10(self):
        G = Graph(directed=False)
        edges = [Edge(0,1), Edge(1,2), Edge(2,3), Edge(3,4),
            Edge(0,5), Edge(1,6), Edge(2,7), Edge(3,8), Edge(4,9),
            Edge(5,6), Edge(6,7), Edge(7,8), Edge(8,9),]
        for edge in edges:
            G.add_edge(edge)
        self.assertEqual(set(G.iternodes()), set(range(10)))
        algorithm = ATFreeDominatingSet(G)
        algorithm.run()
        dsets = [{0,7,4}, {5,2,9}]
        self.assertTrue(algorithm.dominating_set in dsets)
        self.assertEqual(algorithm.cardinality, 3)

# 0---2---4---6---8   dsets {2,6} {2,7}
# | / | / | / | /     2-tree
# 1---3---5---7
    def test_interval_2tree_n9(self):
        G = Graph(directed=False)
        edges = [Edge(0,1), Edge(0,2), Edge(1,2), Edge(1,3), Edge(2,3), 
            Edge(2,4), Edge(3,4), Edge(3,5), Edge(4,5), Edge(4,6), 
            Edge(5,6), Edge(5,7), Edge(6,7), Edge(6,8), Edge(7,8)]
        for edge in edges:
            G.add_edge(edge)
        self.assertEqual(set(G.iternodes()), set(range(9)))
        algorithm = ATFreeDominatingSet(G)
        algorithm.run()
        dsets = [{2,6}, {2,7}]
        self.assertTrue(algorithm.dominating_set in dsets)
        self.assertEqual(algorithm.cardinality, 2)

# 0---1---2---3---4---5   dset {1,4}
    def test_path_n6(self):
        G = Graph(directed=False)
        for edge in [Edge(0,1), Edge(1,2), Edge(2,3), Edge(3,4), Edge(4,5)]:
            G.add_edge(edge)
        self.assertEqual(set(G.iternodes()), set(range(6)))
        algorithm = ATFreeDominatingSet(G)
        algorithm.run()
        self.assertEqual(algorithm.dominating_set, {1,4})
        self.assertEqual(algorithm.cardinality, 2)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
