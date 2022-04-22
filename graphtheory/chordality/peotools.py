#!/usr/bin/env python3
"""
https://en.wikipedia.org/wiki/Chordal_graph

PEO = Perfect Elimination Ordering
"""

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

def find_peo_mcs(graph):   # to nie jest najszybsza wersja!
    """Finding PEO in a chordal graph using maximum cardinality search."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    order = list()   # PEO
    used = set()
    visited_degree = dict((node, 0) for node in graph.iternodes())
    for step in range(graph.v()):   # all nodes in the loop
        source = max((node for node in graph.iternodes() if node not in used),
            key=visited_degree.__getitem__)   # O(V) time przy szybkim tescie
        order.append(source)
        used.add(source)
        # Update visited degree.
        for target in graph.iteradjacent(source):   # total O(E) time
            visited_degree[target] += 1
    order.reverse()   # O(V) time
    return order


def find_maximum_clique_peo(graph, order):
    """Find a maximum clique in a chordal graph using PEO."""
    max_clique = set()   # kandydat na klike najwieksza
    # Indices of nodes in PEO.
    M = dict((node, i) for (i, node) in enumerate(order))   # O(V) time
    for source in order:
        clique = set([source])
        for target in graph.iteradjacent(source): # total O(E) time
            if M[source] < M[target]:
                clique.add(target)
        max_clique = max(clique, max_clique, key=len)
    return max_clique


def find_all_maximal_cliques(graph, order):
    """Find all maximal cliques in a chordal graph using PEO."""
    # Algorithm 4.3 [2004 Golumbic] .. 99.
    # Nie obliczam liczby chromatycznej (rozmiar najwiekszej kliki)
    cliques = []   # lista klik maksymalnych
    # Indices of nodes in PEO.
    M = dict((node, i) for (i, node) in enumerate(order))   # O(V) time
    # S[node] to rozmiar najwiekszego zbioru, ktory bylby dolaczony
    # do A[node] w algorytmie 4.2 [2004 Golumbic].
    S = dict((node, 0) for node in order)
    for source in order:
        X = set()
        for target in graph.iteradjacent(source): # total O(E) time
            if M[source] < M[target]:
                X.add(target)
        if graph.degree(source) == 0:
            cliques.append(set([source]))
        if not X:
            continue
        node = min(X, key=M.__getitem__)   # najblizej source
        S[node] = max(S[node], len(X)-1)
        if S[source] < len(X):
            cliques.append(X | set([source]))
    return cliques


def is_peo1(graph, order):
    """Testing PEO, return bool, O(V+E) time."""
    # Algorithm 4.2 [2004 Golumbic] p. 88.
    # Slownik trzymajacy numery wierzcholkow w PEO.
    M = dict((node, i) for (i, node) in enumerate(order))   # O(V) time
    # Lista/zbior wierzcholkow do sprawdzenia.
    A = dict((node, set()) for node in order)   # O(V) time
    for source in order:
        # X to zbior sasiadow source na prawo w PEO.
        X = set()
        for target in graph.iteradjacent(source): # sumarycznie O(E) time
            if M[source] < M[target]:
                X.add(target)
        if X:
            target = min(X, key=M.__getitem__)   # najblizej source
            A[target].update(X - set([target]))
        # Testowanie A na zbiorach.
        if A[source] - set(graph.iteradjacent(source)):
            # Ma zostac zbior pusty, bo wierzcholki w A[source]
            # powinny tworzyc klike z source we wczesniejszej iteracji.
            return False
    return True


def is_peo2(graph, order):
    """Testing PEO, return bool, O(V+E) time."""
    # Algorithm 4.2 [2004 Golumbic] p. 88.
    # Nie uzywam zbiorow tylko wszedzie listy.
    # Slownik trzymajacy numery wierzcholkow w PEO.
    M = dict((node, i) for (i, node) in enumerate(order))   # O(V) time
    # Lista wierzcholkow do sprawdzenia.
    # Tutaj moga pojawic sie powtorzenia wierzcholkow, bo jest lista.
    A = dict((node, []) for node in order)   # O(V) time
    # Pomocniczy slownik do testowania A.
    D = dict((node, 0) for node in order)
    for source in order:
        # X to lista sasiadow source na prawo w PEO.
        X = []
        # Indeks elementu najblizej source po prawej.
        min_idx = len(order)   # indeks wiekszy od prawidlowych
        for target in graph.iteradjacent(source): # sumarycznie O(E) time
            if M[source] < M[target]:
                X.append(target)
                min_idx = min(min_idx, M[target])
        #if min_idex < len(order):   # inna mozliwosc
        if X:
            target = order[min_idx]
            A[target].extend(node for node in X if node != target)
            #print "A[]", target, A[target]
        else:
            # Tutaj wchodzimy przy koncu kazdej spojnej skladowej grafu.
            #print "X is empty"
            pass
        # Testowanie A na slownikach, razem czas O(E).
        for target in graph.iteradjacent(source):
            D[target] = 1
        for target in A[source]:
            if D[target] == 0:   # nie jest w otoczeniu source
                return False
        for target in graph.iteradjacent(source):
            D[target] = 0
    return True

# EOF
