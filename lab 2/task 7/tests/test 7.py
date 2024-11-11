import unittest
from io import StringIO
import sys


def max_subarray_kadane(arr):
    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])  # Cập nhật max_current
        if max_current > max_global:  # Cập nhật max_global
            max_global = max_current

    return max_global

class TestMaxSubarrayKadane(unittest.TestCase):

    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_subarray_kadane(arr), 15)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4]
        self.assertEqual(max_subarray_kadane(arr), -1)

    def test_mixed_numbers(self):
        arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_kadane(arr), 9)

    def test_all_zeroes(self):
        arr = [0, 0, 0, 0]
        self.assertEqual(max_subarray_kadane(arr), 0)

    def test_single_element(self):
        arr = [42]
        self.assertEqual(max_subarray_kadane(arr), 42)

    def test_alternating_signs(self):
        arr = [5, -1, 2, -1, 3]
        self.assertEqual(max_subarray_kadane(arr), 8)

    def test_numbers(self):
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_kadane(arr), 6)
if __name__ == "__main__":
    unittest.main()
