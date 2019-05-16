# Position.py
# author:
# date: 04/12/2018

class Position:

    # x: row, y : colon
    def __init__(self, orientation, x, y):
        self.__x = x
        self.__y = y
        self.__orientation = orientation

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, value):
        self.__orientation = value