from unittest import TestCase
from game import Player
from colors import *


class TestPlayer(TestCase):
    def test_get_total_coins(self):
        p = Player()
        p.coins = {white: 3, blue: 0, green: 2}
        self.assertEqual(p.get_total_coins(), 5)
