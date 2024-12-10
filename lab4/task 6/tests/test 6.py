import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b6 import MinQueue

class TestMinQueue(unittest.TestCase):

    def setUp(self):
        self.min_queue = MinQueue()

    def test_add_and_min(self):
        # given
        self.min_queue.add(5)
        self.assertEqual(self.min_queue.get_min(), 5)

        # when
        self.min_queue.add(3)
        self.assertEqual(self.min_queue.get_min(), 3)

        # when
        self.min_queue.add(4)
        self.assertEqual(self.min_queue.get_min(), 3)

        # then
        self.min_queue.add(1)
        self.assertEqual(self.min_queue.get_min(), 1)

    def test_remove(self):
        # given
        self.min_queue.add(5)
        self.min_queue.add(3)
        self.min_queue.add(1)
        self.min_queue.remove()

        # when
        self.assertEqual(self.min_queue.get_min(), 1)
        self.min_queue.remove()
        self.assertEqual(self.min_queue.get_min(), 1)
        self.min_queue.remove()

        # then
        with self.assertRaises(IndexError):
            self.min_queue.get_min()

    def test_multiple_min_queries(self):
        self.min_queue.add(10)
        self.min_queue.add(20)
        self.min_queue.add(5)
        self.assertEqual(self.min_queue.get_min(), 5)
        self.min_queue.remove()
        self.assertEqual(self.min_queue.get_min(), 5)
        self.min_queue.remove()
        self.assertEqual(self.min_queue.get_min(), 5)

    def test_empty_queue(self):
        with self.assertRaises(IndexError):
            self.min_queue.remove()
        self.min_queue.add(10)
        self.min_queue.remove()
        with self.assertRaises(IndexError):
            self.min_queue.get_min()

if __name__ == '__main__':
    unittest.main()