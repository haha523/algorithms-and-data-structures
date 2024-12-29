import os
import sys
import unittest
from collections import deque

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from e2 import read_input, write_output, optimal_sequence

class TestPrimitiveCalculator(unittest.TestCase):

    def test_read_input(self):
        # given
        test_input = "5\n"
        with open('test_input.txt', 'w') as f:
            f.write(test_input)

        # when
        n = read_input('test_input.txt')
        self.assertEqual(n, 5)

        # then
        os.remove('test_input.txt')

    def test_write_output(self):
        # given
        write_output('test_output.txt', 3, [1, 2, 4, 5])

        # when
        with open('test_output.txt', 'r') as f:
            content = f.read().strip().splitlines()

        # when
        self.assertEqual(content[0], "3")
        self.assertEqual(content[1], "1 2 4 5")

        # then
        os.remove('test_output.txt')

    def test_optimal_sequence(self):
        # given
        k, sequence = optimal_sequence(5)
        self.assertEqual(k, 3)
        self.assertEqual(sequence, [1, 2, 4, 5])

        # when
        k, sequence = optimal_sequence(1)
        self.assertEqual(k, 0)  # 1
        self.assertEqual(sequence, [1])

        # then
        k, sequence = optimal_sequence(96234)
        self.assertIsInstance(k, int)
        self.assertIsInstance(sequence, list)

if __name__ == "__main__":
    unittest.main()
