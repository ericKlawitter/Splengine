from game import Game
from board import Board, Noble
from picker import SetupPicker, TurnPicker
from colors import *
from cards import cards_one, cards_two, cards_three
import argparse

card_row_length = 4
number_of_nobles = 3


def all_nobles():
    return [Noble({white: 4, blue: 4}), Noble({blue: 4, green: 4}), Noble({green: 4, red: 4}),
            Noble({red: 4, black: 4}), Noble({white: 4, black: 4}), Noble({white: 3, blue: 3, green: 3}),
            Noble({blue: 3, green: 3, red: 3}), Noble({green: 3, red: 3, black: 3}),
            Noble({white: 3, red: 3, black: 3}), Noble({white: 3, blue: 3, black: 3})]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", help="Run without user input. For quick testing.", action="store_true")
    if parser.parse_args().dry_run:
        board = Board(cards_one[0:card_row_length],
                      cards_two[0:card_row_length],
                      cards_three[0:card_row_length],
                      all_nobles()[0:number_of_nobles])
    else:
        board = Board(SetupPicker.pick(cards_one, card_row_length),
                      SetupPicker.pick(cards_two, card_row_length),
                      SetupPicker.pick(cards_three, card_row_length),
                      SetupPicker.pick(all_nobles(), number_of_nobles))
    game = Game(board)
    print(game)
    while not game.is_finished():
        TurnPicker.take_turn(game)
        game.p1_turn = not game.p1_turn



