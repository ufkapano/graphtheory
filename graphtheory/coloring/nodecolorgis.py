#!/usr/bin/env python3

class GISNodeColoring1:
    """Greedy independent sets algorithm."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")

    def run(self):
        """Executable pseudocode."""
        uncolored_graph = self.graph.copy()   # O(V+E) memory
        c = 0
        while uncolored_graph.v() > 0:   # nie dla kazdej implementacji
            available_graph = uncolored_graph.copy()
            while available_graph.v() > 0:   # nie dla kazdej implementacji
                # Find node with the smallest degree.
                source = min(available_graph.iternodes(),
                    key=available_graph.degree)
                self.color[source] = c
                uncolored_graph.del_node(source)
                # Remove source and its neighbors from available graph.
                to_delete = [source]
                to_delete.extend(available_graph.iteradjacent(source))
                for target in to_delete:
                    available_graph.del_node(target)
            c += 1


class GISNodeColoring2:
    """Greedy independent sets algorithm."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")

    def run(self):
        """Executable pseudocode."""
        n = self.graph.v()
        # Stopnie wierzcholkow w podgrafie generowanym przez niepokolorowane.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time and memory
        colored = 0   # licznik wierzcholkow pokolorowanych
        c = 0
        while colored < n:
            available = set(node for node in self.graph.iternodes()
                if self.color[node] is None)
            dict_copy = dict(degree_dict)   # O(V) time and memory
            while available:
                # Find node with the smallest degree in the subgraph generated.
                source = min(available, key=dict_copy.__getitem__)
                #print dict_copy[source]   # ma byc nieujemne
                self.color[source] = c
                colored += 1
                # Remove source and its neighbors from available.
                available.remove(source)
                for target in self.graph.iteradjacent(source):
                    # target moze nie nalezec do available.
                    available.discard(target)
                    degree_dict[target] -= 1
                    #dict_copy[target] -= 1   # niepotrzebne bo wylatuje z available
                    for node in self.graph.iteradjacent(target):
                        dict_copy[node] -= 1
            c += 1

GISNodeColoring = GISNodeColoring1

# EOF
