import unittest

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def count_inversions(arr):
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

class TestInversionCount(unittest.TestCase):
    def test_no_inversions(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(count_inversions(arr), 0)

    def test_some_inversions(self):
        arr = [2, 3, 8, 6, 1]
        self.assertEqual(count_inversions(arr), 5)

    def test_all_inversions(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(count_inversions(arr), 10)

    def test_empty_array(self):
        arr = []
        self.assertEqual(count_inversions(arr), 0)

    def test_single_element_array(self):
        arr = [42]
        self.assertEqual(count_inversions(arr), 0)

    def test_duplicates(self):
        arr = [1, 3, 2, 3, 1]
        self.assertEqual(count_inversions(arr), 4)

if __name__ == "__main__":
    unittest.main()
