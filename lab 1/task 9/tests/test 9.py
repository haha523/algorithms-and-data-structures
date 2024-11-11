import unittest
import os

def read_input_file(filename):
    with open(filename, 'r') as file:
        binary_numbers = file.readline().strip().split()
    return binary_numbers[0], binary_numbers[1]

def binary_addition(A, B):
    sum_binary = bin(int(A, 2) + int(B, 2))[2:]
    return sum_binary

def write_output_file(filename, result):
    with open(filename, 'w') as file:
        file.write(result)

class TestBinaryAddition(unittest.TestCase):

    def setUp(self):
        self.input_file = 'input.txt'
        self.output_file = 'output.txt'

    def tearDown(self):
        # Remove the output file after each test
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_binary_addition(self):
        # Prepare input
        with open(self.input_file, 'w') as f:
            f.write('1101 1011\n')

        # Read input
        A, B = read_input_file(self.input_file)

        # Perform addition
        result = binary_addition(A, B)

        # Write output
        write_output_file(self.output_file, result)

        # Check the output
        with open(self.output_file, 'r') as f:
            output = f.read().strip()

        self.assertEqual(output, '11000')  # Expected result

if __name__ == '__main__':
    unittest.main()
