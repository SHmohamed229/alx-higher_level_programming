#!/usr/bin/python3


def safe_print_integer(value):
    """ for Print an int with "{:d}".format().

    Args:
        for value (int): The integer to print.

    Returns:
        False - If a TypeError or ValueError occurs
        True -  Otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
