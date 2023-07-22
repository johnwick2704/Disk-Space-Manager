import os
from concurrent.futures import ThreadPoolExecutor


def identify_large_files(path):
    large_files_dict = {}
    threshold = int(input("Large file threshold limit in KB ? "))

    def process_directory(path):
        for root, dirs, files in os.walk(path):
            try:
                file_paths = [os.path.join(root, file) for file in files]
                for file_path in file_paths:
                    file_size = os.path.getsize(file_path) / 1024
                    if file_size >= threshold:
                        large_files_dict[file_path] = file_size
            except OSError:
                pass

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_directory, subdirectories)

    for root, dirs, files in os.walk(path):
        file_paths = [os.path.join(root, file) for file in files]
        for file_path in file_paths:
            try:
                file_size = os.path.getsize(file_path) / 1024
                if file_size >= threshold:
                    large_files_dict[file_path] = file_size
            except OSError:
                pass
        break

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
