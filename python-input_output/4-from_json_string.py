#!/usr/bin/python3
"""Module for converting JSON string to object."""
import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string.

    Args:
        my_str: JSON string to convert

    Returns:
        Python object represented by my_str
    """
    return json.loads(my_str)
