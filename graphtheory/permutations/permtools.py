#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

import random
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

def make_complement_perm(perm):
    """Make a perm for the complement graph.
    
    # https://en.wikipedia.org/wiki/Complement_graph
    """
    return perm[::-1]

# EOF
