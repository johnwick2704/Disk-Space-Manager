import os


def remove_empty_files():
    path = os.getcwd()
    empty_files = []

    for (root, dirs, files) in os.walk(path):
        for file in files:
            if os.stat(file).st_size == 0:
                empty_files.append(os.path.join(root, file))

    for file in empty_files:
        os.remove(file)


def delete_large_files():
    large_files_list = []
    threshold = 1
    path = os.getcwd()

    for (root, dirs, files) in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path) / 1024
                if file_size >= threshold:
                    large_files_list.append(file_path)

    for file in large_files_list:
        os.remove(file)


def delete_n_days_old_file(n):
    import datetime

    path = os.getcwd()
    today = datetime.date.today()
    print(today)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
            if (today - modification_time) >= datetime.timedelta(days=n):
                os.remove(file_path)


def delete_files_with_same_content():
    import hashlib
    import os
    from concurrent.futures import ThreadPoolExecutor

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




def delete():
    menu = {'1': "Delete Empty Files", '2': "Delete large files", '3': "Delete n days old files", '4': "Exit"}

    while True:
        options = list(menu.keys())
        options.sort()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")
        if selection == '1':
            remove_empty_files()
        elif selection == '2':
            delete_large_files()
        elif selection == '3':
            days = input("Number of days: ")
            delete_n_days_old_file(days)
        elif selection == '5':
            delete_files_with_same_content()
        elif selection == '4':
            break
        else:
            print("Unknown Option Selected!")