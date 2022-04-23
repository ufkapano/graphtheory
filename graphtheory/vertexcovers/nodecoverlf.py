#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

class LargestFirstNodeCover:
    """Find a minimum node cover (largest first algorithm) in O(V+E) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.node_cover = set()
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        # Grupujemy wierzcholki w bukietach wg stopni.
        bucket = list(set() for deg in range(self.graph.v()))   # O(V) time
        for node in self.graph.iternodes():   # O(V) time
            bucket[self.graph.degree(node)].add(node)

        maxi = self.graph.v()-1   # max possible index

        while True:
            # Wybor wierzcholka o najwiekszym stopniu.
            #print ( "bucket {}".format(bucket) )
            while not bucket[maxi]:   # ide w dol, chyba O(2V)
                maxi -= 1
            if maxi == 0:   # no edges to cover
                break
            source = bucket[maxi].pop()
            #print ( "source {} maxi {}".format(source, maxi) )
            self.node_cover.add(source)
            # Removing outedges.
            for target in self.graph.iteradjacent(source):
                if target in self.node_cover:   # target removed from bucket
                    continue
                # Update degree_dict and bucket.
                deg = degree_dict[target]
                bucket[deg].remove(target)
                bucket[deg-1].add(target)
                degree_dict[target] = deg-1   # because source was removed
                degree_dict[source] -= 1
            assert degree_dict[source] == 0
        self.cardinality = len(self.node_cover)

# EOF
