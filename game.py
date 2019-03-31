class Player:
    def __init__(self):
        self.score = 0
        self.nobles = []
        self.l1_cards = []
        self.l2_cards = []
        self.l3_cards = []
        self.coins = dict()
        self.reserves = []

    def __str__(self):
        return 'Score: %s, Cards: %s, Coins; %s, Reserves: %s' % \
               (self.score, self._get_card_colors(), self.coins, self.reserves)

    def __repr__(self):
        return self.__str__()

    def _get_card_colors(self):
        return str(self.l3_cards) #todo implement function to print Map of Colors of Cards Bought

class Game:
    def __init__(self, board):
        self.p1 = Player()
        self.p2 = Player()
        self.board = board
        #todo do we want turns?

    def __str__(self):
        return str(self.board)
#   todo do we want a base object?
