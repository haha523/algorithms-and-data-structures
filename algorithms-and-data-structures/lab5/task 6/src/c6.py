import heapq
import os

class PriorityQueue:
    def __init__(self):
        self.elements = []
        self.entry_finder = {}
        self.REMOVED = '<removed>'
        self.counter = 0

    def add(self, x):
        if x in self.entry_finder:
            self.remove(x)
        entry = [x, self.counter]
        self.entry_finder[x] = entry
        heapq.heappush(self.elements, entry)
        self.counter += 1

    def remove(self, x):
        entry = self.entry_finder.pop(x)
        entry[-1] = self.REMOVED

    def pop(self):
        while self.elements:
            x, count = heapq.heappop(self.elements)
            if count != self.REMOVED:
                del self.entry_finder[x]
                return x
        return None

def process_operations(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    pq = PriorityQueue()
    results = []

    with open(input_path, 'r') as f:
        n = int(f.readline().strip())
        operations = f.readlines()

    for i, operation in enumerate(operations):
        parts = operation.strip().split()
        cmd = parts[0]

        if cmd == 'A':
            x = int(parts[1])
            pq.add(x)
        elif cmd == 'X':
            min_elem = pq.pop()
            if min_elem is None:
                results.append('*')
            else:
                results.append(str(min_elem))
        elif cmd == 'D':
            idx = int(parts[1]) - 1
            new_value = int(parts[2])

            old_value = int(operations[idx].strip().split()[1])
            pq.remove(old_value)
            pq.add(new_value)

    with open(output_path, 'w') as f:
        f.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    process_operations()