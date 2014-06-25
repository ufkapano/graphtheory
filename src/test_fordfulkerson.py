#!/usr/bin/python

import unittest
from fordfulkerson import FordFulkerson
from graphs import Graph
from edges import Edge

#     10
#  A ---> B
#  |   /  |
#10|  /1  |10
# .| /.   |.
#  C ---> D
#     10

class TestFordFulkerson(unittest.TestCase):

    def setUp(self):
        self.N = 4           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["A", "B", "C", "D"]
        self.edges = [
        Edge("A", "B", 10), 
        Edge("A", "C", 10),
        Edge("B", "C", 1), 
        Edge("B", "D", 10), 
        Edge("C", "D", 10)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        self.G.show()

    def test_fordfulkerson(self):
        algorithm = FordFulkerson(self.G)
        algorithm.run("A", "D")
        expected_max_flow = 20
        expected_flow = {
        'A': {'A': 0, 'C': 10, 'B': 10, 'D': 0}, 
        'B': {'A': -10, 'C': 0, 'B': 0, 'D': 10}, 
        'C': {'A': -10, 'C': 0, 'B': 0, 'D': 10}, 
        'D': {'A': 0, 'C': -10, 'B': -10, 'D': 0}}
        self.assertEqual(algorithm.max_flow, expected_max_flow)
        self.assertEqual(algorithm.flow, expected_flow)

class TestFordFulkersonWiki(unittest.TestCase):

    def setUp(self):
        self.N = 7           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["A", "B", "C", "D", "E", "F", "G"]
        self.edges = [
        Edge("A", "B", 3), 
        Edge("A", "D", 3),
        Edge("B", "C", 4), 
        Edge("C", "A", 3), 
        Edge("C", "D", 1), 
        Edge("C", "E", 2), 
        Edge("D", "E", 2), 
        Edge("D", "F", 6), 
        Edge("E", "B", 1), 
        Edge("E", "G", 1), 
        Edge("F", "G", 9)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        self.G.show()

    def test_wiki(self):
        algorithm = FordFulkerson(self.G)
        algorithm.run("A", "G")
        expected_max_flow = 5
        expected_flow = {
        'A': {'A': 0, 'C': 0, 'B': 2, 'E': 0, 'D': 3, 'G': 0, 'F': 0}, 
        'B': {'A': -2, 'C': 2, 'B': 0, 'E': 0, 'D': 0, 'G': 0, 'F': 0}, 
        'C': {'A': 0, 'C': 0, 'B': -2, 'E': 1, 'D': 1, 'G': 0, 'F': 0}, 
        'D': {'A': -3, 'C': -1, 'B': 0, 'E': 0, 'D': 0, 'G': 0, 'F': 4}, 
        'E': {'A': 0, 'C': -1, 'B': 0, 'E': 0, 'D': 0, 'G': 1, 'F': 0}, 
        'F': {'A': 0, 'C': 0, 'B': 0, 'E': 0, 'D': -4, 'G': 4, 'F': 0}, 
        'G': {'A': 0, 'C': 0, 'B': 0, 'E': -1, 'D': 0, 'G': 0, 'F': -4}}
        self.assertEqual(algorithm.max_flow, expected_max_flow)
        self.assertEqual(algorithm.flow, expected_flow)

if __name__ == "__main__":

    unittest.main()
