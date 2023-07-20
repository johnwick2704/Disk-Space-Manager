import os
import datetime


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
    path = os.getcwd()
    today = datetime.date.today()
    print(today)

    for (root, dirs, files) in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
            if (today - modification_time) >= datetime.timedelta(days= n):
                os.remove(file_path)
