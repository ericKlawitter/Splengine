class Picker:

    @staticmethod
    def get_valid_input(msg, max_legal, picked=set()):
        val = int(input(msg))
        if val < 0 or val > max_legal or val in picked:
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
    def pick_coins(game):
        print("Available coins: %s", game.coins)
        print("Pick up to 3 distinct coins, or two of the same color. You may only have two of the same color.")
        picked = set()



    @staticmethod
    def take_turn(game):
        choice = Picker.get_valid_input("Enter one of the following: 0: Pick Coins, 1: Reserve, 2: Buy From Board, "
                                        "3: Buy From Reserves, 4: Pass", 4)
        if choice == 0:
            coins = Picker.pick_coins(game)
        elif choice == 1:
            reserve_card(game)
        elif choice == 2:
            buy_from_board(game)
        elif choice == 3:
            buy_from_reserves(game.p1) #todo we need to verify whose turn it is
        else:
            pass
        # todo how do we want to process here? Return a new game, player, or do everything in place
