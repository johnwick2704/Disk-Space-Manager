import os


def identify_large_files():
    large_files_list = []
    threshold = 1
    path = os.getcwd()

    for(root, dirs, files) in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path) / 1024
                if file_size >= threshold:
                    large_files_list.append((file_path, file_size))

    if large_files_list:
        print("Large files found:")
        for file_path, file_size in large_files_list:
            print(f"{file_path} - Size: {format_bytes(file_size)}")
    else:
        print("No large files found.")


def format_bytes(size):
    for unit in ['KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"
