#!/usr/bin/python3
"""Module for CountedIterator class."""


class CountedIterator:
    """An iterator that counts fetched items."""

    def __init__(self, iterable):
        """Initialize with iterator and counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Returns self."""
        return self

    def __next__(self):
        """Returns next item and increments counter."""
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """Returns current counter value."""
        return self.counter
