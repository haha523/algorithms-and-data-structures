import os

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, number, name):
        self.contacts[number] = name

    def delete(self, number):
        if number in self.contacts:
            del self.contacts[number]

    def find(self, number):
        return self.contacts.get(number, "not found")

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
    phone_book = PhoneBook()
    results = []

    for operation in operations:
        parts = operation.split()
        cmd = parts[0]
        if cmd == 'add':
            number = parts[1]
            name = parts[2]
            phone_book.add(number, name)
        elif cmd == 'del':
            number = parts[1]
            phone_book.delete(number)
        elif cmd == 'find':
            number = parts[1]
            result = phone_book.find(number)
            results.append(result)

    write_output(output_path, results)

if __name__ == "__main__":
    main()
