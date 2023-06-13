#!/usr/bin/python3
"""Defines square"""

class Square:
    """defines square with size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    """ Return size"""
    @property
    def size(self):
        return self.__size

    """ defines size"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size**2

    def my_print(self):
        for i in range(self.size):
            for i in range(self.size):
                print("#", end="")
            print()
        if self.size == 0:
            print()
