#!/usr/bin/env python3

import math
from fractions import Fraction

class Point:
    """The class defining a point in the plane (2D vector)."""

    def __init__(self, x, y):  # konstuktor
        """Load up a point instance."""
        self.x = x
        self.y = y

    def __repr__(self):
        """Return the string representation of the point."""
        return "Point({0!r}, {1!r})".format(self.x, self.y)

    def __add__(self, other):
        """Return a new point (point1 + point2)."""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Return a new point (point1 - point2)."""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Return a dot product or a new point."""
        if isinstance(other, Point):      # point1 * point2 to iloczyn skalarny
            return (self.x * other.x + self.y * other.y)
        else:   # mnozenie przez liczbe (int, float, Fraction)
            return Point(self.x * other, self.y * other)

    __rmul__ = __mul__

    def copy(self):
        """Return a point copy."""
        #return self     # chyba tez mozna, bo niezmienne
        return Point(self.x, self.y)   # inna instancja

    def cross(self, other):
        """Return the cross product in 2D (a number)."""
        return (self.x * other.y - self.y * other.x)

    def __pos__(self):
        """Return +point."""
        return self

    def __neg__(self):
        """Return -point = (-1) * point."""
        return Point(-self.x, -self.y)

    def length(self):
        """Return the points length."""
        return math.hypot(self.x, self.y)

    def __abs__(self):
        """Return the points length."""
        return math.hypot(self.x, self.y)

    def alpha(self):
        """A monotonic function of an angle.
        
        http://www.algorytm.org/geometria-obliczeniowa/porzadkowanie-wierzcholkow-wg-rosnacych-katow-nachylenia-ich-wektorow-wodzacych.html
        """
        if self.x == 0 and self.y == 0:
            #raise ValueError("alpha() not defined")
            return 0   # wygodna konwencja
        distance = abs(self.x) + abs(self.y)
        if isinstance(distance, float):
            if self.x >= 0 and self.y >= 0:  # I cwiartka
                return self.y / distance
            elif self.x < 0 and self.y >= 0:  # II cwiartka
                return 2.0 - (self.y / distance)
            elif self.x < 0 and self.y < 0:  # III cwiartka
                return 2.0 + (-self.y / distance)
            elif self.x >= 0 and self.y < 0:  # IV cwiartka
                return 4.0 - (-self.y / distance)
        else:
            if self.x >= 0 and self.y >= 0:  # I cwiartka
                return Fraction(self.y, distance)
            elif self.x < 0 and self.y >= 0:  # II cwiartka
                return 2 - Fraction(self.y, distance)
            elif self.x < 0 and self.y < 0:  # III cwiartka
                return 2 + Fraction(-self.y, distance)
            elif self.x >= 0 and self.y < 0:  # IV cwiartka
                return 4 - Fraction(-self.y, distance)

    def __eq__(self, other):
        """Points comparison (like 2-tuple)."""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """Points comparison (like 2-tuple)."""
        return not (self == other)

    def __lt__(self, other):
        """Points comparison (like 2-tuple)."""
        return (self.x, self.y) < (other.x, other.y)

    def __le__(self, other):
        """Points comparison (like 2-tuple)."""
        return (self.x, self.y) <= (other.x, other.y)

    def __gt__(self, other):
        """Points comparison (like 2-tuple)."""
        return (self.x, self.y) > (other.x, other.y)

    def __ge__(self, other):
        """Points comparison (like 2-tuple)."""
        return (self.x, self.y) >= (other.x, other.y)

    def __cmp__(self, other):   # Python 2 only
        """Points comparison (like 2-tuple)."""
        return cmp((self.x, self.y), (other.x, other.y))

    def __hash__(self):
        """Hashable points."""
        return hash((self.x, self.y))   # hash based on tuple

# EOF
