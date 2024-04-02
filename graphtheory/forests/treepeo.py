#!/usr/bin/env python3

import sys
import collections


def find_peo_tree(graph):
    """Find PEO for a tree or a forest (removing leaves)."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    peo = []
    degree_dict = dict((node, graph.degree(node))
        for node in graph.iternodes())   # O(n) time
    Q = collections.deque()   # for leaves
    # Put leaves to the queue, O(n) time.
    for node in graph.iternodes():
        if degree_dict[node] == 0:   # isolated node from the beginning
            peo.append(node)
        elif degree_dict[node] == 1:   # leaf
            Q.append(node)
    while len(Q) > 0:
        source = Q.popleft()
        # A leaf may become isolated.
        if degree_dict[source] == 0:
            peo.append(source)
            continue
        assert degree_dict[source] == 1
        for target in graph.iteradjacent(source):
            if degree_dict[target] > 0:   # this is parent
                peo.append(source)
                # Remove the edge from source to target.
                degree_dict[target] -= 1
                degree_dict[source] -= 1
                if degree_dict[target] == 1:   # parent is a new leaf
                    Q.append(target)
                break
    if len(peo) != graph.v():
        raise ValueError("the graph is not a tree")
    return peo

# EOF
