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
