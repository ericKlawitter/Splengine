from enum import Enum


class Color(Enum):
    WHITE = 1
    BLUE = 2
    GREEN = 3
    RED = 4
    BLACK = 5
    GOLD = 6

    def __str__(self):
        return str.lower(self.name)

    def __repr__(self):
        return self.__str__()


white = Color.WHITE
blue = Color.BLUE
green = Color.GREEN
red = Color.RED
black = Color.BLACK
gold = Color.GOLD