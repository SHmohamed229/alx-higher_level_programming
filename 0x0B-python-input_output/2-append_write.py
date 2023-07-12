#!/usr/bin/python3
"""this for Defines a file-appending function."""


def append_write(filename="", text=""):
    """for Appends a str to the end of a UTF8 text file.

    Args:
        filename (str): for name of the file to append to.
        text (str):for str to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
