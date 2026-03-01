#!/usr/bin/python3
"""This module defines an is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or inherited from, a_class

    Args:
        obj: object to check
        a_class: class to compare with

    Returns:
        True if obj is an instance of a_class or inherited from it
        False otherwise
    """
    return isinstance(obj, a_class)
