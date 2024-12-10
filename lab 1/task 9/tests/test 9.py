import unittest
import os

def read_input_file(filename):
    #given
    with open(filename, 'r') as file:
        binary_numbers = file.readline().strip().split()
    # then
    return binary_numbers[0], binary_numbers[1]

def binary_addition(A, B):
    # given
    sum_binary = bin(int(A, 2) + int(B, 2))[2:]
    # then
    return sum_binary

def write_output_file(filename, result):
    # given
    with open(filename, 'w') as file:
        file.write(result)

class TestBinaryAddition(unittest.TestCase):

    def setUp(self):
        # given
        self.input_file = 'input.txt'
        self.output_file = 'output.txt'

    def tearDown(self):
        # given
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_binary_addition(self):
        # given
        with open(self.input_file, 'w') as f:
            f.write('1101 1011\n')

        A, B = read_input_file(self.input_file)

        result = binary_addition(A, B)

        write_output_file(self.output_file, result)

        # when
        with open(self.output_file, 'r') as f:
            output = f.read().strip()

        # then
        self.assertEqual(output, '11000')  # Expected result

if __name__ == '__main__':
    unittest.main()
