import os

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class AssociativeArray:
    def __init__(self):
        self.data = {}
        self.head = None
        self.tail = None

    def put(self, key, value):
        if key in self.data:
            self.data[key].value = value
        else:
            new_node = Node(key, value)
            self.data[key] = new_node

            if self.tail:
                self.tail.next = new_node
                new_node.prev = self.tail
            else:
                self.head = new_node

            self.tail = new_node

    def get(self, key):
        if key in self.data:
            return self.data[key].value
        return "<none>"

    def delete(self, key):
        if key in self.data:
            node_to_delete = self.data[key]
            if node_to_delete.prev:
                node_to_delete.prev.next = node_to_delete.next
            if node_to_delete.next:
                node_to_delete.next.prev = node_to_delete.prev
            if node_to_delete == self.head:
                self.head = node_to_delete.next
            if node_to_delete == self.tail:
                self.tail = node_to_delete.prev

            del self.data[key]

    def prev(self, key):
        if key in self.data:
            node = self.data[key].prev
            if node:
                return node.value
        return "<none>"

    def next(self, key):
        if key in self.data:
            node = self.data[key].next
            if node:
                return node.value
        return "<none>"

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
    associative_array = AssociativeArray()
    results = []

    for operation in operations:
        parts = operation.split()
        cmd = parts[0]
        if cmd == 'put':
            associative_array.put(parts[1], parts[2])
        elif cmd == 'get':
            results.append(associative_array.get(parts[1]))
        elif cmd == 'prev':
            results.append(associative_array.prev(parts[1]))
        elif cmd == 'next':
            results.append(associative_array.next(parts[1]))
        elif cmd == 'delete':
            associative_array.delete(parts[1])

    write_output(output_path, results)

if __name__ == "__main__":
    main()
