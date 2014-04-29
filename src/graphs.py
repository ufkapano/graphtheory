#!/usr/bin/python
#
# graphs.py
#
# Nodes can be numbers, string, or any hashable objects.
# We would like also to compare nodes.
#
# {"A":{"B":1,"C":2}, 
# "B":{"C":3,"D":4}, 
# "C":{"D":5}, 
# "D":{"C":6}, 
# "E":{"C":7}, 
# "F":{}}

from edges import Edge


class Graph(dict):
    """The class defining a graph."""

    def __init__(self, n=0, directed=False):
        """Loads up a Graph instance."""
        self.n = n              # compatibility
        self.directed = directed  # bool

    def v(self):
        """Returns the number of nodes (the graph order)."""
        return len(self)

    def e(self):
        """Returns the number of edges."""
        edges = sum(len(self[node]) for node in self)
        return (edges if self.is_directed() else edges / 2)

    def is_directed(self):
        """Test if the graph is directed."""
        return self.directed

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self:
            self[node] = {}

    def has_node(self, node):
        """Test if a node exists."""
        return node in self

    def del_node(self, node):
        """Remove a node from the graph (with edges)."""
        # dictionary changes size during iteration.
        for edge in list(self.iterinedges(node)):
            self.del_edge(edge)
        if self.is_directed():
            for edge in list(self.iteroutedges(node)):
                self.del_edge(edge)
        del self[node]

    def add_edge(self, edge):
        """Add an edge to the graph (missing nodes are created)."""
        self.add_node(edge.source)
        self.add_node(edge.target)
        if edge.target not in self[edge.source]:
            self[edge.source][edge.target] = edge.weight
        if not self.is_directed():
            if edge.source not in self[edge.target]:
                self[edge.target][edge.source] = edge.weight

    def del_edge(self, edge):
        """Remove an edge from the graph."""
        del self[edge.source][edge.target]
        if not self.is_directed():
            del self[edge.target][edge.source]

    def has_edge(self, edge):
        """Test if an edge exists."""
        return (edge.target in self[edge.source] and
        edge.weight == self[edge.source][edge.target])

    def weight(self, source, target):
        """Returns the edge weight or zero."""
        if source in self and target in self[source]:
            return self[source][target]
        else:
            return 0

    def iternodes(self):
        """Generates nodes from the graph on demand."""
        return self.iterkeys()

    def iteradjacent(self, source):
        """Generates adjacent nodes from the graph on demand."""
        return self[source].iterkeys()

    def iteroutedges(self, source):
        """Generates outedges from the graph on demand."""
        for target in self[source]:
            yield Edge(source, target, self[source][target])

    def iterinedges(self, source):
        """Generates outedges from the graph on demand."""
        if self.is_directed():   # inefficient, time O(E)
            for edge in self.iteredges():
                if edge.target == source:
                    yield edge
        else:    # iteroutedges
            for target in self[source]:
                yield Edge(source, target, self[source][target])

    def iteredges(self):
        """Generates edges from the graph on demand."""
        for source in self.iternodes():
            for target in self[source]:
                if self.is_directed() or source < target:
                    yield Edge(source, target, self[source][target])

    def show(self):
        """Graph presentation."""
        for source in self.iternodes():
            print source, ":",
            for target in self.iteradjacent(source):
                print "%s(%s)" % (target, self[source][target]),
            print

    def __eq__(self, other):
        """Test if the graphs are equal."""
        if self.is_directed() is not other.is_directed():
            #print "directed and undirected graphs"
            return False
        if self.v() != other.v():
            #print "|V1| != |V2|"
            return False
        alist = list(self.iternodes())
        alist.sort()
        blist = list(other.iternodes())
        blist.sort()
        if alist != blist:
            #print "V1 != V2"
            return False
        if self.e() != other.e():   # inefficient, time O(E)
            #print "|E1| != |E2|"
            return False
        for edge in self.iteredges():
            if not other.has_edge(edge):
                #print "E1 != E2"
                return False
        return True

    def __ne__(self, other):
        """Test if the graphs are not equal."""
        return not self == other

# EOF
