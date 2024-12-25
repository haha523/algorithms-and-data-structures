import os
import unittest
import sys
from collections import deque

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b7 import max_in_sliding_window

class TestMaxInSlidingWindow(unittest.TestCase):

    def test_basic_cases(self):
        # given
        self.assertEqual(max_in_sliding_window(8, [2, 7, 3, 1, 5, 2, 6, 2], 4), [7, 7, 5, 6, 6])
        self.assertEqual(max_in_sliding_window(8, [1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(max_in_sliding_window(1, [1], 1), [1])
        self.assertEqual(max_in_sliding_window(5, [1, 2, 3, 4, 5], 2), [2, 3, 4, 5])

    def test_edge_cases(self):
        # given
        self.assertEqual(max_in_sliding_window(5, [5, 5, 5, 5, 5], 5), [5])
        self.assertEqual(max_in_sliding_window(3, [1, 2, 3], 1), [1, 2, 3])

    def test_large_input(self):
        # given
        large_input = list(range(100000))

        # when
        expected_output = [i + 999 for i in range(99001)]

        # then
        self.assertEqual(max_in_sliding_window(100000, large_input, 1000), expected_output)

if __name__ == '__main__':
    unittest.main()