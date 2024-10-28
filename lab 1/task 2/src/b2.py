with open('d:/Visual studio code/lab_1.py/input for b2.txt', 'r') as input_file:
    data = input_file.read().split()
    numbers = list(map(int, data))

def insertion_sort(arr):
    sorted_list = []
    with open('d:/Visual studio code/lab_1.py/output for b2.txt', 'w') as output_file:
        for i in range(len(arr)):
            sorted_list.append(arr[i])
            sorted_list.sort()
            output_file.write(f'{sorted_list}\n')

insertion_sort(numbers)
