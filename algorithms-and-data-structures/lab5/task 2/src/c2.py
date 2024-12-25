import os

def read_tree_from_file(input_file_path):
    with open(input_file_path, 'r') as f:
        n = int(f.readline().strip())
        parents = list(map(int, f.readline().strip().split()))
    return n, parents

def build_tree(n, parents):
    tree = [[] for _ in range(n)]

    for child in range(n):
        parent = parents[child]
        if parent != -1:
            tree[parent].append(child)

    return tree

def calculate_height(tree, node, height):
    if not tree[node]:
        return height

    max_height = height
    for child in tree[node]:
        max_height = max(max_height, calculate_height(tree, child, height + 1))

    return max_height

def main():
    input_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt'))
    output_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt'))

    n, parents = read_tree_from_file(input_file_path)
    tree = build_tree(n, parents)

    root_index = parents.index(-1)

    height = calculate_height(tree, root_index, 1)

    with open(output_file_path, 'w') as f:
        f.write(str(height))

if __name__ == '__main__':
    main()