import os

def process_stack_commands(input_file, output_file):
    stack = []
    output = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        M = int(infile.readline().strip())

        for _ in range(M):
            command = infile.readline().strip()
            if command.startswith('+'):
                _, number = command.split()
                stack.append(int(number))
            elif command == '-':
                output.append(stack.pop())

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for value in output:
            outfile.write(f"{value}\n")

def main():
    txtf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'txtf')
    input_file_path = os.path.join( '..', 'txtf', 'input.txt')
    output_file_path = os.path.join( '..', 'txtf', 'output.txt')

    process_stack_commands(input_file_path, output_file_path)

if __name__ == "__main__":
    main()