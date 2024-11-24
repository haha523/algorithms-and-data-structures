import unittest

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


class TestSelectionSort(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_array(self):
        arr = [3, 1, 4, 2, 5]
        selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty_array(self):
        arr = []
        selection_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [1]
        selection_sort(arr)
        self.assertEqual(arr, [1])

    def test_array_with_duplicates(self):
        arr = [3, 1, 2, 2, 5, 4, 3]
        selection_sort(arr)
        self.assertEqual(arr, [1, 2, 2, 3, 3, 4, 5])

    def test_all_elements_same(self):
        arr = [2, 2, 2, 2]
        selection_sort(arr)
        self.assertEqual(arr, [2, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
