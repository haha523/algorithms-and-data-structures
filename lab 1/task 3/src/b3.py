import os

def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as infile:
        data = list(map(int, infile.readline().strip().split()))

    insertion_sort_recursive(data, len(data))

    with open(output_file_path, 'w') as outfile:
        outfile.write(' '.join(map(str, data)))

if __name__ == "__main__":
    main()
