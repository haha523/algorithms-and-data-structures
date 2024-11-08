def merge(arr, left, mid, right):
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0  
    k = left   

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)

def main():
    with open('d:/Visual studio code/lab_2.py/input for t1.txt', 'r') as f:
        n = int(f.readline())  
        arr = list(map(int, f.readline().split()))  

    merge_sort(arr, 0, n - 1)  

    with open('d:/Visual studio code/lab_2.py/output for t1.txt', 'w') as f:
        f.write(' '.join(map(str, arr)))  

if __name__ == "__main__":
    main()
