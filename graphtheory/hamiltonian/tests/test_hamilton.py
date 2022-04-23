#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.hamiltonian.hamilton import *

# 0 --------- 5
# | \       / |
# |  1 --- 4  |
# | /       \ |
# 2 --------- 3

class TestHamiltonianCycle(unittest.TestCase):

    def setUp(self):
        # 3-prism graph, Halin graph
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(0, 2), Edge(0, 5), Edge(1, 2),
            Edge(1, 4), Edge(2, 3), Edge(3, 4), Edge(3, 5), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_hamilton(self):
        algorithm = HamiltonianCycleDFS(self.G)
        algorithm.run(0)
        # 5 solutions
        expected_cycle = [0, 1, 2, 3, 4, 5, 0]
        self.assertEqual(algorithm.hamiltonian_cycle, expected_cycle)

    def test_hamilton_with_edges(self):
        algorithm = HamiltonianCycleDFSWithEdges(self.G)
        algorithm.run(0)
        # 5 solutions
        expected_cycle = [
            Edge(0, 1), Edge(1, 2), Edge(2, 3),
            Edge(3, 4), Edge(4, 5), Edge(5, 0)]
        self.assertEqual(algorithm.hamiltonian_cycle, expected_cycle)

    def test_hamilton_with_cycle_graph(self):
        algorithm = HamiltonianCycleDFSWithGraph(self.G)
        algorithm.run(0)
        # 5 solutions
        expected_cycle = [
            Edge(0, 1), Edge(1, 2), Edge(2, 3),
            Edge(3, 4), Edge(4, 5), Edge(5, 0)]
        #print "undirected", list(algorithm.hamiltonian_cycle.iteredges())
        for edge in expected_cycle:
            self.assertTrue(algorithm.hamiltonian_cycle.has_edge(edge))

    def tearDown(self): pass

# 0 ----------o 5
# o \         o |
# |  o       /  |
# |   1 --o 4   |
# |  o       o  |
# | /         \ o
# 2 o---------- 3

class TestHamiltonianCycleDirected(unittest.TestCase):

    def setUp(self):
        # 3-prism graph, Halin graph
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(2, 0), Edge(0, 5), Edge(2, 1),
            Edge(1, 4), Edge(3, 2), Edge(3, 4), Edge(5, 3), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_hamilton(self):
        algorithm = HamiltonianCycleDFS(self.G)
        algorithm.run(0)
        expected_cycle = [0, 1, 4, 5, 3, 2, 0]
        self.assertEqual(algorithm.hamiltonian_cycle, expected_cycle)

    def test_hamilton_with_edges(self):
        algorithm = HamiltonianCycleDFSWithEdges(self.G)
        algorithm.run(0)
        expected_cycle = [
            Edge(0, 1), Edge(1, 4), Edge(4, 5),
            Edge(5, 3), Edge(3, 2), Edge(2, 0)]
        self.assertEqual(algorithm.hamiltonian_cycle, expected_cycle)

    def test_hamilton_with_cycle_graph(self):
        algorithm = HamiltonianCycleDFSWithGraph(self.G)
        algorithm.run(0)
        # 5 solutions
        expected_cycle = [
            Edge(0, 1), Edge(1, 4), Edge(4, 5),
            Edge(5, 3), Edge(3, 2), Edge(2, 0)]
        #print "directed", list(algorithm.hamiltonian_cycle.iteredges())
        for edge in expected_cycle:
            self.assertTrue(algorithm.hamiltonian_cycle.has_edge(edge))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
