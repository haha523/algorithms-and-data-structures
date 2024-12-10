import unittest
import random
import os

def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))
    return n, array


def write_output(filename, array):
    with open(filename, 'w') as file:
        file.write(" ".join(map(str, array)))


def randomized_partition(arr, l, r):
    pivot_index = random.randint(l, r)
    arr[l], arr[pivot_index] = arr[pivot_index], arr[l]
    pivot = arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    return i - 1


def randomized_quicksort(arr, l, r):
    if l < r:
        pivot = randomized_partition(arr, l, r)
        randomized_quicksort(arr, l, pivot - 1)
        randomized_quicksort(arr, pivot + 1, r)


def partition3(arr, l, r):
    pivot = arr[l]
    lt = l
    gt = r
    i = l + 1
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


def randomized_quicksort_partition3(arr, l, r):
    if l < r:
        lt, gt = partition3(arr, l, r)
        randomized_quicksort_partition3(arr, l, lt - 1)
        randomized_quicksort_partition3(arr, gt + 1, r)


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        # given
        self.test_data = [5, 3, 8, 1, 2, 7, 4, 6]
        self.test_file_input = 'test_input.txt'
        self.test_file_output1 = 'test_output1.txt'
        self.test_file_output2 = 'test_output2.txt'
        # when
        with open(self.test_file_input, 'w') as f:
            f.write(f"{len(self.test_data)}\n")
            f.write(" ".join(map(str, self.test_data)))

    def tearDown(self):
        # given
        for file in [self.test_file_input, self.test_file_output1, self.test_file_output2]:
            if os.path.exists(file):
                os.remove(file)

    def test_read_input(self):
        # given
        n, array = read_input(self.test_file_input)
        # when
        self.assertEqual(n, len(self.test_data))
        self.assertEqual(array, self.test_data)

    def test_write_output(self):
        # given
        write_output(self.test_file_output1, self.test_data)
        # when
        with open(self.test_file_output1, 'r') as f:
            output_data = list(map(int, f.readline().strip().split()))
        # then
        self.assertEqual(output_data, self.test_data)

    def test_randomized_quicksort(self):
        # given
        array_copy = self.test_data[:]
        # when
        randomized_quicksort(array_copy, 0, len(array_copy) - 1)
        # then
        self.assertEqual(sorted(self.test_data), array_copy)

    def test_randomized_quicksort_partition3(self):
        # given
        array_copy = self.test_data[:]
        # when
        randomized_quicksort_partition3(array_copy, 0, len(array_copy) - 1)
        # then
        self.assertEqual(sorted(self.test_data), array_copy)

if __name__ == '__main__':
    unittest.main()
