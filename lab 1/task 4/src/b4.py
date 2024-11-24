import os

def linear_search(arr, v):
    indices = [i for i, x in enumerate(arr) if x == v]

    if len(indices) > 0:
        return f"{len(indices)}: " + ', '.join(map(str, indices))
    else:
        return "-1"

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as file:
        arr = list(map(int, file.readline().split()))
        v = int(file.readline().strip())

    result = linear_search(arr, v)

    with open(output_file_path, 'w') as file:
        file.write(result)


if __name__ == "__main__":
    main()