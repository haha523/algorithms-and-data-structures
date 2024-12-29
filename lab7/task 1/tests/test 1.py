import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from e1 import read_input, write_output, min_coins

class TestCoinExchange(unittest.TestCase):

    def test_read_input(self):
        # given
        test_input = "2 3\n1 3 4\n"
        with open('test_input.txt', 'w') as f:
            f.write(test_input)

        # when
        money, coins = read_input('test_input.txt')
        self.assertEqual(money, 2)
        self.assertEqual(coins, [1, 3, 4])

        # then
        os.remove('test_input.txt')

    def test_min_coins(self):
        # given
        self.assertEqual(min_coins(2, [1, 3, 4]), 2)
        # when
        self.assertEqual(min_coins(6, [1, 3, 4]), 2)
        self.assertEqual(min_coins(34, [1, 3, 4]), 9)
        # then
        self.assertEqual(min_coins(7, [2, 5]), 2)

    def test_write_output(self):
        # given
        write_output('test_output.txt', 2)

        # when
        with open('test_output.txt', 'r') as f:
            content = f.read().strip()

        # when
        self.assertEqual(content, "2")

        # then
        os.remove('test_output.txt')

if __name__ == "__main__":
    unittest.main()
