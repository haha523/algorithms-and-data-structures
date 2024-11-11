import unittest


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


class TestBubbleSort(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_array(self):
        arr = [3, 1, 4, 2, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty_array(self):
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [1]
        bubble_sort(arr)
        self.assertEqual(arr, [1])

    def test_array_with_duplicates(self):
        arr = [3, 1, 2, 2, 5, 4, 3]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 2, 3, 3, 4, 5])

    def test_all_elements_same(self):
        arr = [2, 2, 2, 2]
        bubble_sort(arr)
        self.assertEqual(arr, [2, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
