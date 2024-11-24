import os

def insertion_sort(arr):
    sorted_list = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(output_file_path, 'w') as output_file:
        for i in range(len(arr)):
            sorted_list.append(arr[i])
            sorted_list.sort()
            output_file.write(f'{sorted_list}\n')

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')

    with open(input_file_path, 'r') as input_file:
        data = input_file.read().split()
        numbers = list(map(int, data))

    insertion_sort(numbers)

if __name__ == "__main__":
    main()
