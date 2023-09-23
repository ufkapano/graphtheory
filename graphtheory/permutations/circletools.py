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

def make_2tree_circle(n):
    """Return a 2-tree graph as double perm."""
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

def make_abstract_circle_graph(perm):
    """Return an abstract circle graph from double perm in O(n^2) time."""
    nodes = set(perm)   # O(n) time
    # dict do zapisu pierwszego i drugiego wystapienia wierzcholka w perm.
    pairs = dict((node, []) for node in nodes)   # O(n) time
    for i, node in enumerate(perm):   # O(n) time
        pairs[node].append(i)
    assert all(len(pairs[node]) == 2 for node in pairs)
    graph = Graph(n=len(nodes))
    # Jest krawedz, jezeli przedzialy sie zazebiaja.
    # Zlozonosc n(n-1)/2, czyli O(n^2).
    for (source, target) in itertools.combinations(nodes, 2):
        s1, s2 = pairs[source]
        t1, t2 = pairs[target]
        if (s1 < t1 < s2 < t2) or (t1 < s1 < t2 < s2):
            graph.add_edge(Edge(source, target))
    return graph

def circle_is_connected(perm):
    """Testing connectivity of the circle graph in O(n^2) time."""
    order = []
    algorithm = CircleBFS(perm)
    # Elementy permutacji to wierzcholki, a to nie musza byc liczby.
    algorithm.run(perm[0], pre_action=lambda node: order.append(node))
    return len(order) * 2 == len(perm)

def is_perm_graph(perm):   # O(n) time, O(n) memory
    """Test if the circle graph (double perm) is a perm graph in O(n) time.
    Note that if this test failed then the corresponding abstract graph
    still can be a perm graph but harder to detect.
    """
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
    # Przesuwamy okno.
    for i in range(n):   # O(n) time
        node = perm[i]   # node wychodzacy z okna
        if node in window:
            window.remove(node)
        else:
            window.add(node)
        node = perm[i+n]   # node wchodzacy do okna
        if node in window:
            window.remove(node)
        else:
            window.add(node)
        if len(window) == n:
            return True
    return False

# Zakladam, ze double_perm zawiera etykiety (int lub str).
# Jezeli circle graph jest perm graph, to chce dostac permutacje liczb
# od 0 do n-1 i slownik D par (number, label)
def circle2perm(double_perm):
    """From double perm to perm for perm graphs.
    Note that if this test failed then the corresponding abstract graph
    still can be a perm graph but harder to detect.
    """
    window = set()
    start_idx = -1   # nieprawidlowy index na starcie, poczatek okna
    n = len(double_perm) // 2   # liczba wierzcholkow
    for i in range(n):   # make initial window, O(n) time
        node = double_perm[i]
        if node in window:
            window.remove(node)
        else:
            window.add(node)
    if len(window) == n:
        start_idx = 0
    else:   # Przesuwamy okno. Z lewej wychodza, z prawej wchodza.
        for i in range(n):   # O(n) time
            node = double_perm[i]   # node wychodzacy z okna
            if node in window:
                window.remove(node)
            else:
                window.add(node)
            node = double_perm[i+n]   # node wchodzacy do okna
            if node in window:
                window.remove(node)
            else:
                window.add(node)
            if len(window) == n:
                start_idx = i+1
                break
    if start_idx == -1:
        raise ValueError("perm graph not detected")
    # Buduje slowniki.
    label2number = dict()
    number2label = dict()
    for i in range(n):
        label2number[double_perm[start_idx+i]] = i
        number2label[i] = double_perm[start_idx+i]
    # Buduje permutacje.
    perm = [label2number[double_perm[(start_idx+n+i) % (2*n)]] for i in range(n)]
    perm.reverse()
    return perm, number2label, label2number

# EOF
