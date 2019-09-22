from colors import *
class Picker:

    @staticmethod
    def get_valid_input(msg, max_legal, picked=set(), min_value=0):
        val = int(input(msg))
        if val < min_value or val > max_legal or val in picked:
            raise ValueError
        else:
            return val

    @staticmethod
    def get_single(msg, max_legal, picked):
        try:
            picked_idx = Picker.get_valid_input(msg, max_legal, picked)
        except ValueError:
            print("Invalid Input. Try again.\n")
            return Picker.get_single(msg, max_legal, picked)
        else:
            print("Successfully added.")
            return picked_idx

    @staticmethod
    def setup_board(items, num):
        picked = set()
        print("Pick %s items: " % num)
        for idx, n in enumerate(items):
            print("%s: %s" % (idx, n))
        game_list = []

        while num > 0:
            val = Picker.get_single("Enter Card Index: ", len(items), picked)
            picked.add(val)
            game_list.append(items[val])
            num -= 1
        return game_list

    @staticmethod
    def pick_coins(game, player_up):
        print("Pick up to 3 distinct coins, or two of the same color. You may only have two of the same color.\n"
              "Press q to stop picking.")
        picked = []
        inp = input(Picker.print_coins(game.board.coins))
        while inp.lower() != "q" and (len(picked) < 3 or len(picked) == 2 and picked[0] == picked[1]):
            if 1: #valid input
                print("here")#doSomething
            else:
                print("here")#x = 1#PromptAgain
        #add coins to the player
        if player_up.total_coins() > 10:
            remove_coins(player_up)
        print(player_up.coins)

    @staticmethod
    def _remove_coins(player):
        while player.total_coins() > 10:
            try:
                inp = Picker.get_valid_input("Max coins is 10, select coins to remove: %s" %
                                             Picker.print_coins(player.coins), 6, min_value=1)
                if Color(inp) in player.coins and player.coins[Color(inp)] > 0:
                    player.coins[Color(inp)] -= 1
            except ValueError:
                print("Invalid input, enter a valid index")

    @staticmethod #todo should this go in a more general class?
    def print_coins(coins):
        s = ""
        for color, amount in coins.items():
            s += "%d: %s: %d\n" % (color.value, color, amount)
        return s

    @staticmethod
    def take_turn(game, player_up):
        choice = Picker.get_valid_input("Enter one of the following: 0: Pick Coins, 1: Reserve, 2: Buy From Board, "
                                        "3: Buy From Reserves, 4: Pass", 4)
        if choice == 0:
            Picker.pick_coins(game, player_up)
        elif choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass #todo we need to verify whose turn it is
        else:
            pass
        return game #todo modify game || create new one
