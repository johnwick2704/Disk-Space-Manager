import os
import hashlib


def get_file_hash(file_path):
    with open(file_path, 'rb') as f:
        blake2b_hash = hashlib.blake2b()
        chunk = f.read(8192)
        while chunk:
            blake2b_hash.update(chunk)
            chunk = f.read(8192)
    return blake2b_hash.hexdigest()


def find_duplicates(directory):
    hash_to_files = {}

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = get_file_hash(file_path)
            if file_hash not in hash_to_files:
                hash_to_files[file_hash] = []
            hash_to_files[file_hash].append(file_path)

    # print(hash_to_files.items())
    # hash_to_files is stored like (hash,array[file1,file2,...])
    # we go over it and store only the ones that have arrays with more than one entry in duplicates{}
    # which means only the instances where same hash has multiple files associated

    duplicates = {}
    for file_hash, file_list in hash_to_files.items():
        if len(file_list) > 1:
            duplicates[file_hash] = file_list

    return duplicates


def delete_oldest_duplicates(duplicates):
    for duplicate_group in duplicates.values():
        # sorting duplicates so that later on, leaving the last instance(latest modified),
        # the ones above it can be removed
        sorted_files = sorted(duplicate_group, key=os.path.getmtime)
        for file_path in sorted_files[:-1]:
            print(f"Duplicate: {file_path}")
            user_input = input("Do you want to delete this duplicate? (y/n): ")
            if user_input == 'y':
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"Skipped deletion for {file_path}")


def delete_duplicate_files_folders():
    dir_path = os.getcwd()
    duplicates = find_duplicates(dir_path)

    if duplicates:
        print("Found duplicates:")
        for file_list in duplicates.values():
            print("\n".join(file_list))
        user_input = input("Do you want to delete the oldest duplicates? (y/n): ")
        if user_input == 'y':
            print("\nDeleting oldest duplicates...")
            delete_oldest_duplicates(duplicates)
        else:
            print("Deletion canceled.")
    else:
        print("No duplicates found in the directory.")
