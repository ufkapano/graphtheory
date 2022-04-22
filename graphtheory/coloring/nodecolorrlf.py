#!/usr/bin/env python3

class RLFNodeColoring1:
    """Recursive Largest First (RLF) algorithm for node coloring."""

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
            # Jako pierwszego kolorujemy wierzcholek o najwiekszym
            # stopniu w podgrafie generowanym przez niepokolorowane.
            source = max(available_graph.iternodes(),
                key=available_graph.degree)
            self.color[source] = c
            uncolored_graph.del_node(source)
            # Wyznaczam wierzcholki bez koloru, sasiadujace z kolorem c.
            # Czyli zaden wierzcholek z neighbors nie dostanie koloru c.
            neighbors = set(available_graph.iteradjacent(source))
            # Remove source and its neighbors from available.
            to_delete = [source]
            to_delete.extend(available_graph.iteradjacent(source))
            for target in to_delete:
                available_graph.del_node(target)
            # Teraz uncolored != available.
            # Wybieramy nastepne wierzcholki do pokolorowania kolorem c.
            while available_graph.v() > 0:   # nie dla kazdej implementacji
                # Find node with the largest degree in the subgraph.
                source = max(available_graph.iternodes(), key=lambda node:
                    len(set(uncolored_graph.iteradjacent(node)) & neighbors))
                self.color[source] = c
                uncolored_graph.del_node(source)
                neighbors.union(available_graph.iteradjacent(source))
                # Remove source and its neighbors from available.
                to_delete = [source]
                to_delete.extend(available_graph.iteradjacent(source))
                for target in to_delete:
                    available_graph.del_node(target)
            c += 1


class RLFNodeColoring2:
    """Recursive Largest First (RLF) algorithm for node coloring."""

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
        # Potrzebujemy stopni wierzcholkow w malejacym grafie zawierajacym
        # tylko niepokolorowane wierzcholki.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time and memory
        colored = 0   # licznik wierzcholkow pokolorowanych
        c = 0
        while colored < n:
            # Jako pierwszego kolorujemy wierzcholek o najwiekszym
            # stopniu w podgrafie generowanym przez niepokolorowane.
            available = set(node for node in self.graph.iternodes()
                if self.color[node] is None)
            source = max(available, key=degree_dict.__getitem__)
            self.color[source] = c
            colored += 1
            # Remove source and its neighbors from available.
            available.remove(source)
            for target in self.graph.iteradjacent(source):
                available.discard(target)
                degree_dict[target] -= 1
            # Teraz uncolored != available.
            # Wyznaczam wierzcholki bez koloru, sasiadujace z kolorem c.
            # Czyli zaden wierzcholek z neighbors nie dostanie koloru c.
            neighbors = set(node for node in self.graph.iteradjacent(source)
                if self.color[node] is None)
            # Wybieramy nastepne wierzcholki do pokolorowania kolorem c.
            while available:
                # Find node with the largest degree in the subgraph.
                source = max(available, key=lambda node:
                    len(set(self.graph.iteradjacent(node)) & neighbors))
                #print dict_copy[source]   # ma byc nieujemne
                self.color[source] = c
                colored += 1
                # Remove source and its neighbors from available.
                available.remove(source)
                for target in self.graph.iteradjacent(source):
                    # target moze nie nalezec do available.
                    available.discard(target)
                    degree_dict[target] -= 1
                    if self.color[target] is None:
                        #neighbors.union([target])
                        neighbors.add(target)
            c += 1

RLFNodeColoring = RLFNodeColoring1

# EOF
