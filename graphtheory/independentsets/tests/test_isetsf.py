#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet1
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet2
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet3
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet4
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet5
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet6
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet7

# 0 --- 1 --- 2 nie jest dwudzielny, bo sa trojkaty
# |   / |     |
# |  /  |     | Niezalezne: 0, 4, 2 (najlepszy)
# | /   |     |
# 3 --- 4 --- 5

class TestIndependentSet(unittest.TestCase):

    def setUp(self):
        self.N = 6
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(0, 3), Edge(1, 3), Edge(1, 4), 
            Edge(1, 2), Edge(2, 5), Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_sf_independent_set1(self):
        algorithm = SmallestFirstIndependentSet1(self.G)
        #algorithm.run()   # przypadkiem znajduje najlepsze rozwiazanie
        algorithm.run(3)   # znajduje set([2, 3])
        for edge in self.G.iteredges():
            self.assertFalse(edge.source in algorithm.independent_set
                         and edge.target in algorithm.independent_set)
        self.assertEqual(algorithm.cardinality, len(algorithm.independent_set))
        #print algorithm.independent_set

    def test_sf_independent_set2(self):
        algorithm = SmallestFirstIndependentSet2(self.G)
        #algorithm.run()   # przypadkiem znajduje najlepsze rozwiazanie
        algorithm.run(3)   # znajduje set([2, 3])
        for edge in self.G.iteredges():
            self.assertFalse(edge.source in algorithm.independent_set
                         and edge.target in algorithm.independent_set)
        self.assertEqual(algorithm.cardinality, len(algorithm.independent_set))
        #print algorithm.independent_set

    def test_sf_independent_set3(self):
        algorithm = SmallestFirstIndependentSet3(self.G)
        #algorithm.run()   # przypadkiem znajduje najlepsze rozwiazanie
        algorithm.run(3)   # znajduje set([2, 3])
        for edge in self.G.iteredges():
            self.assertFalse(algorithm.independent_set[edge.source]
                         and algorithm.independent_set[edge.target])
        cardinality = sum(1 for node in self.G if algorithm.independent_set[node])
        self.assertEqual(algorithm.cardinality, cardinality)
        #print algorithm.independent_set

    def test_sf_independent_set4(self):
        algorithm = SmallestFirstIndependentSet4(self.G)
        #algorithm.run()   # przypadkiem znajduje najlepsze rozwiazanie
        algorithm.run(3)   # znajduje set([2, 3])
        for edge in self.G.iteredges():
            self.assertFalse(edge.source in algorithm.independent_set
                         and edge.target in algorithm.independent_set)
        self.assertEqual(algorithm.cardinality, len(algorithm.independent_set))
        #print algorithm.independent_set

    def test_sf_independent_set5(self):
        algorithm = SmallestFirstIndependentSet5(self.G)
        #algorithm.run()   # przypadkiem znajduje najlepsze rozwiazanie
        algorithm.run(3)   # znajduje set([2, 3])
        for edge in self.G.iteredges():
            self.assertFalse(edge.source in algorithm.independent_set
                         and edge.target in algorithm.independent_set)
        self.assertEqual(algorithm.cardinality, len(algorithm.independent_set))
        #print algorithm.independent_set

    def test_sf_independent_set6(self):
        algorithm = SmallestFirstIndependentSet6(self.G)
        #algorithm.run()   # przypadkiem znajduje najlepsze rozwiazanie
        algorithm.run(3)   # znajduje set([2, 3])
        for edge in self.G.iteredges():
            self.assertFalse(algorithm.independent_set[edge.source]
                         and algorithm.independent_set[edge.target])
        cardinality = sum(1 for node in self.G if algorithm.independent_set[node])
        self.assertEqual(algorithm.cardinality, cardinality)
        #print algorithm.independent_set

    def test_sf_independent_set7(self):
        algorithm = SmallestFirstIndependentSet7(self.G)
        #algorithm.run()   # przypadkiem znajduje najlepsze rozwiazanie
        algorithm.run(3)   # znajduje set([2, 3])
        for edge in self.G.iteredges():
            self.assertFalse(edge.source in algorithm.independent_set
                         and edge.target in algorithm.independent_set)
        self.assertEqual(algorithm.cardinality, len(algorithm.independent_set))
        #print algorithm.independent_set

    def test_exceptions(self):
        self.assertRaises(ValueError, SmallestFirstIndependentSet1,
            Graph(5, directed=True))
        self.assertRaises(ValueError, SmallestFirstIndependentSet2,
            Graph(5, directed=True))
        self.assertRaises(ValueError, SmallestFirstIndependentSet3,
            Graph(5, directed=True))
        self.assertRaises(ValueError, SmallestFirstIndependentSet4,
            Graph(5, directed=True))
        self.assertRaises(ValueError, SmallestFirstIndependentSet5,
            Graph(5, directed=True))
        self.assertRaises(ValueError, SmallestFirstIndependentSet6,
            Graph(5, directed=True))
        self.assertRaises(ValueError, SmallestFirstIndependentSet7,
            Graph(5, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
