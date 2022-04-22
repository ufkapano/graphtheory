#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.algorithms.acyclic import is_acyclic
from graphtheory.connectivity.connected import is_connected
from graphtheory.traversing.bfs import SimpleBFS
from graphtheory.chordality.tdtools import find_treewidth_min_deg # upper bound
from graphtheory.chordality.tdtools import find_treewidth_mmd # lower bound

# https://en.wikipedia.org/wiki/Tree_decomposition
#
# A---B---F     outerplanar graph
# | / | \ |     treewidth = 2
# C   |   G
# | \ | / |
# D---E---H
#
# (A,B,C)   (B,F,G)   tree decomposition
#    |         |
# (B,C,E)---(B,E,G)
#    |         |
# (C,D,E)   (E,G,H)

class TestTreeDecomposition(unittest.TestCase):

    def setUp(self):
        self.N = 8     # number of nodes
        self.G = Graph(self.N)
        self.nodes = list("ABCDEFGH")
        self.edges = [
            Edge("A", "B"), Edge("A", "C"), Edge("B", "C"), Edge("B", "F"), 
            Edge("B", "G"), Edge("C", "D"), Edge("C", "E"), Edge("D", "E"), 
            Edge("E", "G"), Edge("E", "H"), Edge("F", "G"), Edge("G", "H"),
            Edge("B", "E")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        self.T = Graph(6)   # tree decomposition
        b0 = ("A", "B", "C")
        b1 = ("B", "C", "E")
        b2 = ("C", "D", "E")
        b3 = ("B", "E", "G")
        b4 = ("B", "F", "G")
        b5 = ("E", "G", "H")
        bags = [b0, b1, b2, b3, b4, b5]
        tdedges = [Edge(b0, b1), Edge(b1, b2), Edge(b1, b3), Edge(b3, b4), Edge(b3, b5)]
        for bag in bags:
            self.T.add_node(bag)
        for edge in tdedges:
            self.T.add_edge(edge)
        #self.T.show()

    def test_is_tree(self):
        self.assertTrue(is_acyclic(self.T))
        self.assertTrue(is_connected(self.T))

    def test_bags_cover_vertices(self):
        set1 = set(self.G.iternodes())
        set2 = set()
        for bag in self.T.iternodes():
            set2.update(bag)   # po worku moge iterowac
        self.assertEqual(set1, set2)

    def test_bags_cover_edges(self):
        # Buduje graf wiekszy niz G (tu akurat rowny G).
        H = Graph(self.N)
        for node in self.G.iternodes():
            H.add_node(node)
        for bag in self.T.iternodes():
            for node1 in bag:
                for node2 in bag:
                    if node1 < node2:
                        edge = Edge(node1, node2)
                        if not H.has_edge(edge):
                            H.add_edge(edge)
        #H.show()
        # Kazda krawedz G ma zawierac sie w H.
        for edge in self.G.iteredges():
            self.assertTrue(H.has_edge(edge))

    def test_tree_property(self):
        bag_order = []   # kolejnosc odkrywania przez BFS
        algorithm = SimpleBFS(self.T)
        algorithm.run(pre_action=lambda node: bag_order.append(node))
        # Bede korzystal z drzewa BFS zapisanego jako parent (dict).
        # Dla kazdego wierzcholka grafu G buduje poddrzewo (dict).
        subtree = dict((node, dict()) for node in self.G.iternodes())
        root_bag = bag_order[0]
        # Zaczynam pierwsze poddrzewa.
        for node in root_bag:
            subtree[node][root_bag] = None
        # Przetwarzam nastepne bags.
        is_td = True   # flaga sprawdzajaca poprawnosc td
        for bag in bag_order[1:]:
            for node in bag:
                if len(subtree[node]) == 0:   # new subtree
                    subtree[node][bag] = None
                elif algorithm.parent[bag] in subtree[node]:   # kontynuacja
                    subtree[node][bag] = algorithm.parent[bag]
                else:   # rozlaczne poddrzewa, wlasnosc nie jest spelniona
                    is_td = False
        self.assertTrue(is_td)

    def test_treewidth(self):
        treewidth = max(len(bag) for bag in self.T.iternodes()) -1
        self.assertEqual(treewidth, 2)   # outerplanar graph

    def test_find_treewidth_min_deg(self):
        treewidth, order = find_treewidth_min_deg(self.G) # upper bound, 2
        #print("min_deg", treewidth)
        self.assertTrue(treewidth >= 2) # 2 is the true treewidth

    def test_find_treewidth_mmd(self):
        treewidth, order = find_treewidth_mmd(self.G) # lower bound, 2
        #print("mmd", treewidth)
        self.assertTrue(treewidth <= 2) # 2 is the true treewidth

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
