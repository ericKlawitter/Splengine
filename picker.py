class SetupPicker:  # TODO implement some go back functionality

    @staticmethod
    def _get_valid_input(num, picked, items):
        inp = input("Item %s: " % num)
        val = int(inp)
        if val < 0 or val >= len(items) or val in picked:
            raise ValueError
        else:
            return val

    @staticmethod
    def pick(items, num):
        picked = set()
        print("Pick %s items: " % num)
        for idx, n in enumerate(items):
            print("%s: %s" % (idx, n))
        game_list = []

        def get_single(curr_idx):
            try:
                picked_idx = SetupPicker._get_valid_input(curr_idx, picked, items)
            except ValueError:
                print("Invalid Input. Try again.\n")
                return get_single(curr_idx)
            else:
                return picked_idx
        i = 0
        while i < num:
            val = get_single(i)
            picked.add(val)
            game_list.append(items[val])
            i += 1
        return game_list


class TurnPicker:

    @staticmethod
    def input_range_idx(min, max, inp):
        val = int(inp)
        if not min <= val <= max:
            raise ValueError
        else:
            return val

    @staticmethod
    def take_turn(game):
        print("What would you like to do?", '\n')
        def get_choice():
            val = int(input("0: Pick Coins, 1: Reserve, 2: Buy From Board, 3: Buy From Reserves, 4: Pass"))
            if not 0 <= val <= 4:
                raise ValueError
            else:
                return val
        try:
            choice = get_choice()
        except ValueError:
            print("Invalid Input. Try again.\n")
        else:
            return choice
        TurnPicker.process_choice(get_choice(), game)

    @staticmethod
    def process_choice(choice, player):
        if choice == 0: #Pick Coins
            pass
        elif choice == 1: #Reserve
            pass
        elif choice == 2: #Buy FromBoard

        elif choice == 3: #Buy from reserves
            print("Pick a card to buy from reserves, or type 9 to go back")
            for card, idx in enumerate(player.reserves):
                print(idx + ": " + card, " ")

        else:
            return

        # we should be able to go back, e.g. if we change our mind
