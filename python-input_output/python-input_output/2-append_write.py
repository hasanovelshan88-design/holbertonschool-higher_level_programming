#!/usr/bin/python3
"""Module for appending to a file."""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns number of characters added.

    Args:
        filename: name of the file to append to
        text: text to append to the file

    Returns:
        Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
