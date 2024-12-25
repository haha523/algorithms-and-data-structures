import os
from collections import deque

def process_queue_commands(input_file, output_file):
    queue = deque()
    output = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        M = int(infile.readline().strip())

        for _ in range(M):
            command = infile.readline().strip()
            if command.startswith('+'):
                _, number = command.split()
                queue.append(int(number))
            elif command == '-':
                output.append(queue.popleft())

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for value in output:
            outfile.write(f"{value}\n")

def main():
    txtf_dir = os.path.join(os.path.dirname(__file__), '..', 'txtf')
    os.makedirs(txtf_dir, exist_ok=True)

    input_file_path = os.path.join(txtf_dir, 'input.txt')
    output_file_path = os.path.join(txtf_dir, 'output.txt')

    process_queue_commands(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
