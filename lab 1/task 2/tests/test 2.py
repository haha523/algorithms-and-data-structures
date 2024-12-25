import unittest
import os

def insertion_sort(arr):
    sorted_list = []
    for i in range(len(arr)):
        sorted_list.append(arr[i])
        sorted_list.sort()
    return sorted_list

class TestInsertionSort(unittest.TestCase):

    def test_sorted_array(self):
        # given
        arr = [1, 2, 3, 4, 5]
        # when
        result = insertion_sort(arr)
        # then
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        # given
        arr = [5, 4, 3, 2, 1]
        # when
        result = insertion_sort(arr)
        # then
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random_array(self):
        # given
        arr = [3, 1, 4, 2, 5]
        # when
        result = insertion_sort(arr)
        # then
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_empty_array(self):
        # given
        arr = []
        # when
        result = insertion_sort(arr)
        # then
        self.assertEqual(result, [])

    def test_single_element_array(self):
        # given
        arr = [1]
        # when
        result = insertion_sort(arr)
        # then
        self.assertEqual(result, [1])

    def test_array_with_duplicates(self):
        # given
        arr = [3, 1, 2, 2, 5, 4, 3]
        # when
        result = insertion_sort(arr)
        # then
        self.assertEqual(result, [1, 2, 2, 3, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
