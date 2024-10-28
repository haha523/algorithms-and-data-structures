def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

def main():
    with open('d:/Visual studio code/lab_1.py/input for b6.txt', 'r') as infile:
        n = int(infile.readline().strip())
        arr = list(map(int, infile.readline().strip().split()))
    
    bubble_sort(arr)
    
    with open('d:/Visual studio code/lab_1.py/output for b6.txt', 'w') as outfile:
        outfile.write(' '.join(map(str, arr)) + '\n')

if __name__ == '__main__':
    main()