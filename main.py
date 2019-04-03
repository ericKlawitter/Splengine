from game import Game
from board import Board, Noble
from picker import SetupPicker
from colors import *
from cards import cards_one, cards_two, cards_three


def all_nobles():
    return [Noble({white: 4, blue: 4}), Noble({blue: 4, green: 4}), Noble({green: 4, red: 4}),
            Noble({red: 4, black: 4}), Noble({white: 4, black: 4}), Noble({white: 3, blue: 3, green: 3}),
            Noble({blue: 3, green: 3, red: 3}), Noble({green: 3, red: 3, black: 3}),
            Noble({white: 3, red: 3, black: 3}), Noble({white: 3, blue: 3, black: 3})]


if __name__ == '__main__':
    board = Board(SetupPicker(cards_one, 4).pick(),
                  SetupPicker(cards_two, 4).pick(),
                  SetupPicker(cards_three, 4).pick(),
                  SetupPicker(all_nobles(), 3).pick())
    print(board)
