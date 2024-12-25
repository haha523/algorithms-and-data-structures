import os

def swap(arr, i, j, swaps):
    arr[i], arr[j] = arr[j], arr[i]
    swaps.append((i, j))

def heapify(arr, n, i, swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        swap(arr, i, smallest, swaps)
        heapify(arr, n, smallest, swaps)

def build_min_heap(arr):
    n = len(arr)
    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, swaps)
    return swaps

def main():
    input_file_path = os.path.join('..', 'txtf', 'input.txt')
    output_file_path = os.path.join('..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))

    swaps = build_min_heap(arr)

    with open(output_file_path, 'w') as f:
        f.write(f"{len(swaps)}\n")
        for i, j in swaps:
            f.write(f"{i} {j}\n")

if __name__ == '__main__':
    main()