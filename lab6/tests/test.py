import unittest
from parameterized import parameterized

from src.KMP import KMP


def read_test_cases(filename="./tests/test_cases.txt"):
    with open(filename, "r") as file:
        lines = file.read()
        result = []
        for line in lines.split("\n"):
            string, substring, excpected, name = line.split(" : ")
            excpected = list(map(int, excpected.split(","))) if excpected else []
            result.append((name, string, substring, excpected))
        return result


class KMP_Test(unittest.TestCase):
    @parameterized.expand(read_test_cases())
    def test_case(self, name, string, substring, expected):
        self.assertEqual(KMP(string, substring), expected)
