import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d1 import SimpleSet, read_input, write_output

class TestSimpleSet(unittest.TestCase):

    def test_operations(self):
        # given
        input_data = "8\nA 2\nA 5\nA 3\n? 2\n? 4\nA 2\nD 2\n? 2\n"
        expected_output = "Y\nN\nN\n"

        # when
        with open(os.path.join('..', 'txtf', 'input.txt'), 'w') as f:
            f.write(input_data)

        # when
        operations = read_input(os.path.join('..', 'txtf', 'input.txt'))

        # when
        simple_set = SimpleSet()
        results = []

        # when
        for operation in operations:
            parts = operation.split()
            cmd = parts[0]
            if cmd == 'A':
                x = int(parts[1])
                simple_set.add(x)
            elif cmd == 'D':
                x = int(parts[1])
                simple_set.remove(x)
            elif cmd == '?':
                x = int(parts[1])
                if simple_set.exists(x):
                    results.append('Y')
                else:
                    results.append('N')

        # when
        write_output(os.path.join('..', 'txtf', 'output.txt'), results)

        # when
        with open(os.path.join('..', 'txtf', 'output.txt'), 'r') as f:
            result = f.read()

        # then
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
