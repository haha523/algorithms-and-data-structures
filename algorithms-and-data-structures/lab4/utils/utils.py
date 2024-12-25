import os

def read_lines_from_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def save_content_to_file(content, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def construct_output_path(task_id):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    task_folder = f'task{task_id}'
    text_folder = os.path.join(current_directory, task_folder, 'txtf')
    return os.path.join(text_folder, "output.txt")

def clear_previous_output(task_id):
    output_file_path = construct_output_path(task_id)
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.truncate(0)

def display_output(task_id):
    output_file_path = construct_output_path(task_id)
    with open(output_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"Output:\n{content}")
