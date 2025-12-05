#!/usr/bin/env python3

from graphtheory.chordality.mdotools import find_mdo

class BronKerboschDegeneracyIterator:
    """Finding all maximal cliques using the Bron-Kerbosch algorithm 
    with a degeneracy ordering. An iterator over maximal cliques is created.
    
    Attributes
    ----------
    graph : input undirected graph
    cliques : list of cliques
    counter : number of recursive calls
    order : list of nodes (degeneracy ordering)
    
    Notes
    -----
    Based on the pseudocode from
    
    https://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm
    
    C. Bron, J. Kerbosch, 
        "Algorithm 457: finding all cliques of an undirected graph", 
        Communications of the ACM 16 (9), 575-577 (1973).
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.order = None   # degeneracy ordering

    def run(self):
        """Executable pseudocode."""
        self.order = find_mdo(self.graph)   # O(n+m) time
        R = set()
        P = set(self.graph.iternodes())
        X = set()
        yield from self.find_cliques(R, P, X)

    def find_cliques(self, R, P, X):
        """The Bron-Kerbosch algorithm with a degeneracy ordering.
        R - the temporary result
        P - the set of the possible candidates
        X - the excluded set
        """
        if len(P) == 0 and len(X) == 0:
            yield R
        elif len(P) == 0:
            return
        else:
            for node in self.order:   # P zmienia sie w petli!
                if node in P:
                    neighbors = set(self.graph.iteradjacent(node))
                    # Usuwamy node przed wyznaczaniem new_P i new_X,
                    # aby miec mniejszy zbior P w operacji intersection().
                    P.remove(node)
                    new_R = R.union([node])             # R | set([node])
                    new_P = P.intersection(neighbors)   # P & neighbors
                    new_X = X.intersection(neighbors)   # X & neighbors
                    yield from self.find_cliques(new_R, new_P, new_X)
                    X.add(node)

# EOF
