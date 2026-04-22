#!/usr/bin/python3
"""Module for writing to a file."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of characters written.

    Args:
        filename: name of the file to write
        text: text to write to the file

    Returns:
        Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
