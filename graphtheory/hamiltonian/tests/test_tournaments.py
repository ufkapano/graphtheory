#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.hamiltonian.tournaments import is_transitive
from graphtheory.hamiltonian.tournaments import find_hamiltonian_path


class TestTournaments(unittest.TestCase):

    def setUp(self):
        self.N = 5           # number of nodes
        graph_factory = GraphFactory(Graph)
        self.G = graph_factory.make_complete(self.N, True)
        #self.G.show()

    def test_is_transitive(self):
        outdegrees = sorted(self.G.outdegree(node)
            for node in self.G.iternodes())
        if is_transitive(self.G):
            self.assertEqual(outdegrees, list(range(self.N)))

    def test_find_hamiltonian_path(self):
        path = find_hamiltonian_path(self.G)
        for i in range(self.N-1):
            self.assertTrue(self.G.has_edge(Edge(path[i], path[i+1])))

    def test_exceptions(self):
        self.assertRaises(ValueError, is_transitive, Graph(1, False))
        self.assertRaises(ValueError, find_hamiltonian_path, Graph(1, False))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
