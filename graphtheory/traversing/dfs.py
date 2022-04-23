#!/usr/bin/env python3

import sys

try:
    from Queue import LifoQueue
except ImportError:   # Python 3
    from queue import LifoQueue


class DFSWithStack:
    """Depth-First Search with a stack.
    
    Attributes
    ----------
    graph : input graph
    color : dict with nodes, private ('WHITE', 'GREY', 'BLACK')
    time : number, private
    dd : dict with nodes ('GREY' time)
    ff : dict with nodes ('BLACK' time)
    parent : dict (DFS tree)
    dag : graph (DFS tree)
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.traversing.dfs import DFSWithStack
    >>> G = Graph(n=10, False)   # an exemplary undirected graph
    # Add nodes and edges here.
    >>> order = list()
    >>> algorithm = DFSWithStack(G)
    >>> algorithm.run(source=0, pre_action=lambda node: order.append(node))
    >>> order   # visited nodes
    >>> algorithm.parent   # DFS tree as a dict
    >>> algorithm.dag    # DFS tree as a directed graph
    >>> algorithm.dd
    >>> algorithm.ff
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Depth-first_search
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.parent = dict(((node, None) for node in self.graph.iternodes()))
        self.time = 0    # time stamp
        self.dd = dict()
        self.ff = dict()
        self.dag = self.graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.dag.add_node(node)

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self._visit(source, pre_action, post_action)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self._visit(node, pre_action, post_action)

    def _visit(self, node, pre_action=None, post_action=None):
        """Explore the connected component,"""
        self.time = self.time + 1
        self.dd[node] = self.time
        self.color[node] = "GREY"
        Q = LifoQueue()
        Q.put(node)   # node is GREY
        if pre_action:   # when Q.put
            pre_action(node)
        while not Q.empty():
            source = Q.get()    # GREY node is processed
            for edge in self.graph.iteroutedges(source):
                if self.color[edge.target] == "WHITE":
                    self.parent[edge.target] = source
                    self.dag.add_edge(edge)
                    self.time = self.time + 1
                    self.dd[edge.target] = self.time
                    self.color[edge.target] = "GREY"
                    Q.put(edge.target)   # target is GREY
                    if pre_action:   # when Q.put
                        pre_action(edge.target)
            self.time = self.time + 1
            self.ff[source] = self.time
            self.color[source] = "BLACK"
            if post_action:   # source became BLACK
                post_action(source)

    def path(self, source, target):
        """Construct a path from source to target."""
        if source == target:
            return [source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[target]) + [target]


class DFSWithRecursion:
    """Depth-First Search with a recursion.
    
    Attributes
    ----------
    graph : input graph
    color : dict with nodes, private ('WHITE', 'GREY', 'BLACK')
    time : number, private
    dd : dict with nodes ('GREY' time)
    ff : dict with nodes ('BLACK' time)
    parent : dict (DFS tree)
    dag : graph (DFS tree)
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.traversing.dfs import DFSWithRecursion
    >>> G = Graph(n=10, False)   # an exemplary undirected graph
    # Add nodes and edges here.
    >>> order = list()
    >>> algorithm = DFSWithRecursion(G)
    >>> algorithm.run(source=0, pre_action=lambda node: order.append(node))
    >>> order   # visited nodes
    >>> algorithm.parent   # DFS tree as a dict
    >>> algorithm.dag    # DFS tree as a directed graph
    >>> algorithm.dd
    >>> algorithm.ff
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Depth-first_search
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.parent = dict(((node, None) for node in self.graph.iternodes()))
        self.time = 0    # time stamp
        self.dd = dict()
        self.ff = dict()
        self.dag = self.graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.dag.add_node(node)
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self._visit(source, pre_action, post_action)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self._visit(node, pre_action, post_action)

    def _visit(self, node, pre_action=None, post_action=None):
        """Explore recursively the connected component."""
        self.time = self.time + 1
        self.dd[node] = self.time
        self.color[node] = "GREY"
        if pre_action:   # _visit started
            pre_action(node)
        for edge in self.graph.iteroutedges(node):
            if self.color[edge.target] == "WHITE":
                self.parent[edge.target] = node
                self.dag.add_edge(edge)
                self._visit(edge.target, pre_action, post_action)
        self.time = self.time + 1
        self.ff[node] = self.time
        self.color[node] = "BLACK"
        if post_action:   # node became BLACK
            post_action(node)

    def path(self, source, target):
        """Construct a path from source to target."""
        if source == target:
            return [source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[target]) + [target]


class SimpleDFS:
    """Depth-First Search with a recursion.
    
    Attributes
    ----------
    graph : input graph
    parent : dict (DFS tree)
    dag : graph (DFS tree)
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.traversing.dfs import SimpleDFS
    >>> G = Graph(n=10, False)   # an exemplary undirected graph
    # Add nodes and edges here.
    >>> order = list()
    >>> algorithm = SimpleDFS(G)
    >>> algorithm.run(source=0, pre_action=lambda node: order.append(node))
    >>> order   # visited nodes
    >>> algorithm.parent   # DFS tree as a dict
    >>> algorithm.dag    # DFS tree as a directed graph
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Depth-first_search
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.parent = dict()
        self.dag = self.graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.dag.add_node(node)
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self.parent[source] = None   # before _visit
            self._visit(source, pre_action, post_action)
        else:
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    self._visit(node, pre_action, post_action)

    def _visit(self, node, pre_action=None, post_action=None):
        """Explore recursively the connected component."""
        if pre_action:
            pre_action(node)
        for edge in self.graph.iteroutedges(node):
            if edge.target not in self.parent:
                self.parent[edge.target] = node   # before _visit
                self.dag.add_edge(edge)
                self._visit(edge.target, pre_action, post_action)
        if post_action:
            post_action(node)

    def path(self, source, target):
        """Construct a path from source to target."""
        if source == target:
            return [source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[target]) + [target]

# EOF
