def swap_sort(arr):
    swaps = []
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                
                swaps.append(f"Swap elements at indices {i + 1} and {j + 1}.")
                arr[i], arr[j] = arr[j], arr[i]
    
    swaps.append("No more swaps needed.")
    
    return swaps

with open('d:/Visual studio code/lab_1.py/input for b8.txt', 'r') as infile:
    n = int(infile.readline().strip())
    arr = list(map(int, infile.readline().strip().split()))

swaps = swap_sort(arr)

with open( 'd:/Visual studio code/lab_1.py/output for b8.txt', 'w') as outfile:
    for swap in swaps:
        outfile.write(swap + '\n')
        