import os


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as infile:
        n = int(infile.readline().strip())
        arr = list(map(int, infile.readline().strip().split()))

    selection_sort(arr)

    with open(output_file_path, 'w') as outfile:
        outfile.write(' '.join(map(str, arr)) + '\n')


if __name__ == '__main__':
    main()