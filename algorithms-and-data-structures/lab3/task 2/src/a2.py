import os

def generate_anti_quick_sort(n):
    result = []
    for i in range(1, n + 1, 2):
        result.append(i)
    for i in range(2, n + 1, 2):
        result.append(i)

    return result

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, "r") as file:
        n = int(file.readline().strip())

    anti_quick_sort_array = generate_anti_quick_sort(n)

    with open(output_file_path, "w") as file:
        file.write(" ".join(map(str, anti_quick_sort_array)))

if __name__ == "__main__":
    main()