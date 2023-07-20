import os
import datetime


def scan_by_file_ext(extension):
    path = os.getcwd()
    all_files_of_type = []

    for (root, dirs, files) in os.walk(path):
        for file in files:
            file_extension = file.split('.')[-1]
            if file_extension == extension.split('.')[-1]:
                all_files_of_type.append(os.path.join(root, file))

    print("Location of all files of given extension : ")
    for data in all_files_of_type:
        print(data)


def get_all_empty_files():
    path = os.getcwd()
    empty_files = []

    for (root, dirs, files) in os.walk(path):
        for file in files:
            if os.stat(file).st_size == 0:
                empty_files.append(os.path.join(root, file))

    print("Location of files with size 0 : ")

    for data in empty_files:
        print(data)


def get_files_created_modified_today():
    path = os.getcwd()
    today = datetime.date.today()
    files_created_modified_today = []

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            creation_time = path.datetime.fromtimestamp(os.path.getctime(file_path)).date()
            modification_time = path.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
            if today in (creation_time, modification_time):
                files_created_modified_today.append(file_path)

    for data in files_created_modified_today:
        print(data)


def scan_files():
    menu = {'1': "Scan files by extension", '2': "Scan for empty files",
            '3': "Scan for files created or modified today", '4': "Exit"}
    path = os.getcwd()

    while True:
        options = list(menu.keys())
        options.sort()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")
        if selection == '1':
            ex = input("Enter extension")
            scan_by_file_ext(ex)
        elif selection == '2':
            get_all_empty_files()
        elif selection == '3':
            get_files_created_modified_today()
        elif selection == '4':
            break
        else:
            print("Unknown Option Selected!")