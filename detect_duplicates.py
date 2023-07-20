import hashlib
import os


def display(category, duplicate_dict):
    print(category)

    for key, value in duplicate_dict.items():
        if len(value) > 1:
            print(key, value)


def duplicate_by_name(path):
    file_name_dict = {}

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

    category = "DUPLICATES BY NAME"
    return category, file_name_dict


def duplicate_by_content(path):
    file_name_dict = {}
    buff_size = 64 * 1024

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

    category = "DUPLICATE BY CONTENT"

    return category, file_name_dict


def get_duplicate_files():
    menu = {'1': "Duplicate by Name", '2': "Duplicate by content", '3': "Exit"}
    path = os.getcwd()

    while True:
        options = list(menu.keys())
        options.sort()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")
        if selection == '1':
            category, duplicate_dict = duplicate_by_name(path)
            display(category, duplicate_dict)
        elif selection == '2':
            category, duplicate_dict = duplicate_by_content(path)
            display(category, duplicate_dict)
        elif selection == '3':
            break
        else:
            print("Unknown Option Selected!")
