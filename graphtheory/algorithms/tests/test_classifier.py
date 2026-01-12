#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.algorithms.classifier import EdgeClassifierDFS

class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.619
        self.N = 8           # number of nodes
        self.G = Graph(directed=True)
        self.nodes = "syztxwvu"
        self.edges = [
            Edge("y", "x"), Edge("z", "y"), Edge("x", "z"), Edge("w", "x"), 
            Edge("z", "w"), Edge("s", "w"), Edge("v", "s"), Edge("v", "w"), 
            Edge("t", "v"), Edge("t", "u"), Edge("u", "t"), Edge("u", "v"), 
            Edge("s", "z"), ]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_classifier(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = EdgeClassifierDFS(self.G)
        algorithm.run()
        self.assertEqual(algorithm.parent["s"], None)
        self.assertEqual(algorithm.parent["t"], None)
        parent_expected = {'s': None, 'y': 'z', 'z': 'x', 't': None,
            'x': 'w', 'w': 's', 'v': 't', 'u': 't'}
        self.assertEqual(algorithm.parent, parent_expected)
        classifier_expected = {Edge('s', 'w'): 'TREE',
            Edge('w', 'x'): 'TREE', Edge('x', 'z'): 'TREE',
            Edge('z', 'y'): 'TREE', Edge('y', 'x'): 'BACK',
            Edge('z', 'w'): 'BACK', Edge('s', 'z'): 'FORWARD',
            Edge('t', 'v'): 'TREE', Edge('v', 's'): 'CROSS',
            Edge('v', 'w'): 'CROSS', Edge('t', 'u'): 'TREE',
            Edge('u', 't'): 'BACK', Edge('u', 'v'): 'CROSS'}
        self.assertEqual(algorithm.classifier, classifier_expected)
        #print(algorithm.parent)
        #print(algorithm.classifier)

    def tearDown(self): pass

class TestUndirectedGraph(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.619
        self.N = 8           # number of nodes
        self.G = Graph()
        self.nodes = "syztxwvu"
        self.edges = [
            Edge("y", "x"), Edge("z", "y"), Edge("x", "z"), Edge("w", "x"), 
            Edge("z", "w"), Edge("s", "w"), Edge("v", "s"), Edge("v", "w"), 
            Edge("t", "v"), Edge("t", "u"), Edge("u", "v"), Edge("s", "z"), ]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_classifier(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = EdgeClassifierDFS(self.G)
        algorithm.run()
        self.assertEqual(algorithm.parent["s"], None)
        parent_expected = {'s': None, 'y': 'x', 'z': 'y', 't': 'v',
            'x': 'w', 'w': 's', 'v': 'w', 'u': 't'}
        self.assertEqual(algorithm.parent, parent_expected)
        classifier_expected = {Edge('s', 'w'): 'TREE', Edge('w', 'x'): 'TREE',
            Edge('x', 'y'): 'TREE', Edge('y', 'z'): 'TREE',
            Edge('z', 'x'): 'BACK', Edge('z', 'w'): 'BACK',
            Edge('z', 's'): 'BACK', Edge('w', 'v'): 'TREE',
            Edge('v', 's'): 'BACK', Edge('v', 't'): 'TREE',
            Edge('t', 'u'): 'TREE', Edge('u', 'v'): 'BACK'}
        self.assertEqual(algorithm.classifier, classifier_expected)
        #print(algorithm.parent)
        #print(algorithm.classifier)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
