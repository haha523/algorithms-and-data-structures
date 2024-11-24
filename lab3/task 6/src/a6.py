import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().strip().split())
        A = list(map(int, file.readline().strip().split()))
        B = list(map(int, file.readline().strip().split()))
    return n, m, A, B

def calculate_products(A, B):
    products = []
    for a in A:
        for b in B:
            products.append(a * b)
    return products

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    n, m, A, B = read_input(input_file_path)

    products = calculate_products(A, B)

    products.sort()

    total_sum = products[0] + products[10] if len(products) > 10 else 0

    with open(output_file_path, 'w') as file:
        file.write(str(total_sum) + '\n')

if __name__ == "__main__":
    main()

