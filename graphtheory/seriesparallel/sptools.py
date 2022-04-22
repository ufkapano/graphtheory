#!/usr/bin/python

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

def swap(L, i, j):
    """Swap items on the list."""
    L[i], L[j] = L[j], L[i]

def make_random_spgraph(n):
    """Make a series-parallel graph with n vertices."""
    if n < 2:
        raise ValueError("bad n")
    graph = Graph(n)
    for node in range(n):
        graph.add_node(node)
    source = 0
    sink = n-1
    idx = 1
    edge_list = [Edge(source, sink, idx)]
    idx += 1
    node = n-2
    while node > 0:
        # Losowanie krawedzi na ktorej bedzie operacja.
        i = random.randrange(0, len(edge_list))
        swap(edge_list, i, -1)
        edge = edge_list[-1]
        # Losowanie operacji.
        if edge.target == sink:
            action = random.choice(["series", "parallel", "jackknife"])
        else:
            action = random.choice(["series", "parallel"])
        if action == "series":
            edge_list.pop()
            edge_list.append(Edge(edge.source, node, idx))
            idx += 1
            edge_list.append(Edge(node, edge.target, idx))
            idx += 1
        elif action == "parallel":
            edge_list.append(Edge(edge.source, node, idx))
            idx += 1
            edge_list.append(Edge(node, edge.target, idx))
            idx += 1
        elif action == "jackknife":
            edge_list.append(Edge(edge.target, node, idx))
            idx += 1
        node -= 1
    for edge in edge_list:
        graph.add_edge(edge)
    return graph


def make_random_ktree(n, k):   # using list
    """Make a random k-tree with n vertices."""
    if k >= n:
        raise ValueError("bad k")   # run time error possible
    graph = Graph(n)
    if n < 1:
        raise ValueError("bad n")
    elif n == 1:
        graph.add_node(0)
    else:
        for node in range(n):
            graph.add_node(node)
        # Make {n-k-1, ..., n-1} into (k+1)-clique in graph.
        for source in range(n-k-1, n):
            for target in range(n-k-1, n):
                if source < target:
                    graph.add_edge(Edge(source, target))
        node = n-k-2
        while node >= 0:
            # Wybor source z przedzialu od node+1 do n-k-1.
            # To jest jakby wybor duzej (k+1)-kliki,
            source = random.choice(range(node+1, n-k))
            # Teraz zbieram wierzcholki tej kliki, ale one maja byc
            # wieksze od source, wieksze numery!
            neighbors = list(target for target in graph.iteradjacent(source)
                            if source < target)
            neighbors.append(source)   # closed neighborhood
            # Z duzej (k+1)-kliki wybieram mala k-klike.
            idx = random.randrange(0, len(neighbors))
            swap(neighbors, idx, -1)
            neighbors.pop()
            # Connect node to all nodes from neighbors.
            for target in neighbors:
                graph.add_edge(Edge(node, target))
            node -= 1
    return graph


def find_peo_spgraph1(graph):   # graph has to be connected
    """Find PEO for a supergraph (2-tree) of an sp-graph."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    order = list()     # PEO of 2-tree
    graph_copy = graph.copy()
    degree_dict = dict((node, graph.degree(node))
        for node in graph.iternodes())              # O(V) time
    bucket = list(set() for deg in range(graph.v()))   # O(V) time
    for node in graph.iternodes():   # wstawiam do kubelkow, O(V) time
        bucket[graph.degree(node)].add(node)
    # Dopoki sa wierzcholki stopnia 2 wykonuj odrywanie.
    deg = 2
    while bucket[deg]:
        source = bucket[deg].pop()
        order.append(source)
        node1, node2 = list(graph_copy.iteradjacent(source))
        edge = Edge(node1, node2)
        if graph_copy.has_edge(edge):
            # Jezeli ma krawedz, to trzeba poprawic stopnie wierzcholkow,
            # bo przy usuwaniu krawedzi przy source zmniejsza sie stopnie.
            deg1 = degree_dict[node1]   # stary stopien
            bucket[deg1].remove(node1)
            bucket[deg1-1].add(node1)
            degree_dict[node1] = deg1-1   # nowy stopien
            deg2 = degree_dict[node2]   # stary stopien
            bucket[deg2].remove(node2)
            bucket[deg2-1].add(node2)
            degree_dict[node2] = deg2-1   # nowy stopien
        else:   # tu nie trzeba poprawiac stopni
            graph_copy.add_edge(edge)
        # Usuwamy krawedzie z source.
        graph_copy.del_edge(Edge(source, node1))
        graph_copy.del_edge(Edge(source, node2))
    # Sprawdzamy co zostalo.
    len1 = len(bucket[1])
    if len1 == 2 and len(order) + len1 == graph.v():
        # Zostala jedna krawedz, dodajemy konce do PEO.
        order.append(bucket[1].pop())
        order.append(bucket[1].pop())
    elif len(bucket[len1]) == 1 and len(order) + len1 + 1 == graph.v():
        # Zostala gwiazda, jest jackknife.
        while bucket[1]:
            order.append(bucket[1].pop())
        order.append(bucket[len1].pop())
    else:
        raise ValueError("not an sp-graph")
    return order


def find_peo_spgraph2(graph):   # graph has to be connected
    """Find PEO for a supergraph (2-tree) of an sp-graph."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    order = list()     # PEO of 2-tree
    graph_copy = graph.copy()
    degree2 = set(node for node in graph.iternodes()
        if graph.degree(node) == 2)   # active nodes with degree 2
    # Dopoki sa wierzcholki stopnia 2 wykonuj odrywanie.
    while degree2:
        source = degree2.pop()
        if graph_copy.degree(source) != 2:
            # Czasem stopien wierzcholka moze sie zmniejszyc!
            continue
        order.append(source)
        node1, node2 = tuple(graph_copy.iteradjacent(source))
        edge = Edge(node1, node2)
        if graph_copy.has_edge(edge):
            # Jezeli ma krawedz, to trzeba poprawic stopnie wierzcholkow,
            # bo przy usuwaniu krawedzi przy source zmniejsza sie stopnie.
            if graph_copy.degree(node1) == 3:
                degree2.add(node1)
            if graph_copy.degree(node2) == 3:
                degree2.add(node2)
        else:   # tu nie trzeba poprawiac stopni
            graph_copy.add_edge(edge)
        # Usuwamy krawedzie z source.
        graph_copy.del_edge(Edge(source, node1))
        graph_copy.del_edge(Edge(source, node2))
    # Sprawdzamy co zostalo.
    degree1 = set(node for node in graph_copy.iternodes()
        if graph_copy.degree(node) == 1)
    if len(degree1) == 2 and len(order) + 2 == graph.v():
        # Zostala jedna krawedz, dodajemy konce do PEO.
        order.append(degree1.pop())
        order.append(degree1.pop())
    elif len(order) + len(degree1) + 1 == graph.v():
        # Zostala gwiazda, jest jackknife.
        # Szukam centrum gwiazdy.
        for node in graph_copy.iternodes():
            deg = graph_copy.degree(node)
            if deg > 1:
                if deg == len(degree1):
                    break
                else:
                    raise ValueError("not an sp-graph")
        while degree1:
            order.append(degree1.pop())
        order.append(node)
    else:
        raise ValueError("not an sp-graph")
    return order


find_peo_spgraph = find_peo_spgraph1

# EOF
