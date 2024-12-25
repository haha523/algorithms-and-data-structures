import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c6 import process_operations

class TestPriorityQueue(unittest.TestCase):

    def test_operations(self):
        # given
        input_data = "8\nA 3\nA 4\nA 2\nX\nD 2 1\nX\nX\nX\n"
        expected_output = "2\n1\n3\n*\n"

        # when
        with open(os.path.join('..', 'txtf', 'input.txt'), 'w') as f:
            f.write(input_data)

        # when
        process_operations()

        # when
        with open(os.path.join('..', 'txtf', 'output.txt'), 'r') as f:
            result = f.read()

        # then
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
