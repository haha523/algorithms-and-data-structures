def insertion_sort_recursive(arr, n):
    
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key


with open('d:/Visual studio code/lab_1.py/input for b3.txt', 'r') as infile:
    data = list(map(int, infile.readline().strip().split()))

insertion_sort_recursive(data, len(data))


with open('d:/Visual studio code/lab_1.py/output for b3.txt', 'w') as outfile:
    outfile.write(' '.join(map(str, data)))
