import os
from collections import deque

def process_queue():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    queue = deque()

    with open(output_path, 'w') as output_file:
        pass

    with open(input_path, 'r') as input_file:
        n = int(input_file.readline().strip())
        for _ in range(n):
            line = input_file.readline().strip()
            if not line:
                continue

            command = line.split()
            action = command[0]

            if action == '+':
                patient_id = int(command[1])
                queue.append(patient_id)
            elif action == '*':
                patient_id = int(command[1])

                mid_index = len(queue) // 2
                if len(queue) % 2 == 0:
                    mid_index -= 1
                queue.insert(mid_index + 1, patient_id)
            elif action == '-':
                with open(output_path, 'a') as output_file:
                    output_file.write(str(queue.popleft()) + '\n')

if __name__ == '__main__':
    process_queue()