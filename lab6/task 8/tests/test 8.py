import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d8 import read_input, write_output, HashTable

class TestHashTable(unittest.TestCase):

    def test_add_and_contains(self):
        # given
        hash_table = HashTable()
        self.assertFalse(hash_table.contains(5))

        # when
        hash_table.add(5)
        self.assertTrue(hash_table.contains(5))

        # then
        hash_table.add(10)
        self.assertTrue(hash_table.contains(10))
        self.assertFalse(hash_table.contains(15))

    def test_read_input(self):
        # given
        test_input = "4 0 0 0\n1 1 0 0\n"
        with open('test_input.txt', 'w') as f:
            f.write(test_input)

        # when
        N, X, A, B, AC, BC, AD, BD = read_input('test_input.txt')
        self.assertEqual(N, 4)
        self.assertEqual(X, 0)
        self.assertEqual(A, 0)
        self.assertEqual(B, 0)
        self.assertEqual(AC, 1)
        self.assertEqual(BC, 1)
        self.assertEqual(AD, 0)
        self.assertEqual(BD, 0)

        # then
        os.remove('test_input.txt')

    def test_write_output(self):
        # given
        write_output('test_output.txt', 3, 1, 1)

        # when
        with open('test_output.txt', 'r') as f:
            content = f.read().strip()

        # when
        self.assertEqual(content, "3 1 1")

        # then
        os.remove('test_output.txt')

if __name__ == "__main__":
    unittest.main()
