import unittest

def count_occurrences(array, candidate):
    return sum(1 for x in array if x == candidate)

def majority_element(array, left, right):
    if left > right:
        return None

    if left == right:
        return array[left]

    mid = (left + right) // 2
    left_candidate = majority_element(array, left, mid)
    right_candidate = majority_element(array, mid + 1, right)

    if left_candidate == right_candidate:
        return left_candidate

    left_count = count_occurrences(array, left_candidate)
    right_count = count_occurrences(array, right_candidate)

    return left_candidate if left_count > right_count else right_candidate

def find_majority(n, array):
    if n == 0:
        return 0

    candidate = majority_element(array, 0, n - 1)
    if candidate is not None and count_occurrences(array, candidate) > n // 2:
        return 1
    return 0

class TestMajorityElement(unittest.TestCase):
    def test_majority_exists(self):
        arr = [1, 2, 3, 2, 2]
        self.assertEqual(find_majority(len(arr), arr), 1)

    def test_majority_not_exists(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_majority(len(arr), arr), 0)

    def test_empty_array(self):
        arr = []
        self.assertEqual(find_majority(len(arr), arr), 0)

    def test_single_element_majority(self):
        arr = [42]
        self.assertEqual(find_majority(len(arr), arr), 1)

    def test_single_element_no_majority(self):
        arr = [1, 1, 2, 2, 3]
        self.assertEqual(find_majority(len(arr), arr), 0)

    def test_multiple_occurrences(self):
        arr = [1, 1, 1, 2, 2, 2, 1]
        self.assertEqual(find_majority(len(arr), arr), 1)

if __name__ == "__main__":
    unittest.main()