from unittest import TestCase, mock
from picker import SetupPicker
from board import Noble
from colors import *

nobles = [Noble({white: 4, blue: 4}), Noble({blue: 4, green: 4}), Noble({green: 4, red: 4}),
          Noble({red: 4, black: 4}), Noble({white: 4, black: 4}), Noble({white: 3, blue: 3, green: 3}),
          Noble({blue: 3, green: 3, red: 3}), Noble({green: 3, red: 3, black: 3}),
          Noble({white: 3, red: 3, black: 3}), Noble({white: 3, blue: 3, black: 3})]  # TODO move this to a shared file


class TestSetupPicker(TestCase):

    @mock.patch("builtins.input")
    def test_valid_input(self, mock_input):
        mock_input.side_effect = [7, 5, 0]
        picker = SetupPicker(nobles, 3)
        self.assertEqual([nobles[7], nobles[5], nobles[0]], picker.pick())

    @mock.patch("builtins.input", return_value="asdf")
    def test_nonnumeric_input(self, input):
        picker = SetupPicker(nobles, 3)
        with self.assertRaises(ValueError):
            picker._get_valid_input(0, set())

    @mock.patch("builtins.input")
    def test_duplicate_input(self, input):
        picked = {4, 1}
        picker = SetupPicker(nobles, 3)
        with self.assertRaises(ValueError):
            picker._get_valid_input(4, picked)

    @mock.patch("builtins.input", return_value=-3)
    def test_less_than_0_input(self, input):
        picker = SetupPicker(nobles, 1)
        with self.assertRaises(ValueError):
            picker._get_valid_input(1, set())

    @mock.patch("builtins.input", return_value=51)
    def test_greater_than_len(self, input):
        picker = SetupPicker(nobles, 1)
        with self.assertRaises(ValueError):
            picker._get_valid_input(1, set())

    @mock.patch("builtins.input", return_value=3.7)
    def test_decimal_input(self, input):
        picker = SetupPicker(nobles, 1)
        self.assertEqual(3, picker._get_valid_input(1, set()))

    @mock.patch("builtins.input")
    def test_some_invalid_input(self, inp):
        inp.side_effect = [1, 3, "asdf", 789, 8]
        picker = SetupPicker(nobles, 3)
        self.assertEqual([nobles[1], nobles[3], nobles[8]], picker.pick())
