#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.permutations.circlebfs import CircleBFS

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def make_random_circle(n):
    """Return a random circle graph as double perm."""
    #perm = list(range(n)) * 2
    perm = [i % n for i in range(2*n)]
    random.shuffle(perm)
    return perm

def make_path_circle(n):
    """Return a path graph P_n as double perm."""
    perm = []
    for i in range(n):
        perm.extend((i, i))
    for i in range(1, 2*n-1, 2):
        swap(perm, i, i+1)
    return perm

def make_cycle_circle(n):
    """Return a cycle graph C_n as double perm."""
    if n < 3:
        raise ValueError("n has to be greater than 2")
    perm = []
    for i in range(n):
        perm.extend((i, i))
    for i in range(1, 2*n-1, 2):
        swap(perm, i, i+1)
    swap(perm, 0, -1)
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

def make_ktree_circle(n, k):
    """Return a k-tree circle graph as double perm."""
    if k >= n:
        raise ValueError("bad k")   # run time error possible
    perm = list(range(k+1))   # first (k+1)-clique
    # Dalej jeden znika, jeden dochodzi.
    for i in range(k+1, n):
        perm.extend((i-k-1, i))
    perm.extend(range(n-k-1, n))   # po kolei znikaja
    return perm

def make_star_circle(n):
    """Return a star graph as double perm."""
    if n < 2:
        raise ValueError("n has to be greater than 1")
    perm = [0]
    perm.extend(range(1, n))
    perm.append(0)
    perm.extend(range(n-1,0,-1))
    return perm

def circle_has_edge(perm, source, target):
    """Test if the circle graph has Edge(source, target), O(n) time, O(n) memory."""
    pairs = dict((node, []) for node in set(perm))   # O(n) time
    for idx, node in enumerate(perm):   # O(n) time
        pairs[node].append(idx)
    s1, s2 = pairs[source]
    t1, t2 = pairs[target]
    return (s1 < t1 < s2 < t2) or (t1 < s1 < t2 < s2)

def circle_is_connected(perm):
    """Testing connectivity of the circle graph in O(n^2) time."""
    order = []
    algorithm = CircleBFS(perm)
    # Elementy permutacji to wierzcholki, a to nie musza byc liczby.
    algorithm.run(perm[0], pre_action=lambda node: order.append(node))
    return len(order) * 2 == len(perm)

def is_perm_graph(perm):   # O(n) time, O(n) memory
    """Test if the circle graph (double perm) is a perm graph in O(n) time."""
    window = set()
    n = len(perm) // 2   # the numbed of nodes
    for i in range(n):   # make initial window, O(n) time
        node = perm[i]
        if node in window:
            window.remove(node)
        else:
            window.add(node)
    if len(window) == n:
        return True
    for i in range(n, 2*n):   # O(n) time
        node = perm[i]
        if node in window:
            window.remove(node)
        else:
            window.add(node)
        if len(window) == n:
            return True
    return False

# EOF
