def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

with open('d:/Visual studio code/lab_1.py/input for b1.txt', 'r') as infile:
    arr = list(map(int, infile.readline().strip().split()))

insertion_sort(arr)

with open('d:/Visual studio code/lab_1.py/output for b1.txt', 'w') as outfile:
        outfile.write(' '.join(map(str, arr)))
