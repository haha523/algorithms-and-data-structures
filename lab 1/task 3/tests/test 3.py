import unittest


def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key


class TestInsertionSortRecursive(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        insertion_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        insertion_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_array(self):
        arr = [3, 1, 4, 2, 5]
        insertion_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty_array(self):
        arr = []
        insertion_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [1]
        insertion_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [1])

    def test_array_with_duplicates(self):
        arr = [3, 1, 2, 2, 5, 4, 3]
        insertion_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [1, 2, 2, 3, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
