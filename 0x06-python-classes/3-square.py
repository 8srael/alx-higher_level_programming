#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size(int): The size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Return:
            The current square area
        """
        return self.__size * self.__size
