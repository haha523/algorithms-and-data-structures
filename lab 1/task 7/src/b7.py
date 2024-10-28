def process_data(input_file, output_file):
    with open(input_file, 'r') as file:
        n = int(file.readline().strip())
        savings = list(map(float, file.readline().strip().split()))
    
        residents = [(savings[i], i + 1) for i in range(n)]
    
        residents.sort()
    
    poorest = residents[0][1]
    richest = residents[-1][1]
    median = residents[n // 2][1]
    
    
    with open(output_file, 'w') as file:
        file.write(f"{poorest} {median} {richest}\n")

process_data('d:/Visual studio code/lab_1.py/input for b7.txt', 'd:/Visual studio code/lab_1.py/output for b7.txt')
