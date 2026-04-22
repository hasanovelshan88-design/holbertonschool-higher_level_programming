#!/usr/bin/python3
"""Module for converting object to JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj: object to convert to JSON string

    Returns:
        JSON string representation of my_obj
    """
    return json.dumps(my_obj)
