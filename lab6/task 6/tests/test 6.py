import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d6 import is_fibonacci, read_input, write_output

class TestFibonacci(unittest.TestCase):

    def test_is_fibonacci(self):
        # given
        self.assertTrue(is_fibonacci(1))
        self.assertTrue(is_fibonacci(2))
        self.assertTrue(is_fibonacci(3))
        self.assertTrue(is_fibonacci(5))
        self.assertTrue(is_fibonacci(8))

        # when
        self.assertFalse(is_fibonacci(4))
        self.assertFalse(is_fibonacci(6))
        self.assertFalse(is_fibonacci(7))
        self.assertFalse(is_fibonacci(9))

        # then
        self.assertFalse(is_fibonacci(-1))

    def test_read_input(self):
        # given
        test_input = "3\n1\n2\n3\n"
        with open('test_input.txt', 'w') as f:
            f.write(test_input)

        # when
        result = read_input('test_input.txt')
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

        # then
        os.remove('test_input.txt')

    def test_write_output(self):
        # given
        results = ["Yes", "Yes", "Yes"]
        write_output('test_output.txt', results)

        # when
        with open('test_output.txt', 'r') as f:
            content = f.readlines()

        # when
        expected_output = ["Yes\n", "Yes\n", "Yes\n"]
        self.assertEqual(content, expected_output)

        # then
        os.remove('test_output.txt')

if __name__ == "__main__":
    unittest.main()
