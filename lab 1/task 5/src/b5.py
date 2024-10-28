def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    with open('d:/Visual studio code/lab_1.py/input for b5.txt', 'r') as infile:
        n = int(infile.readline().strip())
        arr = list(map(int, infile.readline().strip().split()))
    
    selection_sort(arr)
    
    with open('d:/Visual studio code/lab_1.py/output for b5.txt', 'w') as outfile:
        outfile.write(' '.join(map(str, arr)) + '\n')

if __name__ == '__main__':
    main()