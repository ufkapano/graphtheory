#!/usr/bin/env python3
#
# Tools for circular-arc graphs.

import random
import itertools
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph


def make_random_arc(n):
    """Return a random circular-arc graph as a list of pairs."""
    assert n > 0
    events = list(range(2*n))
    random.shuffle(events)
    head, tail = events[0], events[1]
    # Przenumerowuje, zeby dostac events[0] == 0 < events[1] (forward arc).
    events = [(event + 2*n -head) % (2*n) for event in events]
    reprB = [(events[i], events[i+1]) for i in range(0, 2*n, 2)]
    reprB.sort()   # a canonical form from [1988 Masuda Nakajima]
    return reprB


def make_cycle_arc(n):
    """Return a cycle circular-arc graph C_n as a list of pairs."""
    assert n > 2
    reprB = [(2*i, (2*i+3) % (2*n)) for i in range(n)]
    return reprB   # a canonical form from [1988 Masuda Nakajima]


def make_complete_arc(n):
    """Return a complete circular-arc graph K_n as a list of pairs."""
    assert n > 0
    reprB = [(i, i+n) for i in range(n)]   # only forward arcs
    return reprB   # a canonical form from [1988 Masuda Nakajima]


def make_abstract_arc_graph(reprB):
    """Finding an abstract circular-arc graph from a representation B, O(n+m) time."""
    # Nie jest potrzebna postac kanoniczna.
    n = len(reprB)
    graph = Graph()
    # arc to etykiety/numery przedzialow/lukow.
    # reprB[arc] zwraca (head, tail).
    D = {}   # pary (event, arc)
    for (arc, (head, tail)) in enumerate(reprB):   # O(n)
        D[head] = arc
        D[tail] = arc
    active = set()

    # Pierwsza petla 'for' nie uwzglednia zawinietych lukow.
    for event in range(2*n):
        curr_arc = D[event]   # etykieta luku
        head, tail = reprB[curr_arc]   # mamy zapisane konce
        if event == head:   # dodajemy nowy luk, jestesmy w head
            graph.add_node(curr_arc)
            for arc in active:
                graph.add_edge(Edge(curr_arc, arc))
            active.add(curr_arc)
        else:   # event == tail
            active.discard(curr_arc)   # tu gubimy wsteczne luki

    # W tym momencie zbior 'active' zawiera tylko wsteczne krawedzie.
    #print("active po pierwszym for ...")
    #print(active)
    for event in range(2*n):
        curr_arc = D[event]   # etykieta luku
        head, tail = reprB[curr_arc]   # mamy zapisane konce
        if event == head:   # zaczyna sie nowy luk
            if head < tail:   # czyli jest zwykly luk
                for arc in active:   # sprawdzamy wsteczne luki
                    head_backward, tail_backward = reprB[arc]
                    if tail < head_backward:
                        # nie bylo przeciecia w pierwszej petli for
                        graph.add_edge(Edge(curr_arc, arc))
        else:   # event == tail
            active.discard(curr_arc)   # tu zwykle luki tez porzucamy
        if len(active) == 0:
            break   # dalej nie siegaja wsteczne krawedzie
    return graph


def make_abstract_arc_graph2(reprB):
    """Finding an abstract circular-arc graph from a representation B, O(n^2) time."""
    # Tu kolejnosc przedzialow podawanych w reprB nie jest istotna.
    graph = Graph(n=len(reprB))
    n = len(reprB)
    for arc in range(n):
        graph.add_node(arc)
    # Dla roznych par lukow sprawdzam przeciecie.
    for (arc1, arc2) in itertools.combinations(range(n), 2):
        head1, tail1 = reprB[arc1]
        head2, tail2 = reprB[arc2]
        tests = [False] * 12
        # Lapiemy koniec arc2 wewnatrz arc1.
        # Nie ma przypadku, gdy arc2 zawiera arc1!
        tests[0] = head1 < head2 < tail1   # arc1 zwykly
        tests[1] = head1 < tail2 < tail1   # arc1 zwykly
        tests[2] = tail1 < head1 < head2   # arc1 zawija sie
        tests[3] = tail1 < head1 < tail2   # arc1 zawija sie
        tests[4] = head2 < tail1 < head1   # arc1 zawija sie
        tests[5] = tail2 < tail1 < head1   # arc1 zawija sie
        # Lapiemy koniec arc1 wewnatrz arc2.
        # Nie ma przypadku, gdy arc1 zawiera arc2!
        tests[6] = head2 < head1 < tail2   # arc2 zwykly
        tests[7] = head2 < tail1 < tail2   # arc2 zwykly
        tests[8] = tail2 < head2 < head1   # arc2 zawija sie
        tests[9] = tail2 < head2 < tail1   # arc2 zawija sie
        tests[10] = head1 < tail2 < head2   # arc2 zawija sie
        tests[11] = tail1 < tail2 < head2   # arc2 zawija sie
        if any(tests):
            graph.add_edge(Edge(arc1, arc2))
    return graph

# EOF
