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
        self.p1_turn = 0
        #todo do we want turns?

    def __str__(self):
        return "Board: %s\nPlayer1:%s\nPlayer2: %s" % (self.board, self.p1, self.p2)
#   todo do we want a base object?

    def is_finished(self):
        return self.p1.score >= 15 or self.p2.score >= 15

    def take_turn(self): #TODO do we need this? Could just set in
        TurnTaker.take_turn(self.p1 if self.p1_turn else self.p2, self.board)
        self.p1_turn = not self.p1_turn
