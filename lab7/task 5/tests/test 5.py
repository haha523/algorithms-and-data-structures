import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from e5 import lcs_length

class TestLCS(unittest.TestCase):

    def test_lcs_length(self):
        # given
        self.assertEqual(lcs_length([1, 2, 3], [2, 1, 3], [1, 3, 5]), 2)
        self.assertEqual(lcs_length([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]), 3)
        # when
        self.assertEqual(lcs_length([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)
        self.assertEqual(lcs_length([1, 1, 1], [1, 1, 1], [1, 1, 1]), 3)
        # then
        self.assertEqual(lcs_length([], [], []), 0)

if __name__ == '__main__':
    unittest.main()
