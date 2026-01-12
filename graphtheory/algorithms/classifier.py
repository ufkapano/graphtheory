#!/usr/bin/env python3

import sys

class EdgeClassifierDFS:
    """Edge classifier based on DFS.
    
    Attributes
    ----------
    graph : input graph
    color : dict with pairs (node, color), private, colors: WHITE, GREY, BLACK
    parent : dict (DFS tree)
    classifier : dict with pairs (edge, edge_type), types: TREE, BACK, FORWARD, CROSS
    
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
        self.classifier = dict()
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
                self.classifier[edge] = "TREE"
                self._visit(edge.target)
            elif self.color[edge.target] == "GREY":   # back edge possible
                if self.graph.is_directed() or edge.target != self.parent[node]:
                    self.classifier[edge] = "BACK"
            else:   # directed graph, cross or forward edge
                if not self.graph.is_directed():
                    continue   # back edge
                source = edge.target
                forward = False
                while self.parent[source] is not None:
                    source = self.parent[source]
                    if source == node:
                        self.classifier[edge] = "FORWARD"
                        forward = True
                if not forward:
                    self.classifier[edge] = "CROSS"
        self.color[node] = "BLACK"

# EOF
