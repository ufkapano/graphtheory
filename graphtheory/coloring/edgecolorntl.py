#!/usr/bin/env python3

try:
    range = xrange
except NameError:   # Python 3
    pass

from graphtheory.coloring.edgecolorcs import ConnectedSequentialEdgeColoring


class NTLEdgeColoring:
    """Find the NTL (Nishizeki, Terada, Leven) edge coloring.
    
    The algorithm is using Delta or Delta+1 colors.
    Based on Java code from
    https://github.com/martakuzak/GIS
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with edges (values are colors)
    m : number (the number od edges)
    missing : dict with nodes (values are sets of missing colors)
    
    Notes
    -----
    Colors are 0, 1, 2, ...
    edge.source < edge.target for any edge in color.
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0   # graph.e() is slow
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
            else:
                self.color[edge] = None   # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")
        # dict with missing colors for nodes.
        self.missing = None

    def run(self, source=None):
        """Executable pseudocode."""
        Delta = max(self.graph.degree(node) for node in self.graph.iternodes())
        if Delta <= 2:
            # Greedy coloring suffies.
            algorithm = ConnectedSequentialEdgeColoring(self.graph)
            algorithm.run()
            self.color = algorithm.color
        else:
            # Ustal liczbe wykorzystywanych kolorow.
            k = Delta + 1   # almost optimal (simple graphs!)
            self.missing = dict((node, set(range(k)))
                for node in self.graph.iternodes())
            for edge in self.graph.iteredges():
                # Sprawdz wspolny kolor brakujacy.
                # To mozna chyba zrobic bardziej wydajnie.
                both = self.missing[edge.source] & self.missing[edge.target]
                if len(both) == 0:
                    self._recolor(edge)
                else:
                    c = min(both)   # choose min color available
                    self._add_color(edge, c)

    def _add_color(self, edge, c):
        """Add color."""
        if edge.source > edge.target:
            edge = ~edge
        self.color[edge] = c
        self.missing[edge.source].remove(c)
        self.missing[edge.target].remove(c)

    def _del_color(self, edge, c):
        """Delete color."""
        if edge.source > edge.target:
            edge = ~edge
        self.color[edge] = None
        self.missing[edge.source].add(c)
        self.missing[edge.target].add(c)

    def _get_color(self, edge):
        """Get color."""
        if edge.source > edge.target:
            edge = ~edge
        return self.color[edge]

    def show_colors(self):
        """Show edge coloring (undirected graphs)."""
        L = []
        for source in self.graph.iternodes():
            L.append("{} : ".format(source))
            for edge in self.graph.iteroutedges(source):
                # It should work for multigraphs.
                c = self._get_color(edge)
                L.append("{}({}) ".format(edge.target, c))
            L.append("\n")
        print("".join(L))

    def _recolor(self, edge):
        """Swap edge colors."""
        # Przygotowanie kolorow brakujacych m(*).
        mis = dict((node, min(self.missing[node]))
            for node in self.graph.iternodes())
        # 1. Tworzymy wachlarz dla krawedzi edge.
        # 2. Wachlarz rozpoczyna sie od wierzcholka w_0 (krawedz edge).
        fan = [edge]   # tu beda cale krawedzie wychodzace z edge.source
        # 3. Zbior do szybkiego sprawdzania, czy wierzcholek nalezy do wachlarza.
        fan_set = set([edge.target])   # zbior koncow krawedzi
        # 5. alpha to kolor brakujacy dla edge.source
        alpha = mis[edge.source]
        tmp_v = edge.target   # zmienna do chodzenia po koncach krawedzi wachlarza
        finished = False
        # 7. W petli szukamy kolejnych krawedzi wachlarza.
        while not finished:
            finished = True
            for edge1 in self.graph.iteroutedges(edge.source):
                # Kolor krawedzi ma byc kolorem brakujacym poprzedniego wierzcholka.
                c = self._get_color(edge1)
                if c == mis[tmp_v] and edge1.target not in fan_set:
                    # 12. Dodajemy krawedz do wachlarza.
                    tmp_v = edge1.target
                    fan.append(edge1)
                    fan_set.add(edge1.target)
                    finished = False
                    break
        # 14. Wachlarz zostal skonstruowany.
        # tmp_v oznacza teraz ostatni wierzcholek wachlarza w_s.
        # 15. Definiujemy kolor beta jako kolor brakujacy wierzcholka w_s.
        beta = mis[tmp_v]
        # 16. Jezeli kolor brakujacy w_s jest rowniez kolorem brakujacym
        # edge.source, to mozemy przesunac wachlarz, a krawedz fan[-1]
        # pokolorowac kolorem beta.
        if beta in self.missing[edge.source]:
            #print "PRZYPADEK 1"
            # 17. Przesuwamy kolory w wachlarzu.
            for i in range(len(fan)-1):
                edge1 = fan[i]
                edge2 = fan[i+1]
                c = mis[edge1.target]   # to chcemy dac edge1
                self._del_color(edge2, c)
                self._add_color(edge1, c)
            # 25. Kolor beta dajemy ostatniej krawedzi wachlarza.
            edge1 = fan[-1]
            self._add_color(edge1, beta)
        else:
            #print "PRZYPADEK 2"   # beta not in self.missing[edge.source]
            # 29. Tworzymy sciezke o poczatku w w_s i skladajaca sie
            # z krawedzi na przemian kolorow alpha i beta.
            path = []   # tu beda cale krawedzie
            path_set = set([tmp_v])   # w_s, aby przyspieszyc wyszukiwanie
            tmp2_v = tmp_v   # chodzi po wierzcholkach sciezki
            finished = False
            # 34. Zmienna parity, pozwala kontrolowac, czy nastepna krawedz
            # powinna byc pokolorowana kolorem alpha czy beta
            parity = 0
            # 35. W petli szukamy kolejnych krawedzi sciezki path.
            while not finished:
                finished = True
                if parity % 2 == 0:   # kolor alpha
                    for edge1 in self.graph.iteroutedges(tmp2_v):
                        # Kolor krawedzi ma byc alpha.
                        c = self._get_color(edge1)
                        if c == alpha and edge1.target not in path_set:
                            tmp2_v = edge1.target
                            path.append(edge1)
                            path_set.add(edge1.target)
                            finished = False
                            break
                else:   # parity % 2 == 1, kolor beta
                    for edge1 in self.graph.iteroutedges(tmp2_v):
                        # Kolor krawedzi ma byc beta.
                        c = self._get_color(edge1)
                        if c == beta and edge1.target not in path_set:
                            tmp2_v = edge1.target
                            path.append(edge1)
                            path_set.add(edge1.target)
                            finished = False
                            break
                # 44. Przed przejsciem do szukania kolejnego wierzcholka
                # sciezki zmieniamy parity.
                parity += 1
            # 45. Sciezka path zostala skonstrowana. Sciezka moze nie istniec.
            # Teraz trzeba sprawdzic, czy nie dochodzimy do edge.source
            # lub do brzegu wachlarza.
            if len(path) == 0:
                # Przesuwamy kolory w wachlarzu.
                for i in range(len(fan)-1):
                    edge1 = fan[i]
                    edge2 = fan[i+1]
                    c = mis[edge1.target]   # to chcemy dac edge1
                    self._del_color(edge2, c)
                    self._add_color(edge1, c)
                # Kolor alpha dajemy ostatniej krawedzi wachlarza.
                edge1 = fan[-1]
                self._add_color(edge1, alpha)
            elif path[-1].target == edge.source:
                # path dochodzi do edge.source kolorem beta.
                # Odwracamy kolory na sciezce.
                # Osobno usuwam, a potem dodaje kolory, aby nie posypalo
                # sie uaktualnianie kolorow w missing.
                # Najpierw usuwam kolory (pierwszy to alpha), bez ostatniego.
                for i in range(len(path)-1):   # bez ostatniej krawedzi
                    c = alpha if (i % 2 == 0) else beta
                    self._del_color(path[i], c)
                # Krawedz path[-1] nalezy do wachlarza i ma jeszcze kolor beta.
                # Przesuwamy kolory w wachlarzu, ale nie do konca.
                for i in range(len(fan)-1):
                    edge1 = fan[i]
                    edge2 = fan[i+1]
                    c = mis[edge1.target]   # to chcemy dac edge1
                    self._del_color(edge2, c)
                    self._add_color(edge1, c)
                    if c == beta:
                        break
                # Teraz jedna krawedz wachlarza, wspolna ze sciezka,
                # nie ma koloru.
                # Dodaje odwrocone kolory w path (pierwszy to beta).
                for i, edge1 in enumerate(path):   # cala sciezka
                    c = beta if (i % 2 == 0) else alpha
                    self._add_color(edge1, c)
            # Dalej path[-1].target != edge.source
            elif path[-1].target in fan_set and (len(path) % 2 == 1):
                # path ma dlugosc nieparzysta i osiaga wierzcholek
                # nalezacy do wachlarza klawedzia koloru alpha.
                # Osobno usuwam, a potem dodaje kolory, aby nie posypalo
                # sie uaktualnianie kolorow w missing.
                # Najpierw usuwam kolory (pierwszy to alpha).
                for i, edge1 in enumerate(path):   # cala sciezka
                    c = alpha if (i % 2 == 0) else beta
                    self._del_color(edge1, c)
                # Mozemy przypadkiem trafic w pierwsza krawedz wachlarza.
                if path[-1].target == edge.target:
                    # Nie przesuwamy wachlarza.
                    # Dodaje krawedz wachlarza do sciezki dla wygody.
                    path.append(~edge)   # odwrotny kierunek!
                    # Teraz sciezka ma parzysta liczbe krawedzi.
                else:
                    # Przesuwamy kolory w wachlarzu, ale nie do konca.
                    for i in range(len(fan)-1):
                        edge1 = fan[i]
                        edge2 = fan[i+1]
                        c = mis[edge1.target]   # to chcemy dac edge1
                        self._del_color(edge2, c)
                        self._add_color(edge1, c)
                        if edge2.target == path[-1].target:
                            # Dodaje krawedzi wachlarza do sciezki, aby
                            # latwiej nadac jej kolor.
                            path.append(~edge2)   # odwrotny kierunek!
                            # Teraz sciezka ma parzysta liczbe krawedzi.
                            break
                # Dodaje odwrocone kolory w path
                # (pierwszy to beta, ostatni to alpha).
                for i, edge1 in enumerate(path):
                    c = beta if (i % 2 == 0) else alpha
                    self._add_color(edge1, c)
            else:
                # path moze sie konczyc kolorem alpha lub beta.
                # Przesuwamy kolory w wachlarzu.
                for i in range(len(fan)-1):
                    edge1 = fan[i]
                    edge2 = fan[i+1]
                    c = mis[edge1.target]   # to chcemy dac edge1
                    self._del_color(edge2, c)
                    self._add_color(edge1, c)
                # Ostatnia krawedz wachlarza jest teraz bez koloru.
                # Odwracamy kolory na sciezce.
                # Osobno usuwam, a potem dodaje kolory, aby nie posypalo
                # sie uaktualnianie kolorow w missing.
                # Najpierw usuwam kolory (pierwszy to alpha).
                for i, edge1 in enumerate(path):   # cala sciezka
                    c = alpha if (i % 2 == 0) else beta
                    self._del_color(edge1, c)
                # Teraz dodaje odwrocone kolory (pierwszy to beta).
                for i, edge1 in enumerate(path):
                    c = beta if (i % 2 == 0) else alpha
                    self._add_color(edge1, c)
                # Obrocilismy sciezke.
                # Kolor alpha dajemy ostatniej krawedzi wachlarza.
                edge1 = fan[-1]
                self._add_color(edge1, alpha)

# EOF
