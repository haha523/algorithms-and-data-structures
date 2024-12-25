import os

def swap_sort(arr):
    swaps = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swaps.append(f"Swap elements at indices {i + 1} and {j + 1}.")
                arr[i], arr[j] = arr[j], arr[i]

    swaps.append("No more swaps needed.")

    return swaps

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as infile:
        n = int(infile.readline().strip())
        arr = list(map(int, infile.readline().strip().split()))

    swaps = swap_sort(arr)

    with open(output_file_path, 'w') as outfile:
        for swap in swaps:
            outfile.write(swap + '\n')


if __name__ == '__main__':
    main()