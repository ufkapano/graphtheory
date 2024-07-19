#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.connectivity.connected import ConnectedComponentsBFS

class ATFreeIndependentSet:
    """Find a maximum independent set for AT-free graphs.

    Based on:

    H. Broersma, T. Kloks, D. Kratsch, H. Muller,
    Independent sets in asteroidal triple-free graphs,
    SIAM J. Discrete Math. 12, No.2, 276-287 (1999).
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph       # AT-free graph
        self.independent_set = None   # na razie nie wyznaczam zbioru
        self.cardinality = 0   # independence number
        self.component_structure = dict()
        self.component_lists = dict()
        # component_lists[u] daje liste komponentow G\N[u] jako 2-tuple
        # (reprezentanci). Zbior mozna odczytac przez cs[a,b].
        self.intervals = dict()
        self.bucket_C = None
        self.bucket_I = None
        self.alpha_C = dict()   # results for components
        self.alpha_I = dict()   # results for intervals

    def run(self):
        """Executable pseudocode."""
        self.create_component_structure()
        self.find_intervals()
        self.sort_components_intervals()
        self.find_alpha_C_I()
        self.find_alpha_G()

    def create_component_structure(self):
        """Create component structure for G."""
        V = set(self.graph.iternodes())
        for v in V:
            closed_neighborhood = set(self.graph.iteradjacent(v)).union([v])
            G_reduced = self.graph.subgraph(V - closed_neighborhood)
            algorithm = ConnectedComponentsBFS(G_reduced)
            algorithm.run()
            component_list = [set() for x in range(algorithm.n_cc + 1)]
            component_list[0] = closed_neighborhood
            for u in closed_neighborhood:
                self.component_structure[v,u] = component_list[0]
            for u in algorithm.cc:   # tu jest numeracja skladowych od 0
                idx = algorithm.cc[u] + 1   # numerujemy od 1
                component_list[idx].add(u)
                self.component_structure[v,u] = component_list[idx]
            # Gromadze reprezentantow/klucze komponentow G\N[v].
            # Pomijam komponent utworzony przez N[v] (closed neighborhood).
            self.component_lists[v] = [
                (v, next(iter(s))) for s in component_list[1:]] 

    def find_intervals(self):
        """Finding intervals for nonadjacent pairs of vertices."""
        Gc = self.graph.complement()   # O(n^2) time
        # Uzywamy dopelnienia G, bo tu krawedzie lacza pary wierzcholkow,
        # ktore nie sa sasiednie w grafie G.
        for edge in Gc.iteredges():   # total O(n^3) time
            v, u = edge.source, edge.target
            self.intervals[v,u] = (self.component_structure[v,u]
                & self.component_structure[u,v])
            self.intervals[u,v] = self.intervals[v,u]   # I(u,v) = I(v,u)

    def sort_components_intervals(self):
        """Sorting components and intervals (bucket sort, O(n^2) time)."""
        # Przygotowanie bukietow dla components i intervals.
        self.bucket_C = [[] for i in range(self.graph.v())]
        self.bucket_I = [[] for i in range(self.graph.v())]
        #for key in self.component_structure:   # key is 2-tuple (u,v)
        #    self.bucket_C[len(self.component_structure[key])].append(key)
        # UWAGA Nie powinno sie uzywac N[u], wiec trzeba inaczej.
        for v in self.graph.iternodes():
            for key in self.component_lists[v]:
                self.bucket_C[len(self.component_structure[key])].append(key)
        for key in self.intervals:   # key is 2-tuple (u,v)
            self.bucket_I[len(self.intervals[key])].append(key)

    def find_alpha_C_I(self):
        """Finding alpha(I) and alpha(C)."""
        # Empty intervals.
        # There are no empty components.
        for key in self.bucket_I[0]:
            self.alpha_I[key] = set()
        # Components and intervals with a single element.
        for key in self.bucket_I[1]:
            self.alpha_I[key] = set(self.intervals[key])
        for key in self.bucket_C[1]:
            self.alpha_C[key] = set(self.component_structure[key])
        # Components and intervals with two elements.
        for key in self.bucket_I[2]:
            S = set(self.intervals[key])
            S.pop()   # zostaje jeden element
            self.alpha_I[key] = S
        for key in self.bucket_C[2]:
            S = set(self.component_structure[key])
            S.pop()   # zostaje jeden element
            self.alpha_C[key] = S
        # Przy wiekszej licznosci trzeba uzywac formul rozkladu.
        for i in range(3, self.graph.v()):
            for key in self.bucket_I[i]:
                self.alpha_I[key] = self.find_alpha_I(key)
            for key in self.bucket_C[i]:
                self.alpha_C[key] = self.find_alpha_C(key)

    def find_alpha_I(self, key):
        """Lemma 6.3 from [1999 Broersma]."""
        results = []
        x, y = key
        interval = self.intervals[key]
        for s in interval:
            # Zaczynam od I(x,s) oraz I(s,y).
            # Z definicji przedzialu s nie jest sasiadem x i y.
            res = self.alpha_I[x,s] | self.alpha_I[s,y]   # to jest nowy zbior
            # Wyznaczam komponenty G\N[s] zawarte w I(x,y).
            # S = I(x,y)-I(x,s)-I(s,y)-N[s]
            S = interval.difference(self.intervals[x,s],
                                    self.intervals[s,y],
                                    self.component_structure[s,s])
            # Teraz w S leza cale komponenty G\N[s].
            for key in self.component_lists[s]:
                C = self.component_structure[key]
                if C.issubset(S):
                    S = S.difference(C)
                    res.update(self.alpha_C[key])
            assert len(S) == 0, S
            res.add(s)
            results.append(res)
        return max(results, key=len)

    def find_alpha_C(self, key):
        """Lemma 6.2 from [1999 Broersma]."""
        results = []
        x, y = key
        component = self.component_structure[key]
        for z in component:
            # Zaczynam od I(x,z).
            res = set(self.alpha_I[x,z])   # to musi byc kopia!
            # Wyznaczam komponenty G\N[z] zawarte w C^x(y).
            # Zachodzi C^x(y) = C^x(z), bo to ten sam komponent.
            # S = C^x(z)-N[z]-I(x,z)
            S = component.difference(self.component_structure[z,z],
                                     self.intervals[x,z])
            # Teraz S zawiera cale komponenty G\N[z].
            for key in self.component_lists[z]:
                C = self.component_structure[key]
                if C.issubset(S):
                    S = S.difference(C)
                    res.update(self.alpha_C[key])
            assert len(S) == 0, S
            res.add(z)
            results.append(res)
        return max(results, key=len)

    def find_alpha_G(self):
        """Final calculations of alpha(G)."""
        # To jest zgodne z Lematem 6.1 from [1999 Broersma].
        results = []   # results for different vertices, list of sets
        for v in self.graph.iternodes():
            S = set([v])   # od razu zaliczam v do max iset
            for key in self.component_lists[v]:
                S.update(self.alpha_C[key])
            results.append(S)
        # Wybieram max iset.
        self.independent_set = max(results, key=len)
        self.cardinality = len(self.independent_set)

# EOF
