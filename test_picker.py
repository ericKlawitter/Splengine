from unittest import TestCase, mock
from picker import Picker
from colors import *
import test_utils


class TestPicker(TestCase):

    @mock.patch("builtins.input")
    def test_valid_input(self, mock_input):
        mock_input.side_effect = [7, 5, 0]
        self.assertEqual([test_utils.nobles[7], test_utils.nobles[5], test_utils.nobles[0]],
                         Picker.setup_board(test_utils.nobles, 3))

    @mock.patch("builtins.input", return_value="asdf")
    def test_nonnumeric_input(self, input):
        with self.assertRaises(ValueError):
            Picker.get_valid_input("", len(test_utils.nobles))

    @mock.patch("builtins.input", return_value=1)
    def test_duplicate_input(self, input):
        picked = {4, 1}
        with self.assertRaises(ValueError):
            Picker.get_valid_input("", len(test_utils.nobles), picked)

    @mock.patch("builtins.input", return_value=-1)
    def test_less_than_0_input(self, input):
        with self.assertRaises(ValueError):
            Picker.get_valid_input("", len(test_utils.nobles))

    @mock.patch("builtins.input", return_value=len(test_utils.nobles))
    def test_greater_than_len(self, input):
        with self.assertRaises(ValueError):
            Picker.get_valid_input("", len(test_utils.nobles) - 1)

    @mock.patch("builtins.input", return_value=3.7)
    def test_decimal_input(self, input):
        self.assertEqual(3, Picker.get_valid_input("", len(test_utils.nobles)))

    @mock.patch("builtins.input")
    def test_some_invalid_input(self, inp):
        inp.side_effect = [1, 3, "asdf", 789, 8]
        self.assertEqual([test_utils.nobles[1], test_utils.nobles[3], test_utils.nobles[8]],
                         Picker.setup_board(test_utils.nobles, 3))

    @mock.patch("builtins.input", return_value=0)
    def test_take_turn_0(self, input):
        picker = Picker()
        with mock.patch.object(Picker, 'pick_coins') as spy_picker:
            picker.take_turn(test_utils.game)
            spy_picker.assert_called_with(test_utils.game)

    #def test_take_turn_1(self, input):
    #    pass

    def test_pick_coins(self):
        Picker.pick_coins(test_utils.game, test_utils.player)
        self.fail("need to implement this unit test")

    def test_remove_forGenericTesting(self):
        coins = {white: 1, blue: 2, gold: 5}
        self.assertEqual(coins[Color(1)], 1)
        self.assertEqual(coins[Color(6)], 5)
