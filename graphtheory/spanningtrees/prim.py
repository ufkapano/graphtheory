#!/usr/bin/env python3

try:
    from Queue import PriorityQueue
    range = xrange
except ImportError:   # Python 3
    from queue import PriorityQueue

from graphtheory.connectivity.connected import is_connected


class PrimMST:
    """Prim's algorithm for finding a minimum spanning tree.
    
    The algorithm runs in O(E log V) time.
    
    Attributes
    ----------
    graph : input undirected weighted graph or multigraph
    mst : graph (MST)
    distance : dict with nodes
    parent : dict with nodes (MST)
    _in_queue : dict, private
    _pq : priority queue, private
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.spanningtrees.prim import PrimMST
    >>> G = Graph(n=10, False)    # an exemplary undirected graph
    # Add nodes and edges here.
    >>> algorithm = PrimMST(G)
    >>> algorithm.run()     # calculations
    >>> algorithm.parent     # MST as a dict
    >>> mst = algorithm.to_tree()   # MST as an undirected graph
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Prim's_algorithm.
    
    https://en.wikipedia.org/wiki/Minimum_spanning_tree
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected weighted graph or multigraph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.mst = None
        self.distance = dict((node, float("inf")) for node in self.graph.iternodes())
        self.parent = dict((node, None) for node in self.graph.iternodes())
        self._in_queue = dict((node, True) for node in self.graph.iternodes())
        self._pq = PriorityQueue()

    def run(self, source=None):
        """Finding MST."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self.source = source
        self.distance[source] = 0
        for node in self.graph.iternodes():
            self._pq.put((self.distance[node], node))
        while not self._pq.empty():
            _, node = self._pq.get()
            if self._in_queue[node]:
                self._in_queue[node] = False
            else:
                continue
            for edge in self.graph.iteroutedges(node):
                if self._in_queue[edge.target] and edge.weight < self.distance[edge.target]:
                    self.distance[edge.target] = edge.weight
                    self.parent[edge.target] = edge.source
                    # DECREASE-KEY
                    self._pq.put((edge.weight, edge.target))

    def to_tree(self):
        """The minimum spanning tree is built."""
        self.mst = self.graph.__class__(self.graph.v(), directed=False)
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.mst.add_node(node)
        for edge in self.graph.iteredges():   # O(E) time
            if (self.parent[edge.source] is edge.target and
                self.distance[edge.source] == edge.weight):
                    self.mst.add_edge(edge)
            elif (self.parent[edge.target] is edge.source and
                self.distance[edge.target] == edge.weight):
                    self.mst.add_edge(edge)
        return self.mst


class PrimMSTWithEdges:
    """Prim's algorithm for finding a minimum spanning tree.
    
    Attributes
    ----------
    graph : input undirected weighted graph or multigraph
    mst : graph (MST)
    distance : dict with nodes
    parent : dict with nodes (MST)
    _in_queue : dict, private
    _pq : priority queue, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mst = None
        self.distance = dict((node, float("inf")) for node in self.graph.iternodes())
        self.parent = dict((node, None) for node in self.graph.iternodes()) # MST as a dict
        self._in_queue = dict((node, True) for node in self.graph.iternodes())
        self._pq = PriorityQueue()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self.source = source
        self.distance[source] = 0
        for node in self.graph.iternodes():
            self._pq.put((self.distance[node], node))
        while not self._pq.empty():
            _, node = self._pq.get()
            if self._in_queue[node]:
                self._in_queue[node] = False
            else:
                continue
            for edge in self.graph.iteroutedges(node):
                if self._in_queue[edge.target] and edge.weight < self.distance[edge.target]:
                    self.distance[edge.target] = edge.weight
                    self.parent[edge.target] = ~edge
                    # DECREASE-KEY
                    self._pq.put((edge.weight, edge.target))

    def to_tree(self):
        """The minimum spanning tree is built."""
        self.mst = self.graph.__class__(self.graph.v(), directed=False)
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.mst.add_node(node)
        for node in self.parent:   # O(V) time
            if self.parent[node] is not None:
                self.mst.add_edge(self.parent[node])
        return self.mst


class PrimMatrixMST:
    """Prim's algorithm for finding a minimum spanning tree.
    
    The algorithm runs in O(V^2) time. It is suitable for dense graphs.
    
    Attributes
    ----------
    graph : input undirected weighted graph or multigraph
    mst : graph (MST)
    distance : dict with nodes
    parent : dict with nodes (MST)
    _in_queue : dict, private
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.spanningtrees.prim import PrimMatrixMST
    >>> from graphtheory.structures.factory import GraphFactory
    >>> gf = GraphFactory(Graph)
    >>> G = gf.make_complete(n=10, directed=False)
    >>> algorithm = PrimMatrixMST(G)
    >>> algorithm.run()     # calculations 
    >>> algorithm.parent     # MST as a dict
    >>> mst = algorithm.to_tree()     # MST as an undirected graph
    
    Notes
    -----
    Based on:

    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Prim's_algorithm.
    
    https://en.wikipedia.org/wiki/Minimum_spanning_tree
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected weighted graph or multigraph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.mst = None
        self.distance = dict((node, float("inf")) for node in self.graph.iternodes())
        self.parent = dict((node, None) for node in self.graph.iternodes())
        self._in_queue = dict((node, True) for node in self.graph.iternodes())

    def run(self, source=None):
        """Finding MST."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self.source = source
        self.distance[source] = 0
        for step in range(self.graph.v()):    # |V| times
            # Find min node in the graph, O(V) time.
            node = min((node for node in self.graph.iternodes() 
                if self._in_queue[node]), key=self.distance.get)
            self._in_queue[node] = False
            for edge in self.graph.iteroutedges(node):  # O(V) time
                if self._in_queue[edge.target] and edge.weight < self.distance[edge.target]:
                    self.distance[edge.target] = edge.weight
                    self.parent[edge.target] = edge.source

    def to_tree(self):
        """The minimum spanning tree is built."""
        self.mst = self.graph.__class__(self.graph.v(), directed=False)
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.mst.add_node(node)
        for edge in self.graph.iteredges():   # O(E) time
            if (self.parent[edge.source] is edge.target and
                self.distance[edge.source] == edge.weight):
                    self.mst.add_edge(edge)
            elif (self.parent[edge.target] is edge.source and
                self.distance[edge.target] == edge.weight):
                    self.mst.add_edge(edge)
        return self.mst


class PrimMatrixMSTWithEdges:
    """Prim's algorithm for finding MST in O(V^2) time.
    
    Attributes
    ----------
    graph : input undirected weighted graph or multigraph
    mst : graph (MST)
    distance : dict with nodes
    parent : dict with edges (MST)
    _in_queue : dict, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mst = None
        self.distance = dict((node, float("inf")) for node in self.graph.iternodes())
        self.parent = dict((node, None) for node in self.graph.iternodes())
        self._in_queue = dict((node, True) for node in self.graph.iternodes())

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self.source = source
        self.distance[source] = 0
        for step in range(self.graph.v()):    # |V| times
            # Find min node in the graph, O(V) time.
            node = min((node for node in self.graph.iternodes() 
                if self._in_queue[node]), key=self.distance.get)
            self._in_queue[node] = False
            for edge in self.graph.iteroutedges(node):   # O(V) time
                if self._in_queue[edge.target] and edge.weight < self.distance[edge.target]:
                    self.distance[edge.target] = edge.weight
                    self.parent[edge.target] = ~edge

    def to_tree(self):
        """The minimum spanning tree is built."""
        self.mst = self.graph.__class__(self.graph.v(), directed=False)
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.mst.add_node(node)
        for node in self.parent:   # O(V) time
            if self.parent[node] is not None:
                self.mst.add_edge(self.parent[node])
        return self.mst


class PrimConnectedMST:
    """Prim's algorithm for finding a minimum spanning tree.
    
    The algorithm runs in O(E log V) time.
    The graph must be connected.
    
    Attributes
    ----------
    graph : input undirected weighted graph or multigraph
    mst : graph (MST)
    _in_queue : dict, private
    _pq : priority queue, private
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Prim's_algorithm.
    
    https://en.wikipedia.org/wiki/Minimum_spanning_tree
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected weighted graph or multigraph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        if not is_connected(graph):
            raise ValueError("the graph is not connected")
        self.graph = graph
        self.mst = self.graph.__class__(self.graph.v(), directed=False)
        self._in_queue = dict((node, True) for node in self.graph.iternodes())
        self._pq = PriorityQueue()

    def run(self, source=None):
        """Finding MST."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self.source = source
        self._in_queue[source] = False
        # W kolejce trzymam krawedzie wychodzace na zewnatrz od MST.
        for edge in self.graph.iteroutedges(self.source):
            self._pq.put((edge.weight, edge))
        while not self._pq.empty():
            _, edge = self._pq.get()
            if self._in_queue[edge.target]:
                self._in_queue[edge.target] = False
                self.mst.add_edge(edge)   # wstawiam do MST
            else:
                continue
            for edge2 in self.graph.iteroutedges(edge.target):
                if self._in_queue[edge2.target]:
                    self._pq.put((edge2.weight, edge2))

    def to_tree(self):
        """Compatibility with other Prim classes."""
        return self.mst


class PrimTrivialMST:
    """Prim's algorithm for finding a minimum spanning tree.
    
    The algorithm runs in O(V*E) time.
    
    Attributes
    ----------
    graph : input undirected weighted graph or multigraph
    mst : graph (MST)
    _in_mst : dict, private
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected weighted graph or multigraph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        if not is_connected(graph):
            raise ValueError("the graph is not connected")
        self.graph = graph
        self.mst = self.graph.__class__(self.graph.v(), directed=False)
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.mst.add_node(node)
        self._in_mst = dict((node, False) for node in self.graph.iternodes())

    def run(self, source=None):
        """Finding MST."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self.source = source
        self._in_mst[source] = True
        for step in range(self.graph.v()-1):    # |V|-1 times
            # Finding min edge, O(E) time.
            min_edge = min(edge for edge in self.graph.iteredges()
                if self._in_mst[edge.source] != self._in_mst[edge.target])
            self.mst.add_edge(min_edge)
            self._in_mst[min_edge.source] = True
            self._in_mst[min_edge.target] = True

    def to_tree(self):
        """Compatibility with other Prim classes."""
        return self.mst

# EOF
