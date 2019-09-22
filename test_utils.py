from board import Noble
from board import Board
from game import Game
from game import Player
from cards import Card
from colors import *

nobles = [Noble({white: 4, blue: 4}), Noble({blue: 4, green: 4}), Noble({green: 4, red: 4}),
          Noble({red: 4, black: 4}), Noble({white: 4, black: 4}), Noble({white: 3, blue: 3, green: 3}),
          Noble({blue: 3, green: 3, red: 3}), Noble({green: 3, red: 3, black: 3}),
          Noble({white: 3, red: 3, black: 3}), Noble({white: 3, blue: 3, black: 3})]
board = Board([], [], [], nobles) #Todo add cards
game = Game(board)
player = Player()
player.coins = {white: 2, black: 2, gold: 1, blue: 3}
player.cards_bought = [Card(0, white, {}), Card(1, white, {}), Card(2, red, {})]
player.reserves = [Card(0, blue, {white: 1, green: 1, red: 2, black: 1})]
