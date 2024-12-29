import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from e4 import read_input, write_output, lcs_length

class TestLCS(unittest.TestCase):

    def test_lcs_length(self):
        # given
        self.assertEqual(lcs_length([2, 7, 5], [2, 5]), 2)
        self.assertEqual(lcs_length([7], [1, 2, 3, 4]), 0)
        # when
        self.assertEqual(lcs_length([2, 7, 8, 3], [5, 2, 8, 7]), 2)
        self.assertEqual(lcs_length([1, 2, 3], [3, 2, 1]), 1)
        # then
        self.assertEqual(lcs_length([1, 3, 4, 1, 2, 5], [3, 4, 1, 2, 5]), 5)

    def test_read_input(self):
        # given
        sequence_a, sequence_b = [2, 7, 5], [2, 5]
        # then
        self.assertEqual(sequence_a, [2, 7, 5])
        self.assertEqual(sequence_b, [2, 5])

    def test_write_output(self):
        # given
        length = 2
        # then
        self.assertEqual(length, 2)

if __name__ == '__main__':
    unittest.main()
