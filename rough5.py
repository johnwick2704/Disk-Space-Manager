import os
import time
from concurrent.futures import ThreadPoolExecutor

def identify_large_files(path, threshold):
    large_files_dict = {}

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

    return large_files_dict

start = time.time()

path_to_search = "C:/Users/"  # Replace with the actual directory path
size_threshold_kb = (1024 * 1024) / 5  # Threshold for large files in kilobytes (e.g., 1 MB)

large_files = identify_large_files(path_to_search, size_threshold_kb)

if large_files:
    print("Large files found:")
    for file_path in large_files.keys():
        size = large_files.get(file_path)
        print(f"{file_path} - Size: {size}")
else:
    print("No large files found.")

print(time.time() - start)