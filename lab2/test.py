import unittest

from board_size import find_min_board_size

class BoardSize(unittest.TestCase):
    def setUp(self) -> None:
        self.input_values = {"N": 0, "W": 0, "H": 0}
        self.output_value = 0

    def test_one_paper(self):
        self.input_values = {"N": 1, "W": 2, "H": 3}
        self.output_value = 3
        
        self.assertEqual(find_min_board_size(**self.input_values), self.output_value)

    def test1(self):
        self.input_values = {"N": 10, "W": 2, "H": 3}
        self.output_value = 9

        self.assertEqual(find_min_board_size(**self.input_values), self.output_value)

    def test2(self):
        self.input_values = {"N": 2, "W": 1_000_000_000, "H": 999_999_999}
        self.output_value = 1_999_999_998

        self.assertEqual(find_min_board_size(**self.input_values), self.output_value)

    def test3(self):
        self.input_values = {"N": 4, "W": 1, "H": 1}
        self.output_value = 2

        self.assertEqual(find_min_board_size(**self.input_values), self.output_value)

    def test4(self):
        self.input_values = {"N": 5, "W": 3, "H": 4}
        self.output_value = 9

        self.assertEqual(find_min_board_size(**self.input_values), self.output_value)

if __name__ == "__main__":
    unittest.main()