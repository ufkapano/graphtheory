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

def make_random_circle(n):
    """Return a random circle graph as double perm."""
    #double_perm = list(range(n)) * 2
    double_perm = [i % n for i in range(2*n)]
    random.shuffle(double_perm)
    return double_perm

def make_path_circle(n):
    """Return a path graph P_n as double perm."""
    perm = []
    for i in range(n):
        perm.extend((i, i))
    for i in range(1, 2*n-1, 2):
        perm[i], perm[i+1] = perm[i+1], perm[i]
    return perm

def make_cycle_circle(n):
    """Return a cycle graph C_n as double perm."""
    if n < 3:
        raise ValueError("n has to be greater than 2")
    perm = []
    for i in range(n):
        perm.extend((i, i))
    for i in range(1, 2*n-1, 2):
        perm[i], perm[i+1] = perm[i+1], perm[i]
    perm[0], perm[-1] = perm[-1], perm[0]
    return perm

def make_tepee_circle(n):
    """Return a tepee graph as double perm."""
    if n < 2:
        raise ValueError("n has to be greater than 1")
    perm = [0, 1, 0, 1]
    for i in range(2, n):
        perm.extend((i, i))
        swap(perm, -3, -2)
        swap(perm, -4, -3)
    return perm

def is_perm_graph(double_perm): # O(n) time, O(n) memory
    """Test if the circle graph (double perm) is a perm graph in O(n) time."""
    window = set()
    n = len(double_perm) // 2   # the numbed of nodes
    for i in range(n):   # make initial window, O(n) time
        node = double_perm[i]
        if node in window:
            window.remove(node)
        else:
            window.add(node)
    if len(window) == n:
        return True
    for i in range(n, 2*n):   # O(n) time
        node = double_perm[i]
        if node in window:
            window.remove(node)
        else:
            window.add(node)
        if len(window) == n:
            return True
    return False

# EOF
