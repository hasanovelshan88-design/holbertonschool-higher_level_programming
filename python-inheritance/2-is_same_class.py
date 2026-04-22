#!/usr/bin/python3
"""This module defines an is_same_class function"""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class

    Args:
        obj: object to check
        a_class: class to compare with

    Returns:
        True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
