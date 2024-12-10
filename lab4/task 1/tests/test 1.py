import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b1 import process_stack_commands

class TestProcessStackCommands(unittest.TestCase):

    def setUp(self):
        # given
        self.test_dir = 'test_txtf'
        os.makedirs(self.test_dir, exist_ok=True)

        # when
        self.input_file = os.path.join(self.test_dir, 'input.txt')
        self.output_file = os.path.join(self.test_dir, 'output.txt')

        # then
        with open(self.input_file, 'w', encoding='utf-8') as f:
            f.write("6\n+ 1\n+ 10\n-\n+ 2\n+ 1234\n-\n")

    def tearDown(self):
        # given
        if os.path.exists(self.test_dir):
            for file in os.listdir(self.test_dir):
                os.remove(os.path.join(self.test_dir, file))
            os.rmdir(self.test_dir)

    def test_process_stack_commands(self):
        # given
        process_stack_commands(self.input_file, self.output_file)

        # when
        with open(self.output_file, 'r', encoding='utf-8') as f:
            output = f.read().strip().split('\n')

        # then
        expected_output = ['10', '1234']
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()