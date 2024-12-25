import os

def calculate_h_index(citations):
    citations.sort(reverse=True)

    h_index = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as f:
        line = f.readline().strip()
        citations = list(map(int, line.replace(',', ' ').split()))

    h_index = calculate_h_index(citations)

    with open(output_file_path, 'w') as f:
        f.write(str(h_index) + '\n')

if __name__ == "__main__":
    main()