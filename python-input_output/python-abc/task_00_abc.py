#!/usr/bin/python3
"""Module for Abstract Animal class."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal class."""

    @abstractmethod
    def sound(self):
        """Abstract sound method."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Returns Bark."""
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Returns Meow."""
        return "Meow"
