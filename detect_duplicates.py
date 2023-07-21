import os


def display(category, duplicate_dict):
    print(category)

    for key, value in duplicate_dict.items():
        if len(value) > 1:
            print(key, value)


def duplicate_by_name(path):
    from concurrent.futures import ThreadPoolExecutor

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

    with ThreadPoolExecutor() as executor:
        executor.map(process_duplicate_by_name, subdirectories)

    category = "DUPLICATES BY NAME"
    return category, file_name_dict


############################  DUPLICATE  BY CONTENT ########################

def duplicate_by_content(path):
    import hashlib
    from concurrent.futures import ThreadPoolExecutor

    file_name_dict = {}  #### dictionary stores key->hash value of content, value-> file path
    buff_size = 64 * 1024

    #################  code snippet to get path and hash value of files with duplicate content  #################
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


######################## Till here  #############################

################### Add code to delete all duplicate files except last modified #########################

####   use os library to delete
####   use os.path.getmtime() function to get last modified date and time


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
