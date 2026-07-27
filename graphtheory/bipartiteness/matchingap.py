#!/usr/bin/env python3

# no recursion
from graphtheory.bipartiteness.bipartite import BipartiteGraphBFS as Bipartite
# with recursion
#from graphtheory.bipartiteness.bipartite import BipartiteGraphDFS as Bipartite


class MatchingUsingAugmentingPath:
    """Maximum-cardinality matching using the Ford-Fulkerson method.
    
    Attributes
    ----------
    graph : input bipartite graph
    mate : a dict with nodes (values are nodes or None)
    cardinality : number
    v1 : the first set of nodes
    v2 : the second set of nodes
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0
        algorithm = Bipartite(self.graph)
        algorithm.run()   # O(n+m) time
        self.v1 = set()
        self.v2 = set()
        for node in self.graph.iternodes():   # O(n) time
            if algorithm.color[node] == 1:
                self.v1.add(node)
            else:
                self.v2.add(node)

    def run(self):
        """Executable pseudocode."""
        while True:
            path_dict = self._find_augmenting_path()
            if path_dict:
                self.mate.update(path_dict)
                self.cardinality += 1
            else:
                break

    def _find_augmenting_path(self):
        """Finding an augmenting path."""
        # Szukamy zbiorow wierzcholkow wolnych.
        self.v1free = set(node for node in self.v1 if self.mate[node] is None)
        self.v2free = set(node for node in self.v2 if self.mate[node] is None)
        for node in self.v1free:
            self.visited_e = set()   # zapisujemy krawedzie w obie strony
            self.visited_v = list()   # lista wierzcholkow na sciezce (sa cykle!)
            last_node = self._visit(node)   # jak sie nie uda to wyjdzie node
            if last_node in self.v2free:
                path = self._remove_cycles()
                return self._create_path_dict(path)
        return {}

    def _visit(self, source):
        """Finding matching using DFS."""
        self.visited_v.append(source)
        for edge in self.graph.iteroutedges(source):
            if edge not in self.visited_e:
                # Tutaj decydujemy o dozwolonym kierunku krawedzi.
                if self._is_entering(edge) or self._is_outgoing(edge):
                    self.visited_e.add(edge)
                    self.visited_e.add(~edge)
                    last_node = self._visit(edge.target)
                    if last_node in self.v2free:
                        return last_node   # przekazujemy wyzej
        # Czyszczenie, chyba ze jestesmy w v2free.
        if source not in self.v2free:
            self.visited_v.pop()
        return source

    def _is_entering(self, edge):   # from v1 to v2, edge not in matching
        # Na wazniaku to nie jest dobrze opisane w definicji grafu G_M
        # i zbioru jego krawedzi E_M.
        return edge.target in self.v2 and self.mate[edge.target] != edge.source

    def _is_outgoing(self, edge):   # from v2 to v1, edge in matching
        return edge.target in self.v1 and self.mate[edge.target] == edge.source

    def _remove_cycles(self):
        """Removing cycles from the path."""
        # Najpierw zaznaczam koniec sciezki.
        node_next = {self.visited_v[-1]: None}
        for i in range(len(self.visited_v)-1):
            node_next[self.visited_v[i]] = self.visited_v[i+1]
        # Buduje sciezke bez cykli od poczatku.
        new_path = []
        node = self.visited_v[0]
        while node is not None:
            new_path.append(node)
            node = node_next[node]
        return new_path

    def _create_path_dict(self, path):
        """Create a dict to update matching."""
        path_dict = dict()
        i = 0
        while i < len(path):   # len(path) is even
            source = path[i]
            target = path[i + 1]
            path_dict[source] = target
            path_dict[target] = source
            i += 2
        return path_dict

# EOF
