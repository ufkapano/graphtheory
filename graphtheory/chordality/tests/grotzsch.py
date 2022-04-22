#!/usr/bin/env python3

import unittest
import itertools
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.algorithms.acyclic import is_acyclic
from graphtheory.connectivity.connected import is_connected
from graphtheory.traversing.bfs import SimpleBFS
from graphtheory.chordality.tdtools import find_td_order
from graphtheory.chordality.tdtools import find_treewidth_min_deg # upper bound
from graphtheory.chordality.tdtools import find_treewidth_mmd # lower bound

# https://en.wikipedia.org/wiki/Gr%C3%B6tzsch_graph
#
# Grotzsh graph
# V = 11, E = 20, triangle-free, Hamiltonian, non-planar,
# treewidth = 5

class TestTreeDecomposition(unittest.TestCase):

    def setUp(self):
        self.N = 11     # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(1, 2), Edge(2, 3), Edge(3, 4), Edge(4, 5), Edge(5, 6), 
            Edge(6, 7), Edge(7, 8), Edge(8, 9), Edge(9, 10), Edge(1, 10), 
            Edge(0, 2), Edge(0, 4), Edge(0, 6), Edge(0, 8), Edge(0, 10), 
            Edge(1, 5), Edge(1, 7), Edge(3, 7), Edge(3, 9), Edge(5, 9)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        # Tworze tree decomposition.
        # Ustalam, ze worki to beda krotki, abym mogl je porownywac.
        # Zgaduje optymalne uporzadkowanie wierzcholkow.
        order = [2, 4, 6, 8, 10, 0, 1, 3, 5, 7, 9] # found manually
        self.T = find_td_order(self.G, order)
        #self.T.show()   # star

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
            for (node1, node2) in itertools.combinations(bag, 2):
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
        self.assertEqual(treewidth, 5)

    def test_find_treewidth_min_deg(self):
        treewidth, order = find_treewidth_min_deg(self.G) # upper bound, 5
        #print("min_deg", treewidth)
        self.assertTrue(treewidth >= 5) # 5 is the true treewidth

    def test_find_treewidth_mmd(self):
        treewidth, order = find_treewidth_mmd(self.G) # lower bound, 3
        #print("mmd", treewidth)
        self.assertTrue(treewidth <= 5) # 5 is the true treewidth

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
