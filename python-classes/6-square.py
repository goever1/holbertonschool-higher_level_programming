#!/usr/bin/python3
"""Defines square"""


class Square:
    """defines square with size"""

    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (type(position) == tuple and len(position) == 2):
            for value in position:
                if type(value) != int or value < 0:
                    raise TypeError(
                            "position must be a tuple fo 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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
    
    def area(self):
        """return the area of the square"""
        return self.__size**2
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple of len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) < 0 or type(value[1]) < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        if self.size > 0 and self.position[1] > 0:
            for i in range(self.position[1]):
                print()
        if self.size != 0:
            for i in range(self.size):
                for i in range(self.position[0]):
                    print(" ", end="")
                for i in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
