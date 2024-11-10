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
    input_file = 'input.txt'
    output_file = 'output.txt'

    A, B = read_input_file(input_file)
    result = binary_addition(A, B)

    write_output_file(output_file, result)
if __name__ == "__main__":
    main()
