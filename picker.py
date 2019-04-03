class SetupPicker:  # TODO implement some go back functionality
    def __init__(self, items, number):
        self.items = items
        self.number = number

    def _get_valid_input(self, num, picked):
        inp = input("Item %s: " % num)
        val = int(inp)
        if val < 0 or val >= len(self.items) or val in picked:
            raise ValueError
        else:
            return val

    def pick(self):
        picked = set()
        print("Pick %s items: " % self.number)
        for idx, n in enumerate(self.items):
            print("%s: %s" % (idx, n))
        game_list = []

        def get_single(num):
            try:
                picked_idx = self._get_valid_input(num, picked)
            except ValueError:
                print("Invalid Input. Try again.\n")
                return get_single(num)
            else:
                return picked_idx
        i = 0
        while i < self.number:
            val = get_single(i)
            picked.add(val)
            game_list.append(self.items[val])
            i += 1
        return game_list
