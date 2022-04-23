#!/usr/bin/env python3

from graphtheory.traversing.bfs import SimpleBFS


class WheelGraph:
    """Wheel graphs detection.
    
    Attributes
    ----------
    graph : input graph
    hub : node
    
    Notes
    -----
    Based on:
    
    https://en.wikipedia.org/wiki/Wheel_graph
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected graph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hub = None

    def run(self):
        """Executable pseudocode."""
        n = self.graph.v()
        e = self.graph.e()   # this may be O(E)
        if n < 4:
            raise ValueError("the number of nodes is less then 4")
        elif n == 4 and e == 6:   # complete graph K4
            self.hub = next(self.graph.iternodes())
            return
        if e != 2 * n - 2:
            raise ValueError("bad number of edges")
        dset = set(self.graph.degree(node) for node in self.graph.iternodes())
        if dset != set([3, n-1]):
            raise ValueError("bad set of node degrees")
        self.hub = max(self.graph.iternodes(), key=self.graph.degree)
        # Remove edges from the hub.
        removed = list(self.graph.iteroutedges(self.hub))
        for edge in removed:
            self.graph.del_edge(edge)
        # Now a cycle should be present.
        # Choose a node different from the hub.
        for node in self.graph.iternodes():
            if node != self.hub:
                source = node
                break
        order = []
        algorithm = SimpleBFS(self.graph)
        algorithm.run(source, pre_action=lambda node: order.append(node))
        # Restore edges.
        for edge in removed:
            self.graph.add_edge(edge)
        if len(order) != n-1:
            raise ValueError("not a wheel graph")


def is_wheel(graph):
    """Test if a graph is a wheel graph."""
    try:
        algorithm = WheelGraph(graph)
        algorithm.run()
        return True
    except ValueError:
        return False

# EOF
