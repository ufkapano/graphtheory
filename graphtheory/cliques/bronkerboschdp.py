#!/usr/bin/env python3

class BronKerboschDegreePivot:
    """Finding all maximal cliques using the Bron-Kerbosch algorithm 
    with a pivot with largest degree in P.
    
    Attributes
    ----------
    graph : input undirected graph
    cliques : list of cliques
    counter : number of recursive calls
    
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
        self.cliques = []
        self.counter = 0

    def run(self):
        """Executable pseudocode."""
        R = set()
        P = set(self.graph.iternodes())
        X = set()
        self.find_cliques(R, P, X)

    def find_pivot(self, P, X):
        """Find a pivot with largest degree in P."""
        degree_dict = dict()
        nodes = P.union(X)
        for node in nodes:
            neighbors = set(self.graph.iteradjacent(node))
            degree_dict[node] = len(P.intersection(neighbors))
        return max(nodes, key=degree_dict.__getitem__)

    def find_cliques(self, R, P, X):
        """The Bron-Kerbosch algorithm with pivoting.
        R - the temporary result
        P - the set of the possible candidates
        X - the excluded set
        """
        self.counter += 1
        if len(P) == 0 and len(X) == 0:
            self.cliques.append(R)
        elif len(P) == 0:
            return
        else:
            pivot = self.find_pivot(P, X)
            for node in self.graph.iternodes():   # P zmienia sie w petli!
                if (node in P) and not self.graph.has_edge((node, pivot)):
                    neighbors = set(self.graph.iteradjacent(node))
                    # Usuwamy node przed wyznaczaniem new_P i new_X,
                    # aby miec mniejszy zbior P w operacji intersection().
                    P.remove(node)
                    new_R = R.union([node])             # R | set([node])
                    new_P = P.intersection(neighbors)   # P & neighbors
                    new_X = X.intersection(neighbors)   # X & neighbors
                    self.find_cliques(new_R, new_P, new_X)
                    X.add(node)

# EOF
