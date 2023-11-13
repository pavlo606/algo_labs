import unittest
import os

from src.beers import min_beer_types, write_file

OUTPUT_PATH = "tests/test_output.txt"

class AlgorithmTest(unittest.TestCase):
    pass



def read_file(path="tests/test_input.txt"):
    with open(path, "r") as file:
        tests_count = int(file.readline())
        arr = []
        for _ in range(tests_count):
            line, result = file.readline().replace("\n", "").split("=")
            n, b, beers = line.split(":")
            n = int(n)
            b = int(b)
            beers = beers.split(" ")
            arr.append(((n, b, beers), int(result)))
        return arr

def test_case(beer, result, test_case_number):
    def func(self):
        test_beer = beer
        test_result = result
        actual_result = min_beer_types(*test_beer)
        self.assertEqual(test_result, actual_result)

        write_file(f"test_case_{test_case_number} {test_beer}: {actual_result}\n", OUTPUT_PATH, "a")
        
    return func

if os.path.exists(OUTPUT_PATH):
    os.remove(OUTPUT_PATH)

beers = read_file()
for i, beer in enumerate(beers):
    setattr(AlgorithmTest, f"test_case_algorithm_{i}", test_case(*beer, i))
