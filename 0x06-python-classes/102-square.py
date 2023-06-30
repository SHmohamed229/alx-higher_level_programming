#!/usr/bin/python3
""" this class for Define a  Square."""


class Square:
    """ for Represent a square."""

    def __init__(self, size=0):
        """ this for Initialize a new square.

        Args:
            size (int): for The size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of  square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ for Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """ for Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """for Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """ for Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """ for Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """ for Define the >= compmarison to a Square."""
        return self.area() >= other.area()
