import unittest
import os


def process_data(input_file, output_file):
    with open(input_file, 'r') as file:
        n = int(file.readline().strip())
        savings = list(map(float, file.readline().strip().split()))

        residents = [(savings[i], i + 1) for i in range(n)]

        residents.sort()

    poorest = residents[0][1]
    richest = residents[-1][1]
    median = residents[n // 2][1]

    with open(output_file, 'w') as file:
        file.write(f"{poorest} {median} {richest}\n")


class TestProcessData(unittest.TestCase):

    def setUp(self):
        self.input_file = 'input.txt'
        self.output_file = 'output.txt'

    def tearDown(self):
        # Remove the output file after each test
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_case_1(self):
        with open(self.input_file, 'w') as f:
            f.write('5\n10.00 8.70 0.01 5.00 3.00\n')

        process_data(self.input_file, self.output_file)

        with open(self.output_file, 'r') as f:
            result = f.read().strip()

        self.assertEqual(result, '3 4 1')

    def test_case_2(self):
        with open(self.input_file, 'w') as f:
            f.write('7\n15.00 5.00 25.00 10.00 30.00 20.00 1.00\n')

        process_data(self.input_file, self.output_file)

        with open(self.output_file, 'r') as f:
            result = f.read().strip()

        self.assertEqual(result, '7 1 5')

    def test_case_3(self):
        with open(self.input_file, 'w') as f:
            f.write('3\n1.00 2.00 3.00\n')

        process_data(self.input_file, self.output_file)

        with open(self.output_file, 'r') as f:
            result = f.read().strip()

        self.assertEqual(result, '1 2 3')


if __name__ == '__main__':
    unittest.main()
