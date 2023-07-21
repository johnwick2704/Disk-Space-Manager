import os
import time
from concurrent.futures import ThreadPoolExecutor


#
def find_large_files_and_count(path, threshold):
    large_files_dict = {}

    for (root, dirs, files) in os.walk(path, topdown=True):
        print(root)
        for file in files:
            file_path = root + "\\" + file
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path) / 1024
                if file_size >= threshold:
                    large_files_dict[file_path] = file_size

    if large_files_dict:
        print("Large files found:")
        for file_path in large_files_dict.keys():
            print(f"{file_path} - Size: {large_files_dict.get(file_path)}")
    else:
        print("No large files found.")


def identify_large_files(path, threshold):
    large_files_dict = {}

    def process_file(file_path):
        for (root, dirs, files) in os.walk(path, topdown=True):
            for file in files:
                file_path = root + "\\" + file
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path) / 1024
                    if file_size >= threshold:
                        large_files_dict[file_path] = file_size

    with ThreadPoolExecutor() as executor:
        for (root, dirs, files) in os.walk(path, topdown=True):
            print(root)
            executor.map(process_file, root)

    if large_files_dict:
        print("Large files found:")
        for file_path in large_files_dict.keys():
            print(f"{file_path} - Size: {large_files_dict.get(file_path)}")
    else:
        print("No large files found.")


path = 'C:/Users/'
threshold = (1024 * 1024) / 5
# start = time.time()
# identify_large_files(path, threshold)
# print(time.time() - start)

start = time.time()
find_large_files_and_count(path, threshold)
print(time.time() - start)
