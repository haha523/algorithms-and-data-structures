import os

def read_input_file(filename):
    with open(filename, 'r') as file:
        binary_numbers = file.readline().strip().split()
    return binary_numbers[0], binary_numbers[1]

def binary_addition(A, B):
    sum_binary = bin(int(A, 2) + int(B, 2))[2:]  
    return sum_binary

def write_output_file(filename, result):
    with open(filename, 'w') as file:
        file.write(result)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    A, B = read_input_file(input_file_path)
    result = binary_addition(A, B)

    write_output_file(output_file_path, result)

if __name__ == "__main__":
    main()