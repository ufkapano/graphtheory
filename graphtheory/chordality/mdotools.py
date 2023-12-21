#!/usr/bin/env python3
"""
MDO = Minimum Degree Ordering
"""

try:
    range = xrange
except NameError:   # Python 3
    pass


def find_mdo(graph):
    """Finding a minimum degree ordering in O(V+E) time."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    order = list()
    used = set()
    degree_dict = dict((node, graph.degree(node))
        for node in graph.iternodes())
    bucket = list(set() for deg in range(graph.v()))   # O(V) time
    for node in graph.iternodes():   # O(V) time
        bucket[graph.degree(node)].add(node)
    for step in range(graph.v()):   # O(V) time
        for deg in range(graph.v()):
            if bucket[deg]:
                source = bucket[deg].pop()
                break
        order.append(source)
        used.add(source)
        for target in graph.iteradjacent(source):
            if target in used:
                continue
            deg = degree_dict[target]   # stary stopien
            bucket[deg].remove(target)
            bucket[deg-1].add(target)
            degree_dict[target] = deg-1   # nowy stopien
    return order


def find_maximum_clique_mdo(graph):
    """Finding a maximum clique in linear time using MDO."""
    order = list()
    used = set()
    degree_dict = dict((node, graph.degree(node))
        for node in graph.iternodes())
    bucket = list(set() for deg in range(graph.v()))   # O(V) time
    for node in graph.iternodes():   # O(V) time
        bucket[graph.degree(node)].add(node)
    max_deg = 0   # najwiekszy stopien wierzcholka
    max_idx = 0   # indeks wierzcholka najdalej w prawo o najwiekszym stopniu
    for step in range(graph.v()):   # O(V) time
        for deg in range(graph.v()):
            if bucket[deg]:
                source = bucket[deg].pop()
                break
        order.append(source)
        used.add(source)
        if max_deg <= degree_dict[source]:   # jak rowny tez zmienic max_idx
            max_deg = degree_dict[source]
            max_idx = step
        for target in graph.iteradjacent(source):
            if target in used:
                continue
            deg = degree_dict[target]   # old degree
            bucket[deg].remove(target)
            bucket[deg-1].add(target)
            degree_dict[target] = deg-1   # new degree
        max_clique = set(order[max_idx:])
        # slower solutions
        #max_clique = set(order[i] for i in range(max_idx, len(order)))
        #max_clique = set(node for (i, node) in enumerate(order) if i >= max_idx)
    return max_clique

# EOF
