#!/usr/bin/python

class BacktrackingNodeColoring:
    """Node coloring with k colors using backtracking.
    
    Find exactly one solution (if it exists).
    Based on the description from
    
    http://www.geeksforgeeks.org/backttracking-set-5-m-coloring-problem/
    """

    def __init__(self, graph, m_colors):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.m_colors = m_colors
        self.node_list = list(self.graph.iternodes())
        import sys
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self):
        """Executable pseudocode."""
        self._graph_color(0)
        if any(self.color[node] is None for node in self.color):
            raise ValueError("m_colors is too small")

    def _is_safe(self, source, c):
        """Check if the current color is safe for the node."""
        return all(self.color[target] != c
            for target in self.graph.iteradjacent(source))

    def _graph_color(self, k):
        """Node coloring with m_colors colors using backtracking."""
        node = self.node_list[k]
        finished = False
        c = 0             # colors from 0 to m_colors-1
        while (not finished) and (c < self.m_colors):
            if self._is_safe(node, c):
                self.color[node] = c   # save
                if k+1 < self.graph.v():
                    finished = self._graph_color(k+1)
                    if not finished:
                        self.color[node] = None   # erase
                else:
                    finished = True
            c += 1
        return finished

# EOF
