#!/usr/bin/python3
"""Module for reading a file."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.

    Args:
        filename: name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
