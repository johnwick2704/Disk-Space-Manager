import os
from concurrent.futures import ThreadPoolExecutor


def display(category, duplicate_dict):
    print(category)

    for key, value in duplicate_dict.items():
        if len(value) > 1:
            print(key, value)


def duplicate_by_name(path):
    file_name_dict = {}

    def process_duplicate_by_name(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                file_name = os.path.basename(file)

                if file_name not in file_name_dict:
                    file_name_dict[file_name] = [file_path]
                else:
                    val = file_name_dict.get(file_name)
                    val.append(file_path)
                    file_name_dict[file_name] = val

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_duplicate_by_name, subdirectories)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file)

            if file_name not in file_name_dict:
                file_name_dict[file_name] = [file_path]
            else:
                val = file_name_dict.get(file_name)
                val.append(file_path)
                file_name_dict[file_name] = val
        break

    category = "DUPLICATES BY NAME"
    return category, file_name_dict


def duplicate_by_content(path):
    import hashlib

    file_name_dict = {}
    buff_size = 64 * 1024

    def process_duplicate_by_content(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                try:
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
                except OSError:
                    pass

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_duplicate_by_content, subdirectories)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            try:
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
            except OSError:
                pass
        break

    category = "DUPLICATES BY CONTENT"
    return category, file_name_dict


def delete_oldest_duplicates(duplicates):
    for key in duplicates.keys():
        if len(duplicates.get(key)) <= 1:
            continue
        val = input(f"Delete duplicates for {key}? y/n")
        if val == 'n':
            continue
        delete_list = sorted(duplicates.get(key), key=os.path.getmtime)
        for file_path in delete_list:
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
        user_input = input("Do you want to delete the oldest duplicates? (y/n): ")
        if user_input == 'y':
            print("\nDeleting oldest duplicates...")
            delete_oldest_duplicates(duplicates)
        else:
            print("Deletion canceled.")
    else:
        print("No duplicates found in the directory.")


def get_duplicate_files(path):
    menu = {'1': "Duplicate by Name", '2': "Duplicate by content", '3': "Exit"}

    while True:
        options = list(menu.keys())
        options.sort()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")
        if selection == '1':
            category, duplicate_dict = duplicate_by_name(path)
            display(category, duplicate_dict)
            delete_duplicate_files_folders(duplicate_dict)
        elif selection == '2':
            category, duplicate_dict = duplicate_by_content(path)
            display(category, duplicate_dict)
            delete_duplicate_files_folders(duplicate_dict)
        elif selection == '3':
            break
        else:
            print("Unknown Option Selected!")
