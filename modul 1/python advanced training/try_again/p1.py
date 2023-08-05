import os

file_name = "1.txt"

current_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_directory, file_name)

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"Error occurred: {e}")
