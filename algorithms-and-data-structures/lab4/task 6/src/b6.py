from collections import deque

class MinQueue:
    def __init__(self):
        self.queue = deque()
        self.min_queue = deque()

    def add(self, value):
        self.queue.append(value)
        while self.min_queue and self.min_queue[-1] > value:
            self.min_queue.pop()
        self.min_queue.append(value)

    def remove(self):
        if not self.queue:
            raise IndexError("remove from empty queue")  
        value = self.queue.popleft()
        if value == self.min_queue[0]:
            self.min_queue.popleft()

    def get_min(self):
        if not self.min_queue:
            raise IndexError("get_min from empty queue")  
        return self.min_queue[0]

def main():
    input_file_path = '../txtf/input.txt'
    output_file_path = '../txtf/output.txt'

    min_queue = MinQueue()
    results = []

    with open(input_file_path, 'r', encoding='utf-8') as infile:
        m = int(infile.readline().strip())
        for _ in range(m):
            command = infile.readline().strip().split()
            if command[0] == '+':
                value = int(command[1])
                min_queue.add(value)
            elif command[0] == '-':
                min_queue.remove()
            elif command[0] == '?':
                results.append(min_queue.get_min())

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for result in results:
            outfile.write(str(result) + '\n')

if __name__ == '__main__':
    main()
