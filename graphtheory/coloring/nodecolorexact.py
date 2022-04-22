#!/usr/bin/env python3

class ExactNodeColoring:
    """Find an exact node coloring (slow).
    
    Based on
    http://eduinf.waw.pl/inf/alg/001_search/0142.php
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with nodes (values are colors)
    
    Notes
    -----
    Colors are 0, 1, 2, ...
    """
    # Idea taka jak w 
    # http://edu.i-lo.tarnow.pl/inf/alg/001_search/0142.php
    # ale nie ma optymalizacji przez pomijanie sprawdzania kombinacji,
    # ktore byly sprawdzane przy mniejszej liczbie kolorow.

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, 0) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")

    def run(self):
        """Executable pseudocode."""
        base = 1
        is_colored = False
        while not is_colored:
            is_colored = True
            # Check if this coloring is proper.
            for edge in self.graph.iteredges():
                if self.color[edge.source] == self.color[edge.target]:
                    is_colored = False
                    break
            if not is_colored:
                roll = False
                # UWAGA Ta iteracja po kolorach musi byc taka sama
                # w ramach ustalonego base, bo inaczej licznik sie posypie.
                # Nie wiem, czy Python to gwarantuje.
                # Jezeli w ostatnim przebiegu roll=True, to znaczy,
                # ze licznik sie skonczyl.
                for node in self.color:
                    if self.color[node] == base - 1:
                        roll = True
                        self.color[node] = 0
                    else:
                        roll = False
                        self.color[node] += 1
                        break
                if roll:
                    base += 1   # add new color
                    self.color = dict(((node, 0)
                        for node in self.graph.iternodes()))

# EOF
