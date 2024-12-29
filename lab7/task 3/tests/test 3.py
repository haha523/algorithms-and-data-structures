import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from e3 import read_input, write_output, edit_distance

class TestEditDistance(unittest.TestCase):

    def test_edit_distance(self):
        # given
        self.assertEqual(edit_distance("ab", "ab"), 0)
        # when
        self.assertEqual(edit_distance("short", "ports"), 3)
        self.assertEqual(edit_distance("editing", "distance"), 5)
        # then
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        self.assertEqual(edit_distance("flaw", "lawn"), 2)

    def test_read_input(self):
        # given
        with open('../txtf/input.txt', 'w') as f:
            f.write("short\nports")

        # when
        str1, str2 = read_input('../txtf/input.txt')

        # then
        self.assertEqual(str1, "short")
        self.assertEqual(str2, "ports")

    def test_write_output(self):
        # given
        write_output('../txtf/output.txt', 3)
        # when
        with open('../txtf/output.txt', 'r') as f:
            output = f.read().strip()
        # then
        self.assertEqual(output, '3')

if __name__ == '__main__':
    unittest.main()
