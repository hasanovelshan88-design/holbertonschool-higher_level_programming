#!/usr/bin/python3
"""Module that inserts a line of text after each line containing a string."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line after each line containing a specific string."""
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
