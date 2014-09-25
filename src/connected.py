#!/usr/bin/python
#
# connected.py
#
# Connected components for undirected graphs.
# Strongly connected components for directed graphs.

#from bfs import BFSWithQueue as SimpleBFS
from bfs import SimpleBFS

#from dfs import DFSWithStack as SimpleDFS
#from dfs import DFSWithRecursion as SimpleDFS
from dfs import SimpleDFS


class StronglyConnectedComponents:
    """Strongly connected components for directed graphs."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.scc = dict((node, None) for node in self.graph.iternodes())
        self.n_scc = 0

    def run(self):
        """Executable pseudocode."""
        algorithm = SimpleDFS(self.graph)
        ordering = []
        # use post_action!
        algorithm.run(post_action=lambda node: ordering.append(node))
        ordering.reverse()
        algorithm = SimpleDFS(self.graph.transpose())
        for source in ordering:
            if self.scc[source] is None:
                algorithm.run(source,
                pre_action=lambda node: self.scc.__setitem__(node, self.n_scc))
                self.n_scc = self.n_scc + 1


class ConnectedComponentsBFS:
    """Connected components for undirected graphs."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("graph is directed")
        self.graph = graph
        self.cc = dict((node, None) for node in self.graph.iternodes())
        self.n_cc = 0

    def run(self):
        """Executable pseudocode."""
        algorithm = SimpleBFS(self.graph)
        for source in self.graph.iternodes():
            if self.cc[source] is None:
                algorithm.run(source, 
                pre_action=lambda node: self.cc.__setitem__(node, self.n_cc))
                self.n_cc = self.n_cc + 1


class ConnectedComponentsDFS:
    """Connected components for undirected graphs."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("graph is directed")
        self.graph = graph
        self.cc = dict((node, None) for node in self.graph.iternodes())
        self.n_cc = 0

    def run(self):
        """Executable pseudocode."""
        algorithm = SimpleDFS(self.graph)
        for source in self.graph.iternodes():
            if self.cc[source] is None:
                algorithm.run(source, 
                pre_action=lambda node: self.cc.__setitem__(node, self.n_cc))
                self.n_cc = self.n_cc + 1

# EOF
