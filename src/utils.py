# src/utils.py

import os

def get_code_files(directory: str, extensions=None):
    """
    Recursively find all code files in a directory with the given extensions.
    """
    if extensions is None:
        extensions = ['.py', '.java', '.js', '.ts']

    code_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                code_files.append(os.path.join(root, file))
    return code_files


def save_json(data, path):
    """
    Save dictionary `data` to a JSON file at `path`.
    """
    import json
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
