import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c4 import build_min_heap

class TestMinHeap(unittest.TestCase):
    def is_min_heap(self, arr):
        n = len(arr)
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[i] > arr[left]:
                return False
            if right < n and arr[i] > arr[right]:
                return False
        return True

    def test_build_min_heap(self):
        # given
        arr = [5, 4, 3, 2, 1]
        swaps = build_min_heap(arr)
        expected_swaps = [(1, 4), (0, 1), (1, 3)]

        # when
        self.assertTrue(len(swaps) <= 4 * len(arr))

        # then
        for s in expected_swaps:
            self.assertIn(s, swaps)

        # given
        arr = [1, 2, 3, 4, 5]
        # when
        swaps = build_min_heap(arr)
        # then
        self.assertEqual(len(swaps), 0)

        # given
        arr = [3, 1, 5, 2, 4]
        # when
        swaps = build_min_heap(arr)
        # then
        self.assertTrue(self.is_min_heap(arr))

if __name__ == '__main__':
    unittest.main()
