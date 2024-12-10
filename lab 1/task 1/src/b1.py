import os


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as infile:
        arr = list(map(int, infile.readline().strip().split()))

    insertion_sort(arr)

    with open(output_file_path, 'w') as outfile:
        outfile.write(' '.join(map(str, arr)))


if __name__ == "__main__":
    main()