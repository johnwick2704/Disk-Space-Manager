def delete_files_with_same_content():
    import hashlib

    path = os.getcwd()
    file_name_dict = {}
    buff_size = 64 * 1024

    def process_duplicate_by_content(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                blake = hashlib.blake2b()
                with open(file_path, 'rb') as f:
                    while True:
                        data = f.read(buff_size)
                        if not data:
                            break
                        blake.update(data)

                hash_val = blake.hexdigest()

                if hash_val not in file_name_dict:
                    file_name_dict[hash_val] = [file_path]
                else:
                    val = file_name_dict.get(hash_val)
                    val.append(file_path)
                    file_name_dict[hash_val] = val

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor() as executor:
        executor.map(process_duplicate_by_content, subdirectories)


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


def delete_duplicate_files_folders(duplicates):
    if duplicates:
        print("Found duplicates:")
        for file_list in duplicates.values:
            print("\n".join(file_list))
        user_input = input("Do you want to delete the oldest duplicates? (y/n): ")
        if user_input == 'y':
            print("\nDeleting oldest duplicates...")
            delete_oldest_duplicates(duplicates)
        else:
            print("Deletion canceled.")
    else:
        print("Files not found.")