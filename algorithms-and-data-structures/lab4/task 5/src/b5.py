class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            if value == self.max_stack[-1]:
                self.max_stack.pop()

    def max(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None


def main():
    input_file_path = '../txtf/input.txt'
    output_file_path = '../txtf/output.txt'

    max_stack = MaxStack()
    results = []

    with open(input_file_path, 'r', encoding='utf-8') as infile:
        n = int(infile.readline().strip())
        for _ in range(n):
            command = infile.readline().strip().split()
            if command[0] == 'push':
                value = int(command[1])
                max_stack.push(value)
            elif command[0] == 'pop':
                max_stack.pop()
            elif command[0] == 'max':
                results.append(max_stack.max())

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for result in results:
            outfile.write(str(result) + '\n')


if __name__ == '__main__':
    main()