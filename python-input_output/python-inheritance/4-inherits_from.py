#!/usr/bin/python3
"""This module defines an inherits_from function"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class

    Args:
        obj: object to check
        a_class: class to compare with

    Returns:
        True if obj is instance of a class inherited from a_class
        False if obj is directly an instance of a_class or not related
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
