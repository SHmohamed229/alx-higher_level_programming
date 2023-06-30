#!/usr/bin/python3
""" this for Define a MagicClass exactly a provided by Holberton."""

import math


class MagicClass:
    """ for Represent a circle."""

    def __init__(self, radius=0):
        """ this for Initialize a MagicClass.

        Arg:
            radius (float or int): for The radius of new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of MagicClass."""
        return (2 * math.pi * self.__radius)
