import os


def max_subarray_kadane(arr):
    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])

        if max_current > max_global:
            max_global = max_current

    return max_global


def main():
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as file:
        arr = list(map(int, file.readline().split()))

    max_sum = max_subarray_kadane(arr)

    with open(output_file_path, 'w') as file:
        file.write(f"Max Subarray Sum: {max_sum}\n")


if __name__ == "__main__":
    main()
