#!/usr/bin/env python3

from abc import ABC, abstractmethod


class BaseGraph(ABC):

    @abstractmethod
    def is_directed(self): pass

    @abstractmethod
    def v(self): pass

    @abstractmethod
    def e(self): pass

    #@abstractmethod
    #def f(self): pass

    #@abstractmethod
    #def iterfaces(self): pass

    #@abstractmethod
    #def iterface(self, start_edge): pass

    @abstractmethod
    def add_node(self, node): pass

    @abstractmethod
    def del_node(self, node): pass

    @abstractmethod
    def has_node(self, node): pass

    @abstractmethod
    def add_edge(self, edge): pass

    @abstractmethod
    def del_edge(self, edge): pass

    @abstractmethod
    def has_edge(self, edge): pass

    @abstractmethod
    def weight(self, edge): pass

    @abstractmethod
    def iternodes(self): pass

    @abstractmethod
    def iteredges(self): pass

    #@abstractmethod
    #def iteredges_connected(self, start_edge): pass

    @abstractmethod
    def iteradjacent(self, source): pass

    @abstractmethod
    def iteroutedges(self, source): pass

    @abstractmethod
    def iterinedges(self, source): pass

    @abstractmethod
    def degree(self, node): pass

    @abstractmethod
    def indegree(self, node): pass

    @abstractmethod
    def outdegree(self, node): pass

    @abstractmethod
    def show(self): pass

    @abstractmethod
    def copy(self): pass

    @abstractmethod
    def transpose(self): pass

    @abstractmethod
    def complement(self): pass

    @abstractmethod
    def subgraph(self, nodes): pass

    @abstractmethod
    def add_graph(self, other): pass

    @abstractmethod
    def __eq__(self, other): pass

    @abstractmethod
    def __ne__(self, other): pass
