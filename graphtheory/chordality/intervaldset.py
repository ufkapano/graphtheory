#!/usr/bin/env python3

class IntervalDominatingSet:
    """Finding a minimum dominating set and a maximum 2-stable set
    of an interval graph (double perm) in O(n+m) time.

    Based on:
    
    Chang, G.J. (2013). Algorithmic Aspects of Domination in Graphs.
    In: Pardalos, P., Du, DZ., Graham, R. (eds) Handbook of Combinatorial
    Optimization. Springer, New York, NY.
    
    Attributes
    ----------
    perm : input double perm
    dominating_set : set with nodes
    cardinality : number (the size of min dset)
    two_stable_set : set with nodes
    pairs : dict with pairs (node, [head, tail])
    graph : dict with pairs (node, set_with_neighbors)
    """

    def __init__(self, perm):
        """The algorithm initialization."""
        self.perm = perm
        self.dominating_set = set()
        self.cardinality = 0
        self.two_stable_set = set()

        # Zapisuje indeksy koncow przedzialow.
        self.pairs = dict((node, []) for node in set(self.perm)) # O(n) time
        for idx, node in enumerate(self.perm): # O(n) time
            self.pairs[node].append(idx)

        # Tworze zbiory sasiadow, graph[v] is closed neighborhood of v.
        self.graph = dict((node, set([node])) for node in set(perm))   # O(n) time
        used = set()   # current nodes
        for source in self.perm:   # O(n) time
            if source in used:   # bedzie usuwanie node
                used.remove(source)
            else:   # dodajemy nowy node i krawedzie
                for target in used:
                    self.graph[source].add(target)
                    self.graph[target].add(source)
                used.add(source)

    def run(self):
        """Finding a dset and a 2-stable set."""
        used = set()   # active intervals
        for source in self.perm:   # O(n) time
            #print("source", source)
            if source in used:   # bedzie usuwanie node, klika zmaleje
                target = max(used, key=lambda v: self.pairs[v][1])
                #print("target", target)
                if len(self.graph[source].intersection(self.dominating_set)) == 0:
                    #print("add ...")
                    self.dominating_set.add(target)
                    self.two_stable_set.add(source)
                used.remove(source)
            else:   # dodajemy nowy node, klika rosnie
                used.add(source)
        self.cardinality = len(self.dominating_set)

# EOF
