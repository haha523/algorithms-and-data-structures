import os

def is_valid_bracket_sequence(sequence):
    stack = []
    bracket_map = {')': '(', ']': '['}

    for char in sequence:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return not stack

def process_bracket_sequences(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        N = int(infile.readline().strip())
        results = []

        for _ in range(N):
            sequence = infile.readline().strip()
            if is_valid_bracket_sequence(sequence):
                results.append("YES")
            else:
                results.append("NO")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for result in results:
            outfile.write(result + "\n")

def main():
    input_file_path = os.path.join('..', 'txtf', 'input.txt')
    output_file_path = os.path.join('..', 'txtf', 'output.txt')

    process_bracket_sequences(input_file_path, output_file_path)

if __name__ == "__main__":
    main()