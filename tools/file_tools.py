import os

def create_file(name, content):
    with open(name, 'w') as f:
        f.write(content)
    return f"Done: {name} created."

def list_files():
    return os.listdir('.')
