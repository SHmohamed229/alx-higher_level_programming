#!/usr/bin/python3
""" this class for Define a  Square."""


class Square:
    """ for Represent a square."""

    def __init__(self, size=0):
        """this for Initialize a new Square.

        Args:
            size (int): for size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
