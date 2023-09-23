#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

import random
import itertools
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def make_random_perm(n):
    """Return a random perm."""
    perm = list(range(n))
    random.shuffle(perm)
    return perm

def make_star_perm(n):
    """Return a perm for K_{1,n-1} bipartite graph."""
    perm = [n-1]
    perm.extend(range(n-1))
    return perm

def make_bipartite_perm(p, q):
    """Return a perm for K_{p,q} complete bipartite graph."""
    perm = []
    perm.extend(range(p, p+q))
    perm.extend(range(p))
    return perm

def make_path_perm(n):
    """Return a perm for P_n path graph."""
    if n < 1:
        raise ValueError("no nodes")
    elif n == 1:
        return [0]
    elif n == 2:
        return [1, 0]
    else:
        perm = make_path_perm(n-2)
        perm.append(n-2)
        perm.append(n-1)
        swap(perm, -2, -1)
        swap(perm, -3, -2)
        return perm

def perm_has_edge1(perm, i, j):
    """Test if the perm graph has Edge(i, j), O(n) time, O(n) memory."""
    if i > j:
        i, j = j, i
    # Szukamy indeksow, position[] to permutacja odwrotma do perm.
    position = list(perm)   # tymczasowo, O(n) memory
    for k, item in enumerate(perm):   # O(n) time
        position[item] = k
    # Wlasciwy test
    return position[i] > position[j]

def perm_has_edge2(perm, i, j):
    """Test if the perm graph has Edge(i, j), O(n) time, O(1) memory."""
    if i > j:
        i, j = j, i
    for k, item in enumerate(perm):   # O(n) time
        if item == i:
            left = k
        if item == j:
            right = k
    return left > right

perm_has_edge = perm_has_edge2

def make_abstract_perm_graph(perm):
    """Return an abstract perm graph from perm in O(n^2) time."""
    # Szukamy indeksow, position[] to permutacja odwrotna do perm.
    position = list(perm)   # tymczasowo, O(n) memory
    for k, item in enumerate(perm):   # O(n) time
        position[item] = k
    graph = Graph(n=len(perm))
    # Jest krawedz, jezeli jest inwersja. Zlozonosc n(n-1)/2, czyli O(n^2).
    for (source, target) in itertools.combinations(perm, 2):
        if source > target:
            source, target = target, source
        if position[source] > position[target]:
            graph.add_edge(Edge(source, target))
    return graph

def make_complement_perm(perm):
    """Make a perm for the complement graph.
    
    # https://en.wikipedia.org/wiki/Complement_graph
    """
    return perm[::-1]

def perm_is_connected(perm):
    """Test if the perm graph is connected in O(n) time."""
    n = len(perm)
    maxi = 0
    for i in range(n):
        if perm[i] > maxi:
            maxi = perm[i]
        if i != n - 1 and maxi == i:
            return False
    return True

def perm_connected_components(perm):
    """Finding connected components of the perm graph in O(n) time."""
    n = len(perm)
    cc = dict()   # pairs (node, no of cc)
    n_cc = 0   # the number of connected components
    maxi = 0
    for i in range(n):
        if perm[i] > maxi:
            maxi = perm[i]
        cc[perm[i]] = n_cc
        if i != n - 1 and maxi == i:
            n_cc += 1   # new connected component
    n_cc += 1
    return n_cc, cc

# EOF
