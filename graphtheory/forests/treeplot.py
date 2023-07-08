#!/usr/bin/env python3

import math
from fractions import Fraction
from graphtheory.forests.treecenter import TreeCenter
from graphtheory.structures.points import Point


class TreePlot:
    """Finding the positions of tree nodes in the plane.
    
    This is not suitable for large trees (n > 1e4) due to
    numerical errors. For large trees use TreePlotRadiusAngle
    with fractions.
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.point_dict = dict()
        self.radius = 1.0

    def run(self, root=None):
        """Executable pseudocode."""
        if root is None:
            algorithm = TreeCenter(self.graph)
            algorithm.run()
            root = algorithm.tree_center[0]
        self.plot(root, 0.0, 2.0 * math.pi, level=0)

    def plot(self, source, left, right, level):
        """Find node positions.
        
        Parameters
        ----------
        source : current node
        left, right : an angle range for the current node and his children
        level : distance (steps) from the root
        """
        angle = 0.5 * (left + right)
        x = self.radius * level * math.cos(angle)
        y = self.radius * level * math.sin(angle)
        self.point_dict[source] = Point(x, y)
        deg = self.graph.degree(source)
        if level == 0:   # current node is root
            if deg == 0:   # G.v() == 1, isolated node
                return
            else:   # all neighbors have to be plotted
                delta = (right - left) / deg
        else:
            if deg == 1:   # hanging node
                return
            else:   # neighbors without already visited node
                delta = (right - left) / (deg - 1.0)
        for target in self.graph.iteradjacent(source):
            if target not in self.point_dict:
                self.plot(target, left, left + delta, level + 1)
                left = left + delta


class TreePlotRadiusAngle:
    """Finding the positions of tree nodes in the plane (radius, angle)."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.point_dict = dict()
        self.radius = 1

    def run(self, root=None):
        """Executable pseudocode."""
        if root is None:
            algorithm = TreeCenter(self.graph)
            algorithm.run()
            root = algorithm.tree_center[0]
        self.plot(root, 0, 6, level=0)

    def plot(self, source, left, right, level):
        """Find node positions (radius, angle).
        
        Parameters
        ----------
        source : current node
        left, right : an angle range for the current node and his children
        level : distance (steps) from the root
        """
        assert isinstance(left, (int, Fraction))
        assert isinstance(right, (int, Fraction))
        angle = Fraction(left + right, 2)
        self.point_dict[source] = (self.radius * level, angle)
        deg = self.graph.degree(source)
        if level == 0:   # current node is root
            if deg == 0:   # G.v() == 1, isolated node
                return
            else:   # all neighbors have to be plotted
                delta = Fraction(right - left, deg)
        else:
            if deg == 1:   # hanging node
                return
            else:   # neighbors without already visited node
                delta = Fraction(right - left, deg - 1)
        for target in self.graph.iteradjacent(source):
            if target not in self.point_dict:
                self.plot(target, left, left + delta, level + 1)
                left = left + delta

# EOF
