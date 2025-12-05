#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.cliques.bronkerbosch import BronKerboschClassic
from graphtheory.cliques.bronkerboschrp import BronKerboschRandomPivot
from graphtheory.cliques.bronkerboschdp import BronKerboschDegreePivot
from graphtheory.cliques.bronkerboschdeg import BronKerboschDegeneracy

# 0---1---2---3   maximum clique {2, 3, 5}
#     |   | /
#     4---5

class TestBronKerbosch(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph()
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(1, 4), Edge(2, 3),
            Edge(2, 5), Edge(3, 5), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_bron_kerbosch_classic(self):
        algorithm = BronKerboschClassic(self.G)
        algorithm.run()
        cliques_expected = [{0, 1}, {1, 2}, {1, 4}, {4, 5}, {2, 3, 5}]
        self.assertEqual(len(algorithm.cliques), len(cliques_expected))
        # Mozna bardziej dokladnie sprawdzic przez sortowanie klik.
        cliques = sorted(algorithm.cliques, key=len)
        self.assertEqual(cliques, cliques_expected)

    def test_bron_kerbosch_random_pivot(self):
        algorithm = BronKerboschRandomPivot(self.G)
        algorithm.run()
        cliques_expected = [{0, 1}, {1, 2}, {1, 4}, {4, 5}, {2, 3, 5}]
        self.assertEqual(len(algorithm.cliques), len(cliques_expected))
        # Mozna bardziej dokladnie sprawdzic przez sortowanie klik.
        cliques = sorted(algorithm.cliques, key=len)
        self.assertEqual(cliques, cliques_expected)

    def test_bron_kerbosch_degree_pivot(self):
        algorithm = BronKerboschDegreePivot(self.G)
        algorithm.run()
        cliques_expected = [{0, 1}, {1, 2}, {1, 4}, {4, 5}, {2, 3, 5}]
        self.assertEqual(len(algorithm.cliques), len(cliques_expected))
        # Mozna bardziej dokladnie sprawdzic przez sortowanie klik.
        cliques = sorted(algorithm.cliques, key=len)
        self.assertEqual(cliques, cliques_expected)

    def test_bron_kerbosch_degeneracy(self):
        algorithm = BronKerboschDegeneracy(self.G)
        algorithm.run()
        cliques_expected = [{0, 1}, {1, 4}, {1, 2}, {4, 5}, {2, 3, 5}]
        self.assertEqual(len(algorithm.cliques), len(cliques_expected))
        # Mozna bardziej dokladnie sprawdzic przez sortowanie klik.
        cliques = sorted(algorithm.cliques, key=len)
        self.assertEqual(cliques, cliques_expected)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
