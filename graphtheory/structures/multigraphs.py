#!/usr/bin/env python3

from graphtheory.structures.edges import Edge

class MultiGraph(dict):
    """The class defining a weighted multigraph.
    
    Nodes can be numbers, strings, or any hashable objects.
    We would like to compare nodes.
    If edge1.source == edge2.source and edge1.target == edge2.target,
    then edge1.weight != edge2.weight (edge1 and edge2 are in a multigraph).
    
    Internal structure of an exemplary directed multigraph:
    {"A": {"B": [Edge("A", "B", 1)], "C": [Edge("A", "C", 2)]}, 
    "B": {"C": [Edge("B", "C", 3)], "D": [Edge("B", "D", 4)]}, 
    "C": {"D": [Edge("C", "D", 5)]}, 
    "D": {"C": [Edge("D", "C", 6), Edge("D", "D", 10)]}, 
    "E": {"C": [Edge("E", "C", 7), Edge("E", "C", 8)]}, 
    "F": {}}
    """

    def __init__(self, n=0, directed=False):
        """Load up a MultiGraph instance.
        
        Parameters
        ----------
        n : int (positive; not used, for compatibility only)
        directed : bool, optional (default=False)
        """
        self.n = n
        self.directed = directed

    def v(self):
        """Return the number of nodes (the multigraph order)."""
        return len(self)

    def e(self):
        """Return the number of edges."""
        loops = 0
        for node in self:
            if node in self[node]:
                loops = loops + len(self[node][node])
        edges = 0
        for source in self:
            for target in self[source]:
                edges = edges + len(self[source][target])
        if self.is_directed():
            return edges
        else:
            return (edges + loops) // 2

    def is_directed(self):
        """Test if the multigraph is directed."""
        return self.directed

    def add_node(self, node):
        """Add a node to the multigraph."""
        if node not in self:
            self[node] = dict()

    def has_node(self, node):
        """Test if a node exists."""
        return node in self

    def del_node(self, node):
        """Remove a node from the multigraph (with edges)."""
        # The dictionary changes size during iteration.
        for edge in list(self.iterinedges(node)):
            self.del_edge(edge)
        if self.is_directed():
            for edge in list(self.iteroutedges(node)):
                self.del_edge(edge)
        del self[node]

    def add_edge(self, edge):
        """Add an edge to the multigraph (missing nodes are created)."""
        if edge.source in self and edge.target in self[edge.source]:
            if edge in self[edge.source][edge.target]:
                raise ValueError("the same parallel edge")
        self.add_node(edge.source)
        self.add_node(edge.target)
        if edge.target not in self[edge.source]:
            self[edge.source][edge.target] = list()
        if not self.is_directed() and edge.source not in self[edge.target]:
            self[edge.target][edge.source] = list()
        # Increase the number of parallel edges.
        self[edge.source][edge.target].append(edge)
        # A loop is added only once.
        if not self.is_directed() and edge.source != edge.target:
            self[edge.target][edge.source].append(~edge)

    def del_edge(self, edge):
        """Remove an edge from the multigraph."""
        if not isinstance(edge, Edge):
            source, target = edge   # tuple or list
            edge = Edge(source, target)
        self[edge.source][edge.target].remove(edge)
        if len(self[edge.source][edge.target]) == 0:
            del self[edge.source][edge.target]
        # A loop is deleted only once.
        if not self.is_directed() and edge.source != edge.target:
            self[edge.target][edge.source].remove(~edge)
            if len(self[edge.target][edge.source]) == 0:
                del self[edge.target][edge.source]

    def has_edge(self, edge):
        """Test if an edge exists. The weight is not checked."""
        if not isinstance(edge, Edge):
            source, target = edge   # tuple or list
            edge = Edge(source, target)
        return edge.source in self and edge.target in self[edge.source]

    def weight(self, edge):
        """Return the number of parallel edges."""
        if isinstance(edge, Edge):
            source, target = edge.source, edge.target
        else:
            source, target = edge   # tuple or list
        if source in self and target in self[source]:
            return len(self[source][target])
        else:
            return 0

    def iternodes(self):
        """Generate nodes from the multigraph on demand."""
        return iter(self)

    def iteradjacent(self, source):
        """Generate adjacent nodes from the multigraph on demand."""
        return iter(self[source])

    def iteroutedges(self, source):
        """Generate outedges from the multigraph on demand."""
        for target in self[source]:
            for edge in self[source][target]:
                yield edge

    def iterinedges(self, source):
        """Generate inedges from the multigraph on demand."""
        if self.is_directed():
            for target in self.iternodes():
                if source in self[target]:
                    for edge in self[target][source]:
                        yield edge
        else:
            for target in self[source]:
                for edge in self[source][target]:
                    yield ~edge   # inverted

    def iteredges(self):
        """Generate edges from the multigraph on demand."""
        for source in self.iternodes():
            for target in self[source]:
                # source <= target, because loops are possible.
                if self.is_directed() or source <= target:
                    for edge in self[source][target]:
                        yield edge

    def show(self):
        """The multigraph presentation."""
        L = []
        for source in self.iternodes():
            L.append("{} : ".format(source))
            for target in self[source]:
                L.append("{}({})".format(target, len(self[source][target])))
            L.append("\n")
        print("".join(L))

    def copy(self):
        """Return the multigraph copy."""
        new_graph = self.__class__(n=self.n, directed=self.directed)
        for source in self.iternodes():
            new_graph[source] = dict()
            for target in self[source]:
                new_graph[source][target] = list(self[source][target])
        return new_graph

    def transpose(self):
        """Return the transpose of the multigraph."""
        new_graph = self.__class__(n=self.n, directed=self.directed)
        for node in self.iternodes():
            new_graph.add_node(node)
        for edge in self.iteredges():
            new_graph.add_edge(~edge)
        return new_graph

    def complement(self):
        """Return the complement of the multigraph."""
        new_graph = self.__class__(n=self.n, directed=self.directed)
        for node in self.iternodes():
            new_graph.add_node(node)
        for source in self.iternodes():
            for target in self.iternodes():
                if source != target:
                    edge = Edge(source, target)
                    # no loops and parallel edges
                    if not self.has_edge(edge) and not new_graph.has_edge(edge):
                        new_graph.add_edge(edge)
        return new_graph

    def subgraph(self, nodes):
        """Return the induced subgraph."""
        node_set = set(nodes)
        if any(not self.has_node(node) for node in node_set):
            raise ValueError("nodes not from the graph")
        new_graph = self.__class__(n=len(node_set), directed=self.directed)
        for node in node_set:
            new_graph.add_node(node)
        for edge in self.iteredges():
            if (edge.source in node_set) and (edge.target in node_set):
                new_graph.add_edge(edge)
        return new_graph

    def degree(self, source):
        """Return the degree of the node in the undirected multigraph."""
        if self.is_directed():
            raise ValueError("the graph is directed")
        if source in self[source]:
            loops = len(self[source][source])
        else:
            loops = 0
        edges = 0
        for target in self[source]:
            edges += len(self[source][target])
        return edges + loops

    def outdegree(self, source):
        """Return the outdegree of the node."""
        if source in self[source]:
            loops = len(self[source][source])
        else:
            loops = 0
        edges = 0
        for target in self[source]:
            edges += len(self[source][target])
        if self.is_directed():
            return edges
        else:   # degree
            return edges + loops

    def indegree(self, source):
        """Return the indegree of the node."""
        if self.is_directed():
            edges = 0
            for target in self.iternodes():
                if source in self[target]:
                    edges += len(self[target][source])
            return edges
        else:   # degree
            if source in self[source]:
                loops = len(self[source][source])
            else:
                loops = 0
            edges = 0
            for target in self[source]:
                edges += len(self[source][target])
            return edges + loops

    def __eq__(self, other):   # FIX
        """Test if the multigraphs are equal."""
        if self.is_directed() is not other.is_directed():
            return False
        if set(self) != set(other):   # checking nodes
            return False
        for source in self.iternodes():   # comparing neighbors
            for target in self[source]:
                if set(self[source][target]) != set(other[source][target]):
                    return False
        return True

    def __ne__(self, other):
        """Test if the multigraphs are not equal."""
        return not self == other

    def add_multigraph(self, other):
        """Add a multigraph to this multigraph (the current multigraph is modified)."""
        for node in other.iternodes():
            self.add_node(node)
        for edge in other.iteredges():
            self.add_edge(edge)

# EOF
