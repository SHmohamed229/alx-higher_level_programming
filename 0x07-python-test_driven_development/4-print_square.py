#!/usr/bin/python3
# 4-print_square.py
"""this for Defines a square-printing function."""


def print_square(size):
    """for Print a square with the # char.

    Args:
        size (int): for The height/width of the square.
    Raises:
        TypeError: for If size is not an int.
        ValueError:for If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
