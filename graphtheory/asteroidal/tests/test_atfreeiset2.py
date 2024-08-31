#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.asteroidal.atfreeiset2 import ATFreeIndependentSet


class TestATFreeIndependentSet(unittest.TestCase):

    def setUp(self): pass

    def test_c4(self):
        G = Graph(directed=False)
        for edge in [Edge(0,1), Edge(1,2), Edge(2,3), Edge(0,3)]:
            G.add_edge(edge)
        algorithm = ATFreeIndependentSet(G)
        algorithm.run()
        self.assertTrue(algorithm.independent_set in [{0, 2}, {1, 3}])
        self.assertEqual(algorithm.cardinality, 2)

    def test_c5(self):
        G = Graph(directed=False)
        for edge in [Edge(0,1), Edge(1,2), Edge(2,3), Edge(3,4), Edge(0,4)]:
            G.add_edge(edge)
        algorithm = ATFreeIndependentSet(G)
        algorithm.run()
        self.assertEqual(algorithm.independent_set, {0, 3}) # other possible
        self.assertEqual(algorithm.cardinality, 2)

# 1---4---5---6
# |   | /
# 2---3
    def test_house_with_edge(self):
        G = Graph(directed=False)
        edges = [Edge("1", "2"), Edge("1", "4"), Edge("2", "3"),
            Edge("3", "4"), Edge("4", "5"), Edge("3", "5"), Edge("5", "6")]
        for edge in edges:
            G.add_edge(edge)
        algorithm = ATFreeIndependentSet(G)
        algorithm.run()
        self.assertEqual(algorithm.independent_set, {'1','6','3'}) # other possible
        self.assertEqual(algorithm.cardinality, 3)

# 2-------3   numeracja wg cyklu Hamiltona
# |\     /|   3-prism graph
# | 1---4 |   cubic, planar
# |/     \|
# 0-------5
    def test_3prism(self):
        G = Graph(directed=False)
        edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(3, 4), 
            Edge(4, 5), Edge(0, 5), Edge(1, 4), Edge(2, 0), Edge(3, 5)]
        for edge in edges:
            G.add_edge(edge)
        algorithm = ATFreeIndependentSet(G)
        algorithm.run()
        self.assertEqual(algorithm.independent_set, {0, 4}) # other possible
        self.assertEqual(algorithm.cardinality, 2)
        #print(algorithm.independent_set)

# 0---1---2---3---4---5---6---7---8
# |   |   |   | X   X |   |   |   |
# 9--10--11--12--13--14--15--16--17
    def test_n18(self):
        G = Graph(directed=False)
        nodes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17"]
        edges = [Edge("0", "1"), Edge("1", "2"), Edge("2", "3"),
            Edge("3", "4"), Edge("4", "5"), Edge("5", "6"),
            Edge("6", "7"), Edge("7", "8"), Edge("8", "17"),
            Edge("17", "16"), Edge("16", "15"), Edge("15", "14"),
            Edge("14", "13"), Edge("13", "12"), Edge("12", "11"),
            Edge("11", "10"), Edge("10", "9"), Edge("9", "0"),
            Edge("1", "10"), Edge("2", "11"), Edge("3", "12"),
            Edge("5", "14"), Edge("6", "15"), Edge("7", "16"),
            Edge("3", "13"), Edge("13", "5"), Edge("14", "4"),
            Edge("4", "12")]
        for node in nodes:
            G.add_node(node)
        for edge in edges:
            G.add_edge(edge)
        algorithm = ATFreeIndependentSet(G)
        algorithm.run()
        #print(algorithm.independent_set)
        self.assertEqual(algorithm.cardinality, 8)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
