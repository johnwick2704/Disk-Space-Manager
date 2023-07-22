import os
from concurrent.futures import ThreadPoolExecutor


def remove_empty_files(path):
    empty_files = []

    def process_remove_empty_files(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    if os.stat(file_path).st_size == 0:
                        empty_files.append(os.path.join(root, file))
                except OSError:
                    pass

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_remove_empty_files, subdirectories)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                if os.stat(file_path).st_size == 0:
                    empty_files.append(os.path.join(root, file))
            except OSError:
                pass
        break

    delete_decision(empty_files)


def delete_large_files(path):
    large_files_list = []
    threshold = int(input("Enter threshold in KB. "))

    def process_delete_large_files(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    if os.path.isfile(file_path):
                        file_size = os.path.getsize(file_path) / 1024
                        if file_size >= threshold:
                            large_files_list.append(file_path)
                except OSError:
                    pass

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_delete_large_files, subdirectories)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path) / 1024
                    if file_size >= threshold:
                        large_files_list.append(file_path)
            except OSError:
                pass
        break

    delete_decision(large_files_list)


def delete_n_days_old_file(path):
    import datetime

    today = datetime.date.today()
    old_files = []
    n = int(input("Enter how many days old. "))

    def process_delete_n_days_old_file(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
                    if (today - modification_time) >= datetime.timedelta(days=n):
                        old_files.append(file_path)
                except OSError:
                    pass

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_delete_n_days_old_file, subdirectories)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
                if (today - modification_time) >= datetime.timedelta(days=n):
                    old_files.append(file_path)
            except OSError:
                pass
        break

    delete_decision(old_files)


def delete_decision(delete_list):
    if len(delete_list) > 0:
        for file in delete_list:
            dec = input(f"Delete file {file} y/n?")
            if dec == 'y':
                os.remove(file)
            else:
                continue
    else:
        print("No files to delete")


def delete(path):
    menu = {'1': "Delete Empty Files", '2': "Delete large files", '3': "Delete n days old files", '4': "Exit"}

    while True:
        options = list(menu.keys())
        options.sort()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")
        if selection == '1':
            remove_empty_files(path)
        elif selection == '2':
            delete_large_files(path)
        elif selection == '3':
            delete_n_days_old_file(path)
        elif selection == '4':
            break
        else:
            print("Unknown Option Selected!")
