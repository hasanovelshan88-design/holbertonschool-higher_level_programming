#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size: size of the square (default 0)
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value: size value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
