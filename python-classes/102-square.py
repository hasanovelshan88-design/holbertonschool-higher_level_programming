#!/usr/bin/python3
"""Module that defines a Square class with comparators."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initializes a new Square."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equal comparator based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparator based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparator based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparator based on area."""
        return self.area() >= other.area()
