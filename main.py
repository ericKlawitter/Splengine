from game import Game
from board import Board, Noble
from colors import *


def all_nobles():
    return [Noble({white: 4, blue: 4}), Noble({blue: 4, green: 4}), Noble({green: 4, red: 4}),
            Noble({red: 4, black: 4}), Noble({white: 4, black: 4}), Noble({white: 3, blue: 3, green: 3}),
            Noble({blue: 3, green: 3, red: 3}), Noble({green: 3, red: 3, black: 3}),
            Noble({white: 3, red: 3, black: 3}), Noble({white: 3, blue: 3, black: 3})]


def pick_nobles():
    print('Pick 3 Nobles:')
    ns = all_nobles()
    for idx, n in enumerate(ns):
        print('%s: %s' % (idx, n))
    n1 = int(input("First Noble: "))
    n2 = int(input("Second Noble: "))
    n3 = int(input("Third Noble: ")) #todo allow go back, validate input (int and valid index)
    return ns[n1], ns[n2], ns[n3]


if __name__ == '__main__':
    nobles = pick_nobles()
    print(nobles)
    #l1_cards = pick_l1_cards()
    #l2_cards = pick_l2_cards()
    #l3_cards = pick_l3_cards

    #game = Game(Board(l1_cards, l2_cards, l3_cards, nobles))





    # print available nobles
    # say, pick Three
