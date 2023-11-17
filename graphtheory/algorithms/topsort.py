#!/usr/bin/env python3

try:
    range = xrange   # range będzie zawsze generatorem
except NameError:   # Python 3
    pass

import collections
#from graphtheory.traversing.dfs import DFSWithRecursion as SimpleDFS
from graphtheory.traversing.dfs import SimpleDFS


class TopologicalSortDFS:
    """Topological sorting of nodes from a dag using DFS.
    
    Attributes
    ----------
    graph : input directed acyclic graph
    sorted_nodes : list of sorted nodes
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Topological_sorting
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.sorted_nodes = []

    def run(self):
        """Executable pseudocode."""
        algorithm = SimpleDFS(self.graph)
        algorithm.run(post_action=lambda node: self.sorted_nodes.append(node))
        self.sorted_nodes.reverse()


class TopologicalSortQueue:
    """Topological sorting of nodes from a dag (Kahn's algorithm).
    
    Attributes
    ----------
    graph : input directed acyclic graph
    sorted_nodes : list of sorted nodes
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Topological_sorting
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.sorted_nodes = list()

    def run(self):
        """Executable pseudocode."""
        queue = collections.deque()   # queue or stack or set
        # Calculate indegree of nodes.
        inedges = dict((node, 0) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            inedges[edge.target] += 1
        for node in self.graph.iternodes():
            if inedges[node] == 0:
                queue.append(node)
        while len(queue):
            node = queue.popleft()
            self.sorted_nodes.append(node)
            # Remove all outedges.
            for edge in self.graph.iteroutedges(node):
                inedges[edge.target] -= 1
                if inedges[edge.target] == 0:
                    queue.append(edge.target)


class TopologicalSortSet:
    """Topological sorting of nodes from a dag (Kahn's algorithm).
    
    Attributes
    ----------
    graph : input directed acyclic graph
    sorted_nodes : list of sorted nodes
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Topological_sorting
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.sorted_nodes = []

    def run(self):
        """Executable pseudocode."""
        Q = set()   # queue or stack or set
        # Calculate indegree of nodes.
        inedges = dict((node, 0) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            inedges[edge.target] += 1
        for node in self.graph.iternodes():
            if inedges[node] == 0:
                Q.add(node)
        while Q:
            node = Q.pop()
            self.sorted_nodes.append(node)
            # Remove all outedges.
            for edge in self.graph.iteroutedges(node):
                inedges[edge.target] -= 1
                if inedges[edge.target] == 0:
                    Q.add(edge.target)


class TopologicalSortList:
    """Topological sorting of nodes from a dag (Kahn's algorithm).
    
    Attributes
    ----------
    graph : input directed acyclic graph
    sorted_nodes : list of sorted nodes
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Topological_sorting
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.sorted_nodes = [None] * self.graph.v()

    def run(self):
        """Executable pseudocode."""
        # Calculate indegree of nodes.
        inedges = dict((node, 0) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            inedges[edge.target] += 1
        qstart = 0  # first to get
        qend = 0   # first free place
        for node in self.graph.iternodes():
            if inedges[node] == 0:
                self.sorted_nodes[qend] = node
                qend += 1
        for step in range(self.graph.v()):
            source = self.sorted_nodes[qstart]
            qstart += 1
            # Remove all outedges.
            for edge in self.graph.iteroutedges(source):
                inedges[edge.target] -= 1
                if inedges[edge.target] == 0:
                    self.sorted_nodes[qend] = edge.target
                    qend += 1

# EOF
