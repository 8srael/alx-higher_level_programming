#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size(int): The size of a new square
        """

        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns:
            The current area of the square.
        """
        return self.__size * self.__size
