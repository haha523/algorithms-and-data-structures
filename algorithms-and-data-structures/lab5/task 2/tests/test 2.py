import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c2 import read_tree_from_file, build_tree, calculate_height

class TestTreeHeight(unittest.TestCase):

    def setUp(self):
        # given
        self.test_input_file = 'test_input.txt'
        self.test_output_file = 'test_output.txt'
        # then
        with open(self.test_input_file, 'w') as f:
            f.write('5\n4 -1 4 1 1\n')

    def tearDown(self):
        # given
        if os.path.exists(self.test_input_file):
            os.remove(self.test_input_file)
        # then
        if os.path.exists(self.test_output_file):
            os.remove(self.test_output_file)

    def test_read_tree_from_file(self):
        # given
        n, parents = read_tree_from_file(self.test_input_file)
        # when
        self.assertEqual(n, 5)
        # then
        self.assertEqual(parents, [4, -1, 4, 1, 1])

    def test_build_tree(self):
        # given
        n, parents = read_tree_from_file(self.test_input_file)
        # when
        tree = build_tree(n, parents)
        expected_tree = [
            [],
            [3, 4],
            [],
            [],
            [0, 2]
        ]
        # then
        self.assertEqual(tree, expected_tree)

    def test_calculate_height(self):
        # given
        n, parents = read_tree_from_file(self.test_input_file)
        # when
        tree = build_tree(n, parents)
        root_index = parents.index(-1)
        height = calculate_height(tree, root_index, 1)
        # then
        self.assertEqual(height, 3)

if __name__ == '__main__':
    unittest.main()