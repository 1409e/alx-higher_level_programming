#!/usr/bin/python3
class Square:
    def __init__(self):
        self.__dict__ = {}

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
