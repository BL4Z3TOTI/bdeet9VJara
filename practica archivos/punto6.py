import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "texto.txt")

try:
    with open(file_path, 'r') as f:
        for line in f:
            print(line, end='')
except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")