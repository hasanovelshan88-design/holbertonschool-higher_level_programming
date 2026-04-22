#!/usr/bin/python3
"""Module for loading object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename: name of the JSON file to read

    Returns:
        Python object represented by the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
