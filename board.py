from colors import *


class Noble:
    def __init__(self, costs):
        self.points = 3
        self.required_cards = costs

    def __str__(self):
        return "Points: %s Required Cards: %s" % (self.points, self.required_cards)

    def __repr__(self):
        return self.__str__()


class Board:
    def __init__(self, level_one_cards, level_two_cards, level_three_cards, nobles):
        self.l1_cards = level_one_cards
        self.l2_cards = level_two_cards
        self.l3_cards = level_three_cards
        self.nobles = nobles
        self.coins = {white: 4, blue: 4, green: 4, red: 4, black: 4, gold: 5}

    def __str__(self): #TODO print nobles, maybe periodically
        return 'L3: %s\n\nL2: %s\n\nL1: %s\n\nCoins: %s' % (self.l3_cards, self.l2_cards, self.l1_cards, self.coins)

    def __repr__(self):
        return self.__str__()
