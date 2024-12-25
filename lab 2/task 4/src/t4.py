import os


def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    # Check if input file exists
    if not os.path.exists(input_file_path):
        print(f"File does not exist: {input_file_path}")
        return

    with open(input_file_path, 'r') as file:
        n = int(file.readline().strip())
        a = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())
        b = list(map(int, file.readline().strip().split()))

    result = []
    for number in b:
        index = binary_search(a, number)
        result.append(index)

    with open(output_file_path, 'w') as file:
        file.write(' '.join(map(str, result)) + '\n')


if __name__ == '__main__':
    main()
