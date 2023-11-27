import unittest
import os

from src.beers import read_file_and_parse, write_file

class FileTest(unittest.TestCase):
    output_path = "tests/test_output2.txt"
    input_path = "src/input.txt"

    def setUp(self) -> None:
        if os.path.exists(FileTest.output_path):
            os.remove(FileTest.output_path)

    def tearDown(self) -> None:
        if os.path.exists(FileTest.output_path):
            os.remove(FileTest.output_path)


    def test_read_file(self):
        a = read_file_and_parse(FileTest.input_path)
        self.assertEqual(type(a), tuple)

    def test_create_and_write_file(self):
        write_file("2", FileTest.output_path, "w")
        
        with open(FileTest.output_path, "r") as file:
            self.assertEqual("2", file.read())