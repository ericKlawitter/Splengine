from unittest import TestCase, mock
from picker import Picker
from board import Noble
from colors import *

nobles = [Noble({white: 4, blue: 4}), Noble({blue: 4, green: 4}), Noble({green: 4, red: 4}),
          Noble({red: 4, black: 4}), Noble({white: 4, black: 4}), Noble({white: 3, blue: 3, green: 3}),
          Noble({blue: 3, green: 3, red: 3}), Noble({green: 3, red: 3, black: 3}),
          Noble({white: 3, red: 3, black: 3}), Noble({white: 3, blue: 3, black: 3})]  # TODO move this to a shared file


class TestPicker(TestCase):

    @mock.patch("builtins.input")
    def test_valid_input(self, mock_input):
        mock_input.side_effect = [7, 5, 0]
        self.assertEqual([nobles[7], nobles[5], nobles[0]], Picker.setup_board(nobles, 3))

    @mock.patch("builtins.input", return_value="asdf")
    def test_nonnumeric_input(self, input):
        with self.assertRaises(ValueError):
            Picker.get_valid_input("", len(nobles))

    @mock.patch("builtins.input") #TODO this functionality should be tested in setup method, not valid input, due to changes
    def test_duplicate_input(self, input):
        picked = {4, 1}
        with self.assertRaises(ValueError):
            Picker.get_valid_input("", len(nobles))

    @mock.patch("builtins.input", return_value=-1)
    def test_less_than_0_input(self, input):
        with self.assertRaises(ValueError):
            Picker.get_valid_input("", len(nobles))

    @mock.patch("builtins.input", return_value=len(nobles))
    def test_greater_than_len(self, input):
        with self.assertRaises(ValueError):
            Picker.get_valid_input("", len(nobles) - 1)

    @mock.patch("builtins.input", return_value=3.7)
    def test_decimal_input(self, input):
        self.assertEqual(3, Picker.get_valid_input("", len(nobles)))

    @mock.patch("builtins.input")
    def test_some_invalid_input(self, inp):
        inp.side_effect = [1, 3, "asdf", 789, 8]
        self.assertEqual([nobles[1], nobles[3], nobles[8]], Picker.setup_board(nobles, 3))
