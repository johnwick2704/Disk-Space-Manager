import os
from concurrent.futures import ThreadPoolExecutor


def scan_by_file_ext(path):
    extension = input("Enter file extension. ")
    print("Location of all files of given extension : ")

    def process_scan_by_file_ext(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                file_extension = file.split('.')[-1]
                if file_extension == extension.split('.')[-1]:
                    print(os.path.join(root, file))

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_scan_by_file_ext, subdirectories)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            file_extension = file.split('.')[-1]
            if file_extension == extension.split('.')[-1]:
                print(os.path.join(root, file))
        break


def get_all_empty_files(path):
    print("Location of files with size 0 : ")

    def process_get_all_empty_files(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    if os.stat(file_path).st_size == 0:
                        print(file_path)
                except OSError:
                    pass

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_get_all_empty_files, subdirectories)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                if os.stat(file_path).st_size == 0:
                    print(file_path)
            except OSError:
                pass
        break


def get_files_created_modified_today(path):
    from datetime import date, datetime

    today = date.today()

    def process_get_files_created_modified_today(path):
        for root, _, files in os.walk(path):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).date()
                    modification_time = datetime.fromtimestamp(os.path.getmtime(file_path)).date()
                    if today in (creation_time, modification_time):
                        print(file_path)
                except OSError:
                    pass

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_get_files_created_modified_today, subdirectories)

    for root, _, files in os.walk(path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).date()
                modification_time = datetime.fromtimestamp(os.path.getmtime(file_path)).date()
                if today in (creation_time, modification_time):
                    print(file_path)
            except OSError:
                pass
        break


def get_all_files_with_name(path):
    from concurrent.futures import ThreadPoolExecutor

    name = input("Full name of file to search/scan ?")
    print(f"Location of files with name {name} : ")

    def process_get_all_files_with_name(path):
        nonlocal name

        for (root, dirs, files) in os.walk(path):
            for file in files:
                if file == name:
                    print(os.path.join(root, file))

    subdirectories = [os.path.join(path, dir) for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_get_all_files_with_name, subdirectories)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            if file == name:
                print(os.path.join(root, file))
        break


def scan_files(path):
    menu = {'1': "Scan files by extension", '2': "Scan for empty files",
            '3': "Scan for files created or modified today", '4': "Scan files with name", '5': "Exit"}

    while True:
        options = list(menu.keys())
        options.sort()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")
        if selection == '1':
            scan_by_file_ext(path)
        elif selection == '2':
            get_all_empty_files(path)
        elif selection == '3':
            get_files_created_modified_today(path)
        elif selection == '4':
            get_all_files_with_name(path)
        elif selection == '5':
            break
        else:
            print("Unknown Option Selected!")
