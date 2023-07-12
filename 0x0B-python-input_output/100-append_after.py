#!/usr/bin/python3
"""this for Define a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """this for Insert text after each line containing a given str in a file.

    Args:
        filename (str): for name of the file.
        search_string (str):for str to search for within the file.
        new_string (str): for  str  to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
