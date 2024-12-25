import os

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

def read_input(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))
    return arr

def write_output(file_path, arr):
    with open(file_path, 'w') as f:
        f.write(' '.join(map(str, arr)) + '\n')

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    arr = read_input(input_path)
    heap_sort(arr)
    write_output(output_path, arr)

if __name__ == "__main__":
    main()