#!/usr/bin/python3
"""Module for VerboseList class."""


class VerboseList(list):
    """A list that prints notifications."""

    def append(self, item):
        """Append item and notify."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend list and notify."""
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove item and notify."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and notify."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
