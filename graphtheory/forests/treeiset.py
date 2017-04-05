#!/usr/bin/python

class BorieIndependentSet:
    """Find a maximum independent set for trees.
    
    Attributes
    ----------
    graph : input forest
    independent_set : set with nodes
    parent : dict (DFS tree)
    cardinality : number (the size of iset)
    
    Notes
    -----
    Based on
    
    Richard B. Borie, R. Gary Parker, Craig A. Tovey, 
    Solving Problems on Recursively Constructed Graphs,
    ACM Computing Surveys 41, 4 (2008).
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.parent = dict()   # DFS tree
        self.independent_set = set()
        self.cardinality = 0
        import sys
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # A single connected component, a single tree.
            self.parent[source] = None   # before _visit
            arg2 = self._visit(source)
            self.independent_set.update(max(arg2, key=len))
            self.cardinality = len(self.independent_set)
        else:
            # A forest is possible.
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    arg2 = self._visit(node)
                    self.independent_set.update(max(arg2, key=len))
            self.cardinality = len(self.independent_set)

    def compose(self, arg1, arg2):
        """Compose results."""
        # a_set : max iset that includes root
        # b_set : max iset that excludes root
        a1_set, b1_set = arg1
        a2_set, b2_set = arg2
        a_set = a1_set | b2_set
        b_set = b1_set | max(arg2, key=len)   # larger is needed
        return (a_set, b_set)

    def _visit(self, root):
        """Explore recursively the connected component."""
        # Start from a single node.
        arg1 = (set([root]), set())
        for target in self.graph.iteradjacent(root):
            if target not in self.parent:
                self.parent[target] = root   # before _visit
                arg2 = self._visit(target)
                arg1 = self.compose(arg1, arg2)
        return arg1
