import unittest

def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

class TestMergeSort(unittest.TestCase):
    def test_sorted_array(self):
        # given
        arr = [1, 2, 3, 4, 5]

        # when
        merge_sort(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])


    def test_reverse_sorted_array(self):
        # given
        arr = [5, 4, 3, 2, 1]

        # when
        merge_sort(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])


    def test_unsorted_array(self):
        # given
        arr = [3, 1, 4, 2, 5]

        # when
        merge_sort(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty_array(self):
        # given
        arr = []

        # when
        merge_sort(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        # given
        arr = [42]

        # when
        merge_sort(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(arr, [42])

    def test_duplicates(self):
        # given
        arr = [3, 1, 2, 3, 1]

        # when
        merge_sort(arr, 0, len(arr) - 1)

        # then
        self.assertEqual(arr, [1, 1, 2, 3, 3])

if __name__ == "__main__":
    unittest.main()