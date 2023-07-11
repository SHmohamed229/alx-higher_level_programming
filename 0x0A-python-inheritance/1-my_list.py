#!/usr/bin/python3
"""the for Defines an inherited list class MyList."""


class MyList(list):
    """for Implement sorted printing for built-in list class."""

    def print_sorted(self):
        """for Print a list in sorted ascending order."""
        print(sorted(self))
