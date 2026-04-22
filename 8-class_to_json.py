#!/usr/bin/python3
"""Module for JSON serialization of an object."""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization."""
    return obj.__dict__
