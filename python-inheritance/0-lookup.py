#!/usr/bin/python3
"""This module defines a lookup function"""


def lookup(obj):
    """Return the list of available attributes and methods of an object

    Args:
        obj: any object

    Returns:
        list: list of attributes and methods
    """
    return dir(obj)
