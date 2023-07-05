#!/usr/bin/python3
"""this for Defines a locked class."""


class LockedClass:
    """
    for Prevent the user from  new LockedClass attributes
    for anything but attribute called 'first_name'.
    """

    __slots__ = ["first_name"]
