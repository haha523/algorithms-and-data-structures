import os

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.p = 1000000007
        self.x = 263

    def hash_function(self, s):
        h = 0
        for i, char in enumerate(s):
            h = (h + (ord(char) * (self.x ** i)) % self.p) % self.p
        return h % self.size

    def add(self, string):
        index = self.hash_function(string)
        if string not in self.table[index]:
            self.table[index].insert(0, string)

    def delete(self, string):
        index = self.hash_function(string)
        if string in self.table[index]:
            self.table[index].remove(string)

    def find(self, string):
        index = self.hash_function(string)
        return "yes" if string in self.table[index] else "no"

    def check(self, index):
        return " ".join(self.table[index]) if self.table[index] else ""

def read_input(file_path):
    with open(file_path, 'r') as f:
        m = int(f.readline().strip())
        n = int(f.readline().strip())
        operations = [f.readline().strip() for _ in range(n)]
    return m, operations

def write_output(file_path, results):
    with open(file_path, 'w') as f:
        f.write('\n'.join(results) + '\n')

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    m, operations = read_input(input_path)
    hash_table = HashTable(m)
    results = []

    for operation in operations:
        parts = operation.split()
        cmd = parts[0]
        if cmd == 'add':
            string = parts[1]
            hash_table.add(string)
        elif cmd == 'del':
            string = parts[1]
            hash_table.delete(string)
        elif cmd == 'find':
            string = parts[1]
            results.append(hash_table.find(string))
        elif cmd == 'check':
            index = int(parts[1])
            results.append(hash_table.check(index))

    write_output(output_path, results)

if __name__ == "__main__":
    main()
