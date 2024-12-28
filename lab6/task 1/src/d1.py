import os

class SimpleSet:
    def __init__(self):
        self.data = set()

    def add(self, x):
        self.data.add(x)

    def remove(self, x):
        self.data.discard(x)

    def exists(self, x):
        return x in self.data

def read_input(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        operations = [f.readline().strip() for _ in range(n)]
    return operations

def write_output(file_path, results):
    with open(file_path, 'w') as f:
        f.write('\n'.join(results) + '\n')

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    operations = read_input(input_path)
    simple_set = SimpleSet()
    results = []

    for operation in operations:
        parts = operation.split()
        cmd = parts[0]
        if cmd == 'A':
            x = int(parts[1])
            simple_set.add(x)
        elif cmd == 'D':
            x = int(parts[1])
            simple_set.remove(x)
        elif cmd == '?':
            x = int(parts[1])
            if simple_set.exists(x):
                results.append('Y')
            else:
                results.append('N')

    write_output(output_path, results)

if __name__ == "__main__":
    main()
