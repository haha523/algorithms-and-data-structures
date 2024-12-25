import os

def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))
    return n, array

def count_occurrences(array, candidate):
    return sum(1 for x in array if x == candidate)

def majority_element(array, left, right):
    if left == right:
        return array[left]

    mid = (left + right) // 2
    left_candidate = majority_element(array, left, mid)
    right_candidate = majority_element(array, mid + 1, right)

    if left_candidate == right_candidate:
        return left_candidate

    left_count = count_occurrences(array, left_candidate)
    right_count = count_occurrences(array, right_candidate)

    return left_candidate if left_count > right_count else right_candidate

def find_majority(n, array):
    candidate = majority_element(array, 0, n - 1)
    if count_occurrences(array, candidate) > n // 2:
        return 1
    return 0

def main():
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    n, array = read_input(input_file_path)
    result = find_majority(n, array)

    with open(output_file_path, 'w') as file:
        file.write(str(result))

if __name__ == "__main__":
    main()