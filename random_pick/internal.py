from pathlib import Path


def build_file_list(path, patterns):
    files = []
    for pattern in patterns:
        files.extend(path.glob(pattern))
    
    return files
