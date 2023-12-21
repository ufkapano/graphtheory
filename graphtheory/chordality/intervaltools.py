#!/usr/bin/env python3

try:
    range = xrange
except NameError:   # Python 3
    pass

import random
import itertools
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def make_random_interval(n):   # tak jak dla circle graphs
    """Return a random interval graph as double perm."""
    #perm = list(range(n)) * 2
    perm = [i % n for i in range(2*n)]
    random.shuffle(perm)
    return perm

def make_path_interval(n):   # tak jak dla circle graphs
    """Return a path interval graph as double perm."""
    perm = []
    for i in range(n):
        perm.extend((i, i))
    for i in range(1, 2*n-1, 2):
        swap(perm, i, i+1)
    return perm

# 0---5---4  graf tepee, do P_{n-1} dolaczamy nowy wierzcholek
# | / | \ |
# 1---2---3
def make_tepee_interval(n):
    """Return a tepee interval graph as double perm."""
    if n < 2:
        raise ValueError("n has to be greater than 1")
    perm = [n-1]
    for i in range(n-1):
        perm.extend((i, i))
    for i in range(2, 2*n-2, 2):
        swap(perm, i, i+1)
    perm.append(n-1)
    return perm

# 0---2---4---6 to nie jest tepee graph
# | / | / | /
# 1---3---5
def make_2tree_interval(n):   # tak jak dla circle graphs
    """Return a 2tree interval graph as double perm."""
    if n < 2:
        raise ValueError("n has to be greater than 1")
    perm = [0, 1, 0, 1]
    for i in range(2, n):
        perm.extend((i, i))
        swap(perm, -3, -2)
        swap(perm, -4, -3)
    return perm

def make_star_interval(n):   # dla circle graphs jest inaczej
    """Return a star interval graph as double perm."""
    if n < 2:
        raise ValueError("n has to be greater than 1")
    perm = [0]
    for i in range(1, n):
        perm.extend((i, i))
    perm.append(0)
    return perm

def make_ktree_interval(n, k):
    """Return a k-tree interval graph as double perm."""
    if k >= n:
        raise ValueError("bad k")   # run time error possible
    perm = list(range(k+1))   # first (k+1)-clique
    # Dalej jeden znika, jeden dochodzi.
    for i in range(k+1, n):
        perm.extend((i-k-1, i))
    perm.extend(range(n-k-1, n))   # po kolei znikaja
    return perm

def interval_has_edge(perm, source, target):
    """Test if the interval graph has Edge(source, target), O(n) time, O(n) memory."""
    pairs = dict((node, []) for node in set(perm)) # O(n) time
    for idx, node in enumerate(perm):   # O(n) time
        pairs[node].append(idx)
    s1, s2 = pairs[source]
    t1, t2 = pairs[target]
    return not (s2 < t1 or t2 < s1)

def make_abstract_interval_graph(perm):   # O(n+m) time
    """Finding an abstract interval graph from double perm in O(n+m) time."""
    graph = Graph(n=len(perm) // 2)
    used = set()   # current nodes
    for source in perm:
        if source in used:   # bedzie usuwanie node
            used.remove(source)
        else:   # dodajemy nowy node
            graph.add_node(source)   # isolated node is possible!
            for target in used:
                graph.add_edge(Edge(source, target))
            used.add(source)
    return graph

def print_intervals(cliques):
    """Printing intervals from ordered maximal cliques."""
    # Dla kazdej kliki maksymalnej drukowany jest jeden wiersz.
    tab = []
    nodes = set()
    for clique in cliques:
        nodes.update(clique)
    for clique in cliques:
        row = []
        for node in nodes:
            dot = "." * len(str(node))
            row.append(str(node) if node in clique else dot)
        tab.append(" ".join(row))
    return "\n".join(tab)

def interval_is_connected(perm):
    """Testing connectivity using double perm in O(n) time."""
    used = set()
    for (idx, node) in enumerate(perm):
        if node in used:
            used.remove(node)
            if len(used) == 0 and idx < len(perm)-1:
                return False
        else:
            used.add(node)
    return True

def find_peo_cliques(perm):
    """Finding PEO and ordered maximal cliques for the interval graph."""
    growing = True   # klika bedzie rosnac
    peo = []
    cliques = []   # list of maximal cliques
    used = set()   # current clique
    for node in perm:
        if node in used:   # bedzie usuwanie node, klika zmaleje
            if growing:   # new maximal clique
                cliques.append(set(used))   # kopia zbioru
            else:   # poprzednio tez usuwalismy, wiec nie ma nowej kliki
                pass
            used.remove(node)
            peo.append(node)
            growing = False
        else:   # clique is growing
            used.add(node)
            growing = True
    return peo, cliques

def find_max_clique_size(perm):   # O(n) time
    """Finding the size of a maximum clique for the interval graph, O(n) time."""
    # Trzeba wiedziec, gdzie sa lewe i prawe konce przedzialow.
    # Ja uzywam zbioru used do wykrywania pierwszego i drugiego
    # pojawienia sie danej etykiety.
    # Opis jest w [1993 Sherwani] str. 143.
    size = 0   # maximum clique size
    used = set()   # current clique
    for node in perm:
        if node in used:   # bedzie usuwanie node, klika zmaleje
            used.remove(node)
        else:   # clique is growing
            used.add(node)
            size = max(size, len(used))
    return size

def interval_node_color(perm):
    """Vertex coloring of an interval graph (double perm) in O(n) time."""
    n = len(perm) // 2
    free = list(range(n-1,-1,-1))   # wolne kolory O(n)
    color = dict()
    used = set()   # aktywne przedzialy
    for node in perm:   # idziemy wzdluz permutacji
        if node in used:   # bedzie usuwanie node, klika zmaleje
            used.remove(node)
            free.append(color[node])   # zwracamy kolor
        else:   # dodajemy nowy node, klika rosnie
            used.add(node)
            color[node] = free.pop()
    return color

def interval_maximum_iset(perm):
    """Finding maximum iset of an interval graph (double perm) in O(n) time."""
    perm = list(perm)   # O(n) time, bedzie modyfikacja perm
    iset = set()
    used = set()   # aktywne przedzialy
    # Zapisuje indeksy koncow przedzialow.
    pairs = dict((node, []) for node in set(perm))   # O(n) time
    for idx, node in enumerate(perm):   # O(n) time
        pairs[node].append(idx)
    for node in perm:   # idziemy wzdluz permutacji
        if node is None:   # wymazany przedzial
            continue
        elif node in used:   # bedzie usuwanie node, klika zmaleje
            used.remove(node)
            iset.add(node)
            for source in used:   # usuwam sasiadow z perm, sumarycznie O(n)
                perm[pairs[source][0]] = None
                perm[pairs[source][1]] = None
            used.clear()   # przedzialy wymazane
        else:   # dodajemy nowy node, klika rosnie
            used.add(node)
    return iset

# EOF
