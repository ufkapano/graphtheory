#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

class LargestFirstDominatingSet:
    """Find a (largest first) dominating set in O(V+E) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.dominating_set = set()
        self.cardinality = 0
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        used = set()
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        # Grupujemy wierzcholki w bukietach wg stopni.
        bucket = list(set() for deg in range(self.graph.v()))   # O(V) time
        for node in self.graph.iternodes():   # O(V) time
            bucket[self.graph.degree(node)].add(node)

        # Liczba krokow do wykonania rowna sie liczbie wierzcholkow.
        steps = self.graph.v()
        maxi = self.graph.v()-1   # max index
        if source is not None:
            self.source = source
            self.dominating_set.add(source)
            used.add(source)
            steps -= 1   # source removed from bucket
            # Update degree_dict and bucket.
            deg = degree_dict[source]   # tutaj deg moze byc dowolne
            bucket[deg].remove(source)
            # Removing neighbors of source.
            for target in self.graph.iteradjacent(source):
                if target in used:   # target removed from bucket
                    continue
                used.add(target)
                steps -= 1   # target will be removed from bucket
                # Update degree_dict and bucket (for source).
                deg = degree_dict[target]
                bucket[deg].remove(target)
                degree_dict[target] = deg-1   # because source was removed
                degree_dict[source] -= 1
                # Update degree_dict and bucket (for target).
                for node in self.graph.iteradjacent(target):
                    if node in used:   # node removed from bucket
                        continue
                    deg = degree_dict[node]
                    bucket[deg].remove(node)
                    bucket[deg-1].add(node)
                    degree_dict[node] = deg-1
                    degree_dict[target] -= 1
                assert degree_dict[target] == 0
            assert degree_dict[source] == 0

        while steps > 0:
            # Wybor wierzcholka o najwiekszym stopniu.
            while not bucket[maxi]:   # ide w dol, chyba O(2V)
                maxi -= 1
            source = bucket[maxi].pop()
            self.dominating_set.add(source)
            used.add(source)
            steps -= 1   # source removed from bucket
            # Removing neighbors of source.
            for target in self.graph.iteradjacent(source):
                if target in used:   # target removed from bucket
                    continue
                used.add(target)
                steps -= 1   # target will be removed from bucket
                # Update degree_dict and bucket (for source).
                deg = degree_dict[target]
                bucket[deg].remove(target)
                degree_dict[target] = deg-1   # because source was removed
                degree_dict[source] -= 1
                # Update degree_dict and bucket (for target).
                for node in self.graph.iteradjacent(target):
                    if node in used:   # node removed from bucket
                        continue
                    deg = degree_dict[node]
                    bucket[deg].remove(node)
                    bucket[deg-1].add(node)
                    degree_dict[node] = deg-1
                    degree_dict[target] -= 1
                assert degree_dict[target] == 0
            assert degree_dict[source] == 0
        #print ( "steps {}".format(steps) )
        assert steps == 0
        self.cardinality = len(self.dominating_set)

# EOF
