import random

def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))
    return n, array

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
    n, array = read_input("input.txt")

    array1 = array[:]
    array2 = array[:]

    randomized_quicksort(array1, 0, n - 1)
    write_output("output 1.txt", array1)

    randomized_quicksort_partition3(array2, 0, n - 1)
    write_output("output 2.txt", array2)

if __name__ == "__main__":
    main()
