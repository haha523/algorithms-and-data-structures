import utils

def read_file(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def write_file(file_path, content):

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")


def append_to_file(file_path, content):

    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

if __name__ == "__main__":
    lines = read_file('input.txt')
    print("File contents:", lines)

    write_file('output.txt', 'Here is an example of writing a file.\n')
