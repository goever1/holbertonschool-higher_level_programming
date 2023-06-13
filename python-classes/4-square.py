#!/usr/bin/python3
"""Defines square"""


class Square:
    """defines square with size"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def area(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Return the area of the square"""
        return self.__size**2
