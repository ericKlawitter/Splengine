from colors import *


class Card:
    def __init__(self, points, color, costs): #todo want level?
        self.points = points
        self.color = color
        self.costs = costs

    def __str__(self):
        return 'Points: %s\nColor: %s\nCosts: %s\n' % (self.points, self.color, self.costs)

    def __repr__(self):
        return self.__str__()


cards_one = (Card(0, white, {white: 3, blue: 1, black: 1}),
             Card(0, white, {red: 2, black: 1}),
             Card(0, white, {blue: 3}),
             Card(0, white, {blue: 2, black: 2}),
             Card(0, white, {blue: 1, green: 1, red: 1, black: 1}),
             Card(0, white, {blue: 1, green: 2, red: 1, black: 1}),
             Card(0, white, {blue: 2, green: 2, black: 1}),
             Card(1, white, {green: 4}),

             Card(0, blue, {blue: 1, green: 3, red: 1}),
             Card(0, blue, {white: 1, black: 2}),
             Card(0, blue, {black: 3}),
             Card(0, blue, {green: 2, black: 2}),
             Card(0, blue, {white: 1, green: 1, red: 1, black: 1}),
             Card(0, blue, {white: 1, green: 1, red: 2, black: 1}),
             Card(0, blue, {white: 1, green: 2, red: 2}),
             Card(1, blue, {red: 4}),

             Card(0, green, {white: 1, blue: 3, green: 1}),
             Card(0, green, {white: 2, blue: 1}),
             Card(0, green, {red: 3}),
             Card(0, green, {blue: 2, red: 2}),
             Card(0, green, {white: 1, blue: 1, red: 1, black: 1}),
             Card(0, green, {white: 1, blue: 1, red: 1, black: 2}),
             Card(0, green, {blue: 1, red: 2, black: 2}),
             Card(1, green, {black: 4}),

             Card(0, red, {white: 1, red: 1, black: 3}),
             Card(0, red, {blue: 2, green: 1}),
             Card(0, red, {white: 3}),
             Card(0, red, {white: 2, red: 2}),
             Card(0, red, {white: 1, blue: 1, green: 1, black: 1}),
             Card(0, red, {white: 2, blue: 1, green: 1, black: 1}),
             Card(0, red, {white: 2, green: 1, black: 2}),
             Card(1, red, {white: 4}),

             Card(0, black, {green: 1, red: 3, black : 1}),
             Card(0, black, {green: 2, red: 1}),
             Card(0, black, {green: 3}),
             Card(0, black, {white: 2, green: 2}),
             Card(0, black, {white: 1, blue: 1, green: 1, red: 1}),
             Card(0, black, {white: 1, blue: 2, green: 1, red: 1}),
             Card(0, black, {white: 2, blue: 2, red: 1}),
             Card(1, black, {blue: 4}))

cards_two = (Card(1, white, {green: 3, red: 2, black: 2}),
             Card(1, white, {white: 2, blue: 3, red: 3}),
             Card(2, white, {red: 5}),
             Card(2, white, {red: 5, black: 3}),
             Card(2, white, {green: 1, red: 4, black: 2}),
             Card(3, white, {white: 6}),

             Card(1, blue, {blue: 2, green: 2, red: 3}),
             Card(1, blue, {blue: 2, green: 3, black: 3}),
             Card(2, blue, {blue: 5}),
             Card(2, blue, {white: 5, blue: 3}),
             Card(3, blue, {blue: 6}),

             Card(1, green, {white: 2, blue: 3, black: 2}),
             Card(1, green, {white: 3, green: 2, red: 3}),
             Card(2, green, {green: 5}),
             Card(2, green, {blue: 5, green: 3}),
             Card(2, green, {white: 4, blue: 2, black: 1}),
             Card(3, green, {green: 6}),

             Card(1, red, {white: 2, red: 2, black: 3}),
             Card(1, red, {blue: 3, red: 2, black: 3}),
             Card(2, red, {black: 5}),
             Card(2, red, {white: 3, black: 5}),
             Card(2, red, {white: 1, blue: 4, green: 2}),
             Card(3, red, {red: 6}),

             Card(1, black, {white: 3, blue: 2, green: 2}),
             Card(1, black, {white: 3, green: 3, black: 2}),
             Card(2, black, {white: 5}),
             Card(2, black, {green: 5, red: 3}),
             Card(2, black, {blue: 2, green: 4, red: 2}),
             Card(3, black, {black: 6}))

cards_three = (Card(3, white, {blue: 3, green: 3, red: 5, black: 3}),
               Card(4, white, {black: 7}),
               Card(4, white, {white: 3, red: 3, black: 6}),
               Card(5, white, {white: 3, red: 7}),

               Card(3, blue, {white: 3, green: 3, red: 3, black: 5}),
               Card(4, blue, {white: 7}),
               Card(4, blue, {white: 6, blue: 3, black: 3}),
               Card(5, blue, {white: 7, blue: 3}),

               Card(3, green, {white: 5, blue: 3, red: 3, black: 3}),
               Card(4, green, {blue: 7}),
               Card(4, green, {white: 3, blue: 6, green: 3}),
               Card(5, green, {blue: 7, green: 3}),

               Card(3, red, {white: 3, blue: 5, green: 3, black: 5}),
               Card(4, red, {green: 7}),
               Card(4, red, {blue: 3, green: 6, red: 3}),
               Card(5, red, {green: 7, red: 3}),

               Card(3, black, {white: 3, blue: 3, green: 5, red: 3}),
               Card(4, black, {red: 7}),
               Card(4, black, {green: 3, red: 6, black: 3}),
               Card(5, black, {red: 7, black: 3}))
