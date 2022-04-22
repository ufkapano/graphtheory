#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.algorithms.matching import MaximalMatching
from graphtheory.algorithms.matching import MaximalMatchingWithEdges
from graphtheory.algorithms.matching import MinimumWeightMatchingWithEdges


class TestMatching(unittest.TestCase):

    def setUp(self):
        # Wilson, ex. 25.1, bipartite graph
        # 0 : 4 5 6
        # 1 : 3 5
        # 2 : 3 4
        # ...
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 4), Edge(0, 5), Edge(0, 6), 
            Edge(1, 3), Edge(1, 5), Edge(2, 3), Edge(2, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_maximal_matching(self):
        algorithm = MaximalMatching(self.G)
        algorithm.run()
        # 5 solutions
        expected_cardinality = 2   # max 3
        expected_mate = {0: 4, 4: 0, 1: 3, 3: 1, 2: None, 5: None, 6: None}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        self.assertEqual(algorithm.mate, expected_mate)
        # Is it matching?
        for source in algorithm.mate:
            if algorithm.mate[source] is not None:
                target = algorithm.mate[source]
                self.assertEqual(algorithm.mate[target], source)

    def test_maximal_matching_with_edges(self):
        algorithm = MaximalMatchingWithEdges(self.G)
        algorithm.run()
        # 5 solutions
        expected_cardinality = 2   # max 3
        expected_mate = {0: Edge(0, 4), 1: Edge(1, 3), 2: None,
            3: Edge(3, 1), 4: Edge(4, 0), 5: None, 6: None}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        self.assertEqual(algorithm.mate, expected_mate)
        # Is it matching?
        for source in algorithm.mate:
            if algorithm.mate[source] is not None:
                edge = algorithm.mate[source]
                self.assertEqual(algorithm.mate[edge.target], ~edge)

    def tearDown(self): pass


class TestMatchingWithWeights(unittest.TestCase):

    def setUp(self):
        # Graf pelny z kolejnymi wagami.
        self.N = 4
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1, 5), Edge(0, 2, 7), Edge(0, 3, 2),
            Edge(1, 2, 3), Edge(1, 3, 6), Edge(2, 3, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_min_weight_matching(self):
        algorithm = MinimumWeightMatchingWithEdges(self.G)
        algorithm.run()
        expected_cardinality = 2
        expected_weight = 5
        expected_mate = {0: Edge(0, 3, 2), 1: Edge(1, 2, 3),
            2: Edge(2, 1, 3), 3: Edge(3, 0, 2)}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        # Krawedzie sa po dwa razy w slowniku.
        weight = sum(algorithm.mate[node].weight
            for node in algorithm.mate if algorithm.mate[node]) // 2
        self.assertEqual(weight, expected_weight)
        self.assertEqual(algorithm.mate, expected_mate)
        # Is it matching?
        for source in algorithm.mate:
            if algorithm.mate[source] is not None:
                edge = algorithm.mate[source]
                self.assertEqual(algorithm.mate[edge.target], ~edge)

    def tearDown(self): pass


class TestMatchingWithWeights2(unittest.TestCase):

    def setUp(self):
        # Graf pelny z kolejnymi wagami.
        self.N = 4
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1, 4), Edge(0, 2, 3), Edge(0, 3, 2),
            Edge(1, 2, 7), Edge(1, 3, 5), Edge(2, 3, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_min_weight_matching(self):
        algorithm = MinimumWeightMatchingWithEdges(self.G)
        algorithm.run()
        expected_cardinality = 2
        expected_weight = 9   # best minimum 8
        # Best solution.
        #expected_mate = {0: Edge(0, 2, 3), 1: Edge(1, 3, 5),
        #    2: Edge(2, 0, 3), 3: Edge(3, 1, 5)}
        expected_mate = {0: Edge(0, 3, 2), 1: Edge(1, 2, 7),
            2: Edge(2, 1, 7), 3: Edge(3, 0, 2)}
        self.assertEqual(algorithm.cardinality, expected_cardinality)
        # Krawedzie sa po dwa razy w slowniku.
        weight = sum(algorithm.mate[node].weight
            for node in algorithm.mate if algorithm.mate[node]) // 2
        self.assertEqual(weight, expected_weight)
        self.assertEqual(algorithm.mate, expected_mate)
        # Is it matching?
        for source in algorithm.mate:
            if algorithm.mate[source] is not None:
                edge = algorithm.mate[source]
                self.assertEqual(algorithm.mate[edge.target], ~edge)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
