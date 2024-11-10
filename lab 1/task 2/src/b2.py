with open('input.txt', 'r') as input_file:
    data = input_file.read().split()
    numbers = list(map(int, data))

def insertion_sort(arr):
    sorted_list = []
    with open('output.txt', 'w') as output_file:
        for i in range(len(arr)):
            sorted_list.append(arr[i])
            sorted_list.sort()
            output_file.write(f'{sorted_list}\n')

insertion_sort(numbers)
