import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c1 import is_min_heap

class TestMinHeap(unittest.TestCase):

    def test_min_heap(self):
        # given
        self.assertEqual(is_min_heap([1, 0, 1, 2, 0]), "NO")
        self.assertEqual(is_min_heap([1, 3, 2, 5, 4]), "YES")

        # when
        self.assertEqual(is_min_heap([1]), "YES")

        # then
        self.assertEqual(is_min_heap([1, 2, 3, 4, 5]), "YES")
        self.assertEqual(is_min_heap([5, 4, 3, 2, 1]), "NO")
        self.assertEqual(is_min_heap([1, 1, 1, 1, 1]), "YES")
        self.assertEqual(is_min_heap([2, 1, 2, 1, 2]), "NO")

if __name__ == '__main__':
    unittest.main()