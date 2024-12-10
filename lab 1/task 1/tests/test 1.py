import unittest

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


class TestInsertionSort(unittest.TestCase):

    def test_sorted_array(self):
        # given
        arr = [1, 2, 3, 4, 5]

        # when
        insertion_sort(arr)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        # given
        arr = [5, 4, 3, 2, 1]

        # when
        insertion_sort(arr)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_array(self):
        # given
        arr = [3, 1, 4, 2, 5]

        # when
        insertion_sort(arr)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty_array(self):
        # given
        arr = []

        # when
        insertion_sort(arr)

        # then
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        # given
        arr = [1]
        # when
        insertion_sort(arr)
        # then
        self.assertEqual(arr, [1])

    def test_array_with_duplicates(self):
        # given
        arr = [3, 1, 2, 2, 5, 4, 3]
        # when
        insertion_sort(arr)
        # then
        self.assertEqual(arr, [1, 2, 2, 3, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
