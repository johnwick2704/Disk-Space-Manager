import os
from concurrent.futures import ThreadPoolExecutor


def identify_large_files():
    large_files_dict = {}
    threshold = (1024 * 1024) / 5
    # path = os.getcwd().split('\\')[0] + "\\"
    path = ("C:\Program Files (x86)/")

    def process_directory(directory):
        for root, dirs, files in os.walk(directory):
            file_paths = [os.path.join(root, file) for file in files]
            for file_path in file_paths:
                file_size = os.path.getsize(file_path) / 1024
                if file_size >= threshold:
                    large_files_dict[file_path] = file_size

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor() as executor:
        executor.map(process_directory, subdirectories)

    if large_files_dict:
        print("Large files found:")
        for file_path in large_files_dict.keys():
            size = large_files_dict.get(file_path)
            print(f"{file_path} - Size: {format_bytes(size)}")
    else:
        print("No large files found.")


def format_bytes(size):
    for unit in ['KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


identify_large_files()
