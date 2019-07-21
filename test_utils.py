from board import Noble
from board import Board
from game import Game
from colors import *

nobles = [Noble({white: 4, blue: 4}), Noble({blue: 4, green: 4}), Noble({green: 4, red: 4}),
          Noble({red: 4, black: 4}), Noble({white: 4, black: 4}), Noble({white: 3, blue: 3, green: 3}),
          Noble({blue: 3, green: 3, red: 3}), Noble({green: 3, red: 3, black: 3}),
          Noble({white: 3, red: 3, black: 3}), Noble({white: 3, blue: 3, black: 3})]
board = Board([], [], [], nobles) #Todo add cards
game = Game(board)


