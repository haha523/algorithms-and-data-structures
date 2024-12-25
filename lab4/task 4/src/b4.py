import os

def check_brackets(sequence):
    stack = []
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for index, char in enumerate(sequence):
        if char in bracket_map.values():
            stack.append((char, index + 1))
        elif char in bracket_map.keys():
            if not stack:
                return index + 1
            top_char, top_index = stack.pop()
            if top_char != bracket_map[char]:
                return index + 1

    if stack:
        return stack[-1][1]

    return "Success"


def main():
    input_file_path = os.path.join('..', 'txtf', 'input.txt')
    output_file_path = os.path.join('..', 'txtf', 'output.txt')

    results = []

    with open(input_file_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            sequence = line.strip()
            result = check_brackets(sequence)
            results.append(str(result))

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join(results) + "\n")

if __name__ == '__main__':
    main()