import os
import random

def read_input(filename):
    try:
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            array = list(map(int, file.readline().strip().split()))
        return n, array
    except FileNotFoundError:
        print(f"File not found: {filename}")
        raise
    except ValueError:
        print("Error reading input data. Please check the format of input.txt.")
        raise

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

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output1_file_path = os.path.join(current_dir, '..', 'txtf', 'output1.txt')
    output2_file_path = os.path.join(current_dir, '..', 'txtf', 'output2.txt')

    try:
        n, array = read_input(input_file_path)

        array1 = array[:]
        array2 = array[:]

        randomized_quicksort(array1, 0, n - 1)
        write_output(output1_file_path, array1)

        randomized_quicksort_partition3(array2, 0, n - 1)
        write_output(output2_file_path, array2)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
