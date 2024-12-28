import os

def is_fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def read_input(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        queries = [int(f.readline().strip()) for _ in range(n)]
    return queries

def write_output(file_path, results):
    with open(file_path, 'w') as f:
        for result in results:
            f.write(f"{result}\n")

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    queries = read_input(input_path)
    results = []

    for query in queries:
        if is_fibonacci(query):
            results.append("Yes")
        else:
            results.append("No")

    write_output(output_path, results)

if __name__ == "__main__":
    main()
