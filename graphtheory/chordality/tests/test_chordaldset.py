#!/usr/bin/env python3

import unittest
import itertools
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.algorithms.acyclic import is_acyclic
from graphtheory.connectivity.connected import is_connected
from graphtheory.traversing.bfs import SimpleBFS
from graphtheory.chordality.chordaldset import ChordalDominatingSet

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

class TestDominatingSet1(unittest.TestCase):

    def setUp(self):
        self.N = 7
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.edges = [
            Edge("A", "B"), Edge("A", "C"), Edge("B", "C"), Edge("B", "F"), 
            Edge("B", "G"), Edge("C", "D"), Edge("C", "E"), Edge("D", "E"), 
            Edge("E", "G"), Edge("E", "H"), Edge("F", "G"), Edge("G", "H"),
            Edge("B", "E")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        # Tworze tree decomposition.
        # Ustalam, ze worki to beda krotki, abym mogl je porownywac.
        self.T = Graph(6)
        b0 = ("A", "B", "C")
        b1 = ("B", "C", "E")
        b2 = ("C", "D", "E")
        b3 = ("B", "E", "G")
        b4 = ("B", "F", "G")
        b5 = ("E", "G", "H")
        bags = [b0, b1, b2, b3, b4, b5]
        tdedges = [
            Edge(b0, b1), Edge(b1, b2), Edge(b1, b3), 
            Edge(b3, b4), Edge(b3, b5)]   # tu byl blad!
        for bag in bags:
            self.T.add_node(bag)
        for edge in tdedges:
            self.T.add_edge(edge)
        #self.T.show()

    def test_chordal_dset(self):
        algorithm = ChordalDominatingSet(self.G, self.T)
        algorithm.run()
        expected1 = set(["C", "G"])
        expected2 = set(["B", "E"])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.dominating_set, expected2)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

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
        #print("bag_order", bag_order)
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
        #print("subtree", subtree)
        self.assertTrue(is_td)

    def test_treewidth(self):
        treewidth = max(len(bag) for bag in self.T.iternodes()) -1
        self.assertEqual(treewidth, 2)   # outerplanar graph

    def tearDown(self): pass

# 0---1---4            2-tree
# | \ | / |
# 3---2---5

class TestDominatingSet2(unittest.TestCase):

    def setUp(self):
        self.N = 6
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(2, 3), Edge(0, 3), 
             Edge(0, 2), Edge(2, 4), Edge(1, 4), Edge(2, 5), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        # Tworze tree decomposition.
        # Ustalam, ze worki to beda krotki, abym mogl je porownywac.
        self.T = Graph(4)
        b0 = (0, 2, 3)
        b1 = (0, 1, 2)
        b2 = (1, 2, 4)
        b3 = (2, 4, 5)
        bags = [b0, b1, b2, b3]
        tdedges = [Edge(b0, b1), Edge(b1, b2), Edge(b2, b3)]
        for bag in bags:
            self.T.add_node(bag)
        for edge in tdedges:
            self.T.add_edge(edge)
        #self.T.show()

    def test_chordal_dset(self):
        algorithm = ChordalDominatingSet(self.G, self.T)
        algorithm.run()
        expected = set([2])
        self.assertEqual(algorithm.cardinality, len(expected))
        self.assertEqual(algorithm.dominating_set, expected)
        # Testing dset.
        neighbors = set(algorithm.dominating_set)
        for node in algorithm.dominating_set:
            neighbors.update(self.G.iteradjacent(node))
        self.assertEqual(len(neighbors), self.G.v())

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
        #print("bag_order", bag_order)
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
        #print("subtree", subtree)
        self.assertTrue(is_td)

    def test_treewidth(self):
        treewidth = max(len(bag) for bag in self.T.iternodes()) -1
        self.assertEqual(treewidth, 2)   # outerplanar graph

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
