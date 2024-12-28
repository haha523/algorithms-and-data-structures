import os

class HashTable:
    def __init__(self):
        self.table = set()

    def add(self, x):
        self.table.add(x)

    def contains(self, x):
        return x in self.table

def read_input(file_path):
    with open(file_path, 'r') as f:
        N, X, A, B = map(int, f.readline().strip().split())
        AC, BC, AD, BD = map(int, f.readline().strip().split())
    return N, X, A, B, AC, BC, AD, BD

def write_output(file_path, X, A, B):
    with open(file_path, 'w') as f:
        f.write(f"{X} {A} {B}\n")

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    N, X, A, B, AC, BC, AD, BD = read_input(input_path)

    hash_table = HashTable()

    for _ in range(N):
        if hash_table.contains(X):
            A = (A + AC) % 1000
            B = (B + BC) % (10**15)
        else:
            hash_table.add(X)
            A = (A + AD) % 1000
            B = (B + BD) % (10**15)

        X = (X * A + B) % (10**15)

    write_output(output_path, X, A, B)

if __name__ == "__main__":
    main()
