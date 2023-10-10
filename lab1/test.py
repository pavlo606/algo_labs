import unittest
from sorting import get_smallest_subarray_to_sort

class TestSmallestSubarray(unittest.TestCase):
    def test_sorted(self):
        input_arr = [1, 2, 4, 6, 7, 10, 20]
        expected = (-1, -1)
        self.assertEqual(get_smallest_subarray_to_sort(input_arr), expected)

    def test_sort_all(self):
        input_arr = [19, 17, 16, 15, 9, 6, 4, 3, 1]
        expected = (0, len(input_arr) - 1)
        self.assertEqual(get_smallest_subarray_to_sort(input_arr), expected)

    def test_one_element(self):
        input_arr = [1]
        expected = (-1, -1)
        self.assertEqual(get_smallest_subarray_to_sort(input_arr), expected)

if __name__ == "__main__":
    unittest.main()
