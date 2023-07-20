import os

path = os.getcwd()

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

for key, value in file_name_dict.items():
    if len(value) > 1:
        print(key, value)
