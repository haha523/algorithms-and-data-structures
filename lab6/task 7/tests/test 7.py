import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d7 import read_input, write_output, count_beautiful_pairs

class TestGemstones(unittest.TestCase):

    def test_count_beautiful_pairs(self):
        # given
        stones = "abacaba"
        pairs = [("a", "a")]
        result = count_beautiful_pairs(len(stones), stones, pairs)
        self.assertEqual(result, 6)

        # then
        pairs = [("a", "b"), ("a", "c"), ("b", "b")]
        result = count_beautiful_pairs(len(stones), stones, pairs)
        self.assertEqual(result, 7)

    def test_read_input(self):
        # given
        test_input = "7 1\nabacaba\naa\n"
        with open('test_input.txt', 'w') as f:
            f.write(test_input)

        # when
        n, k, stones, pairs = read_input('test_input.txt')
        self.assertEqual(n, 7)
        self.assertEqual(k, 1)
        self.assertEqual(stones, "abacaba")
        self.assertEqual(pairs, [("a", "a")])

        # then
        os.remove('test_input.txt')

    def test_write_output(self):
        # given
        write_output('test_output.txt', 6)

        # when
        with open('test_output.txt', 'r') as f:
            content = f.read().strip()

        # when
        self.assertEqual(content, "6")

        # then
        os.remove('test_output.txt')

if __name__ == "__main__":
    unittest.main()
