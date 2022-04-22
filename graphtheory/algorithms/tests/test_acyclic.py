#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.algorithms.acyclic import AcyclicGraphDFS
from graphtheory.algorithms.acyclic import is_acyclic

# r---s   t---u   cycles are present
# |   | / | / |
# v   w---x---y

# r---s   t   u   without cycles
# |   | / | /
# v   w   x---y

class TestAcyclicUdirectedGraph(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607 changed.
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 4), Edge(0, 1), Edge(1, 5), Edge(5, 2), Edge(2, 6), 
            Edge(6, 3), Edge(6, 7)]
        self.cycle_edges = [Edge(5, 6), Edge(2, 3), Edge(3, 7)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_detect_no_cycles(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = AcyclicGraphDFS(self.G)
        algorithm.run(1)   # it is safe, because G is connected
        parent_expected = {1: None, 0: 1, 3: 6, 2: 5, 5: 1, 4: 0, 7: 6, 6: 2}
        self.assertEqual(algorithm.parent, parent_expected)
        self.assertTrue(is_acyclic(self.G))

    def test_detect_cycle1(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[0])
        algorithm = AcyclicGraphDFS(self.G)
        self.assertRaises(ValueError, algorithm.run)
        self.assertFalse(is_acyclic(self.G))

    def test_detect_cycle2(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[1])
        algorithm = AcyclicGraphDFS(self.G)
        self.assertRaises(ValueError, algorithm.run)
        self.assertFalse(is_acyclic(self.G))

    def test_detect_cycle3(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[2])
        algorithm = AcyclicGraphDFS(self.G)
        self.assertRaises(ValueError, algorithm.run)
        self.assertFalse(is_acyclic(self.G))

    def tearDown(self): pass

#     0----------+
#     | \        |
#     o  o       |
# +--o1   4      |
# |   |    \     |
# |   o     o    o
# |   2o-----5--o7
# |   |      |
# |   o      o
# +---3      6

class TestAcyclicDirectedGraph(unittest.TestCase):

    def setUp(self):
        # The graph from
        self.N = 8           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(0, 4), Edge(4, 5), 
            Edge(5, 6), Edge(5, 7), Edge(5, 2), Edge(0, 7)]
        self.cycle_edges = [Edge(3, 1), Edge(5, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_detect_no_directed_cycles(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = AcyclicGraphDFS(self.G)
        algorithm.run(0)   # in order to easy test
        parent_expected = {0: None, 2: 1, 1: 0, 4: 0, 3: 2, 6: 5, 5: 4, 7: 5}
        #parent_expected = {0: None, 2: 1, 1: 0, 4: 0, 3: 2, 6: 5, 5: 4, 7: 0}
        self.assertEqual(algorithm.parent, parent_expected)
        self.assertTrue(is_acyclic(self.G))

    def test_detect_directed_cycle1(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[0])
        algorithm = AcyclicGraphDFS(self.G)
        self.assertRaises(ValueError, algorithm.run)
        self.assertFalse(is_acyclic(self.G))

    def test_detect_directed_cycle2(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[1])
        algorithm = AcyclicGraphDFS(self.G)
        self.assertRaises(ValueError, algorithm.run)
        self.assertFalse(is_acyclic(self.G))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
