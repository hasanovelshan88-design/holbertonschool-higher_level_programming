#!/usr/bin/python3
"""Function that replaces all occurrences of an element by another."""


def search_replace(my_list, search, replace):
    return [replace if x == search else x for x in my_list]
