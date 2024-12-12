import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b3 import is_valid_bracket_sequence, process_bracket_sequences

class TestBracketSequence(unittest.TestCase):

    def setUp(self):
        # given
        self.test_dir = 'txtf'
        os.makedirs(self.test_dir, exist_ok=True)

        # when
        self.input_file = os.path.join(self.test_dir, 'input.txt')
        self.output_file = os.path.join(self.test_dir, 'output.txt')

        # then
        with open(self.input_file, 'w', encoding='utf-8') as f:
            f.write("5\n()()\n([])\n([)]\n((]]\n)(\n")

    def tearDown(self):
        # given
        if os.path.exists(self.test_dir):
            for file in os.listdir(self.test_dir):
                os.remove(os.path.join(self.test_dir, file))
            os.rmdir(self.test_dir)

    def test_is_valid_bracket_sequence(self):
        # given
        self.assertTrue(is_valid_bracket_sequence("()()"))
        self.assertTrue(is_valid_bracket_sequence("([])"))
        self.assertFalse(is_valid_bracket_sequence("([)]"))
        self.assertFalse(is_valid_bracket_sequence("((]]"))
        self.assertFalse(is_valid_bracket_sequence(")("))

    def test_process_bracket_sequences(self):
        # given
        process_bracket_sequences(self.input_file, self.output_file)

        # when
        with open(self.output_file, 'r', encoding='utf-8') as f:
            output = f.read().strip().split('\n')

        # then
        expected_output = ['YES', 'YES', 'NO', 'NO', 'NO']  
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
