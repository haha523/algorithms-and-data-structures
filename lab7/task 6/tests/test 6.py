import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from e6 import longest_increasing_subsequence

class TestLIS(unittest.TestCase):

    def test_longest_increasing_subsequence(self):
        # given
        self.assertEqual(longest_increasing_subsequence([3, 29, 5, 5, 28, 6]), (3, [3, 5, 28]))
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 21, 20, 25]), (3, [10, 22, 25]))
        # when
        self.assertEqual(longest_increasing_subsequence([3, 2, 1]), (1, [3]))
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5]), (5, [1, 2, 3, 4, 5]))
        # then
        self.assertEqual(longest_increasing_subsequence([]), (0, []))

if __name__ == '__main__':
    unittest.main()
