import os

def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    return stack[0]

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    with open(input_path, 'r') as input_file:
        n = int(input_file.readline().strip())
        expression = input_file.readline().strip().split()

    result = evaluate_postfix(expression)

    with open(output_path, 'w') as output_file:
        output_file.write(str(result))

if __name__ == '__main__':
    main()