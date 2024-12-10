import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b5 import MaxStack

class TestMaxStack(unittest.TestCase):

    def setUp(self):
        self.max_stack = MaxStack()

    def test_push_and_max(self):
        # given
        self.max_stack.push(2)
        self.assertEqual(self.max_stack.max(), 2)

        # when
        self.max_stack.push(1)
        self.assertEqual(self.max_stack.max(), 2)

        # then
        self.max_stack.push(3)
        self.assertEqual(self.max_stack.max(), 3)

    def test_pop(self):
        # given
        self.max_stack.push(1)
        self.max_stack.push(2)
        self.max_stack.push(3)

        # when
        self.max_stack.pop()
        self.assertEqual(self.max_stack.max(), 2)

        # then
        self.max_stack.pop()
        self.assertEqual(self.max_stack.max(), 1)

    def test_multiple_max(self):
        # given
        self.max_stack.push(5)
        self.max_stack.push(3)
        self.max_stack.push(8)

        # when
        self.assertEqual(self.max_stack.max(), 8)
        self.max_stack.pop()

        # then
        self.assertEqual(self.max_stack.max(), 5)
        self.max_stack.pop()
        self.assertEqual(self.max_stack.max(), 5)

if __name__ == '__main__':
    unittest.main()