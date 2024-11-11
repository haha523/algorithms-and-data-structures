import unittest
import os


def swap_sort(arr):
    swaps = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swaps.append(f"Swap elements at indices {i + 1} and {j + 1}.")
                arr[i], arr[j] = arr[j], arr[i]

    swaps.append("No more swaps needed.")

    return swaps


class TestSwapSort(unittest.TestCase):

    def setUp(self):
        self.input_file = 'input.txt'
        self.output_file = 'output.txt'

    def tearDown(self):
        # Remove the output file after each test
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_case_1(self):
        with open(self.input_file, 'w') as f:
            f.write('5\n3 1 4 2 2\n')

        with open(self.input_file, 'r') as infile:
            n = int(infile.readline().strip())
            arr = list(map(int, infile.readline().strip().split()))

        swaps = swap_sort(arr)

        with open(self.output_file, 'w') as outfile:
            for swap in swaps:
                outfile.write(swap + '\n')

        expected_output = [
            "Swap elements at indices 1 and 2.",
            "Swap elements at indices 2 and 4.",
            "Swap elements at indices 3 and 4.",
            "Swap elements at indices 3 and 5.",
            "Swap elements at indices 4 and 5.",
            "No more swaps needed."
        ]

        with open(self.output_file, 'r') as f:
            result = [line.strip() for line in f.readlines()]

        self.assertEqual(result, expected_output)

    def test_case_2(self):
        with open(self.input_file, 'w') as f:
            f.write('4\n4 3 2 1\n')

        with open(self.input_file, 'r') as infile:
            n = int(infile.readline().strip())
            arr = list(map(int, infile.readline().strip().split()))

        swaps = swap_sort(arr)

        with open(self.output_file, 'w') as outfile:
            for swap in swaps:
                outfile.write(swap + '\n')

        expected_output = [
            "Swap elements at indices 1 and 2.",
            "Swap elements at indices 1 and 3.",
            "Swap elements at indices 1 and 4.",
            "Swap elements at indices 2 and 3.",
            "Swap elements at indices 2 and 4.",
            "Swap elements at indices 3 and 4.",
            "No more swaps needed."
        ]

        with open(self.output_file, 'r') as f:
            result = [line.strip() for line in f.readlines()]

        self.assertEqual(result, expected_output)

    def test_case_3(self):
        with open(self.input_file, 'w') as f:
            f.write('3\n1 1 1\n')

        with open(self.input_file, 'r') as infile:
            n = int(infile.readline().strip())
            arr = list(map(int, infile.readline().strip().split()))

        swaps = swap_sort(arr)

        with open(self.output_file, 'w') as outfile:
            for swap in swaps:
                outfile.write(swap + '\n')

        expected_output = [
            "No more swaps needed."
        ]

        with open(self.output_file, 'r') as f:
            result = [line.strip() for line in f.readlines()]

        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
