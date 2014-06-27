#!/usr/bin/python

import unittest
from edmondskarp import *
from graphs import Graph
from edges import Edge

#     10
#  A ---> B
#  |   /  |
#10|  /1  |10
# .| /.   |.
#  C ---> D
#     10

class TestEdmondsKarp(unittest.TestCase):

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
        #self.G.show()

    def test_edmondskarp(self):
        algorithm = EdmondsKarp(self.G)
        algorithm.run("A", "D")
        expected_max_flow = 20
        expected_flow = {
        'A': {'A': 0, 'C': 10, 'B': 10, 'D': 0}, 
        'B': {'A': -10, 'C': 0, 'B': 0, 'D': 10}, 
        'C': {'A': -10, 'C': 0, 'B': 0, 'D': 10}, 
        'D': {'A': 0, 'C': -10, 'B': -10, 'D': 0}}
        self.assertEqual(algorithm.max_flow, expected_max_flow)
        self.assertEqual(algorithm.flow, expected_flow)

    def test_edmondskarp_sparse(self):
        algorithm = EdmondsKarpSparse(self.G)
        algorithm.run("A", "D")
        expected_max_flow = 20
        expected_flow = {
        'A': {'C': 10, 'B': 10}, 
        'B': {'A': -10, 'D': 10}, 
        'C': {'A': -10, 'D': 10}, 
        'D': {'C': -10, 'B': -10}}
        self.assertEqual(algorithm.max_flow, expected_max_flow)
        self.assertEqual(algorithm.flow, expected_flow)


class TestEdmondsKarpWiki(unittest.TestCase):

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
        #self.G.show()

    def test_wiki_sparse(self):
        algorithm = EdmondsKarpSparse(self.G)
        algorithm.run("A", "G")
        expected_max_flow = 5
        expected_flow = {
        'A': {'B': 2, 'D': 3}, 
        'B': {'A': -2, 'C': 2}, 
        'C': {'B': -2, 'E': 1, 'D': 1}, 
        'D': {'A': -3, 'C': -1, 'E': 0, 'F': 4}, 
        'E': {'C': -1, 'D': 0, 'G': 1}, 
        'F': {'D': -4, 'G': 4}, 
        'G': {'E': -1, 'F': -4}}
        self.assertEqual(algorithm.max_flow, expected_max_flow)
        self.assertEqual(algorithm.flow, expected_flow)

if __name__ == "__main__":

    unittest.main()
