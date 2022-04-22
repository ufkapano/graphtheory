#!/usr/bin/env python3

import sys

class AcyclicGraphDFS:
    """Cycles detection in graphs based on DFS.
    
    ValueError is raised for cyclic graphs.
    
    Attributes
    ----------
    graph : input graph
    color : dict with nodes, private
    parent : dict (DFS tree)
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.parent = dict(((node, None) for node in self.graph.iternodes()))
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # Only one connected component will be checked!
            self._visit(source)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self._visit(node)

    def _visit(self, node):
        """Explore recursively the connected component."""
        self.color[node] = "GREY"
        for edge in self.graph.iteroutedges(node):
            if self.color[edge.target] == "WHITE":
                self.parent[edge.target] = node
                self._visit(edge.target)
            elif self.color[edge.target] == "GREY":   # back edge possible
                if self.graph.is_directed() or edge.target != self.parent[node]:
                    raise ValueError("cycle detected")
            else:   # directed graph, cross or forward edge
                pass
        self.color[node] = "BLACK"


def is_acyclic(graph):
    """Cycles detection."""
    try:
        algorithm = AcyclicGraphDFS(graph)
        algorithm.run()
        return True
    except ValueError:
        return False

# EOF
