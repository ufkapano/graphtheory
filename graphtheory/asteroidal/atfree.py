#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.connectivity.connected import ConnectedComponentsBFS

class ATFreeGraph:
    """Finding AT-free graphs.

    Based on:
    
    https://networkx.org/documentation/stable/reference/algorithms/asteroidal.html
    
    E. Kohler, Recognizing graphs without asteroidal triples,
    Journal of Discrete Algorithms 2(4), 439-452 (2004).
    
    https://www.graphclasses.org/classes/gc_61.html
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : an undirected graph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.component_structure = dict()
        self.asteroidal_triple = None

    def run(self):
        """Executable pseudocode."""
        self.create_component_structure()
        self.find_asteroidal_triple()

    def create_component_structure(self):
        """Create component structure for the graph."""
        # component_structure[u,v] == 0, if v in N[u],
        # component_structure[u,v] == k > 0, if v in k component of V-N[u].
        # Czyli jezeli u.v sa w tej samej skladowej spojnej, to jest path.
        V = set(self.graph.iternodes())
        for v in V:
            # Label 0 for nodes in N[v].
            Nv = set(self.graph.iteradjacent(v)).union([v])
            for u in Nv:
                self.component_structure[v,u] = 0

            G_reduced = self.graph.subgraph(V - Nv)
            algorithm = ConnectedComponentsBFS(G_reduced)
            algorithm.run()
            for u in algorithm.cc:   # tu jest numeracja skladowych od 0
                self.component_structure[v,u] = algorithm.cc[u] + 1   # numerujemy od 1

    def find_asteroidal_triple(self):
        """Find an asteroidal triple in the given graph."""
        if self.graph.v() < 6:
            # An asteroidal triple cannot exist in a graph
            # with 5 or less vertices.
            return None

        V = set(self.graph.iternodes())
        Gc = self.graph.complement()   # O(n^2) time
        # Uzywamy dopelnienia G, bo tu krawedzie lacza pary wierzcholkow,
        # ktore nie sa sasiednie w grafie G.

        for edge in Gc.iteredges():
            u, v = edge.source, edge.target
            # Obliczanie domknietych sasiedztw.
            Nu = set(self.graph.iteradjacent(u)).union([u])
            Nv = set(self.graph.iteradjacent(v)).union([v])
            union_of_neighborhoods = Nu.union(Nv)
            for w in V - union_of_neighborhoods:
                # Check for each pair of vertices whether they belong to the
                # same connected component when the closed neighborhood of the
                # third is removed.
                if (self.component_structure[u,v] == 
                    self.component_structure[u,w] and
                    self.component_structure[v,u] ==
                    self.component_structure[v,w] and
                    self.component_structure[w,u] ==
                    self.component_structure[w,v]):
                    self.asteroidal_triple = (u, v, w)
                    return None

    def is_at_free(self):
        """Check if a graph is AT-free."""
        if self.component_structure is None:
            raise ValueError("run the algorithm first")
        return self.asteroidal_triple is None

# EOF
