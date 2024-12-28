import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d4 import AssociativeArray

class TestAssociativeArray(unittest.TestCase):

    def setUp(self):
        # given
        self.associative_array = AssociativeArray()

    def test_put_and_get(self):
        # given
        self.associative_array.put("key1", "value1")
        self.assertEqual(self.associative_array.get("key1"), "value1")
        # then
        self.associative_array.put("key1", "value2")
        self.assertEqual(self.associative_array.get("key1"), "value2")

    def test_prev_and_next(self):
        # given
        self.associative_array.put("key1", "value1")
        # when
        self.associative_array.put("key2", "value2")
        self.associative_array.put("key3", "value3")
        # then
        self.assertEqual(self.associative_array.prev("key2"), "value1")
        self.assertEqual(self.associative_array.next("key2"), "value3")

    def test_delete(self):
        # given
        self.associative_array.put("key1", "value1")
        # when
        self.associative_array.delete("key1")
        # then
        self.assertEqual(self.associative_array.get("key1"), "<none>")

    def test_nonexistent_keys(self):
        # given
        self.assertEqual(self.associative_array.get("nonexistent"), "<none>")
        # when
        self.assertEqual(self.associative_array.prev("nonexistent"), "<none>")
        # then
        self.assertEqual(self.associative_array.next("nonexistent"), "<none>")

if __name__ == "__main__":
    unittest.main()
