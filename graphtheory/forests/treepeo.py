#!/usr/bin/env python3

import sys
import collections


def find_peo_tree(graph):
    """Find PEO for a tree or a forest (removing leaves), O(n) time."""
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


class TreePEO:
    """Find PEO for a tree (removing leaves), O(n) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.peo = []
        self.parent = dict()   # a tree as a dict

    def run(self):
        """Executable pseudocode."""
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(n) time
        Q = collections.deque()   # for leaves
        # Put leaves to the queue, O(n) time.
        for node in self.graph.iternodes():
            if degree_dict[node] == 0:   # isolated node from the beginning
                self.peo.append(node)
                self.parent[node] = None   # a forest is started
            elif degree_dict[node] == 1:   # leaf
                Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            # A leaf may become isolated.
            # To moze sie zdarzyc przy ostatnim wierzcholku.
            if degree_dict[source] == 0:
                self.peo.append(source)
                self.parent[source] = None
                #print("finding root", source)
                continue
            assert degree_dict[source] == 1
            for target in self.graph.iteradjacent(source):
                if degree_dict[target] > 0:   # this is parent
                    self.peo.append(source)
                    self.parent[source] = target
                    # Remove the edge from source to target.
                    degree_dict[target] -= 1
                    degree_dict[source] -= 1
                    if degree_dict[target] == 1:   # parent is a new leaf
                        Q.append(target)
                    break
        if len(self.peo) != self.graph.v():
            raise ValueError("the graph is not a tree")
        assert len(self.parent) == self.graph.v()

# EOF
