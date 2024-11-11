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
    n, m, A, B = read_input('input.txt')

    products = calculate_products(A, B)

    products.sort()

    total_sum = products[0] + products[10]

    with open('output.txt', 'w') as file:
        file.write(str(total_sum) + '\n')

if __name__ == "__main__":
    main()

