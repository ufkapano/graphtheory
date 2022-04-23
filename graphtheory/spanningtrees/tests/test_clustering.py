#!/usr/bin/env python3

import unittest
from graphtheory.structures.points import Point
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.spanningtrees.clustering import KruskalClustering


class TestKruskalClustering(unittest.TestCase):
#
# . . . . o .
# . . . o . .
# o o . . . .
# . . . . . .
# o o . . o o
    def setUp(self):
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = [Point(0, 0), Point(1, 0), Point(0, 2), Point(1, 2),
            Point(4, 0), Point(5, 0), Point(3, 3), Point(4, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for p1 in self.nodes:
            for p2 in self.nodes:
                if p1 < p2:
                    #print (p1, p2)
                    self.G.add_edge(Edge(p1, p2, (p1-p2).length()))

    def test_clustering(self):
        self.assertEqual(self.G.v(), self.N)
        n_clusters = 4
        algorithm = KruskalClustering(self.G, n_clusters)
        algorithm.run()
        #print ( algorithm.clusters )
        self.assertEqual(len(algorithm.clusters), n_clusters)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
