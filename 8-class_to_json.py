#!/usr/bin/python3
"""Module that returns dictionary description for JSON serialization of an object."""


def class_to_json(obj):
    """Returns dictionary description with simple data structure for JSON serialization."""
    return obj.__dict__
