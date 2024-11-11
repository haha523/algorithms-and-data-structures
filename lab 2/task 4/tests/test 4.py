import unittest

def binary_search_first_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            result = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result


class TestBinarySearch(unittest.TestCase):
    def test_element_found(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search_first_occurrence(arr, 3), 2)

    def test_element_not_found(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search_first_occurrence(arr, 6), -1)

    def test_first_element(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search_first_occurrence(arr, 1), 0)

    def test_last_element(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search_first_occurrence(arr, 5), 4)

    def test_empty_array(self):
        arr = []
        self.assertEqual(binary_search_first_occurrence(arr, 1), -1)

    def test_single_element_found(self):
        arr = [42]
        self.assertEqual(binary_search_first_occurrence(arr, 42), 0)

    def test_single_element_not_found(self):
        arr = [42]
        self.assertEqual(binary_search_first_occurrence(arr, 0), -1)

    def test_multiple_occurrences(self):
        arr = [1, 2, 2, 2, 3]
        self.assertEqual(binary_search_first_occurrence(arr, 2), 1)

if __name__ == '__main__':
    unittest.main()
