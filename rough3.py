import os


def display(category, duplicate_dict):
    print(category)

    for key, value in duplicate_dict.items():
        if len(value) > 1:
            print(key, value)


def duplicate_by_content(path):
    import os
    from concurrent.futures import ThreadPoolExecutor

    file_name_dict = {}
    buff_size = 64 * 1024

    def process_duplicate_by_content(path):
        from hashlib import blake2b
        for (root, dirs, files) in os.walk(path):
            for file in files:
                lst = ['/', file]
                file_path = os.path.join(root, file)
                blake = blake2b()
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

    category = "DUPLICATE BY CONTENT"

    return category, file_name_dict


path = os.getcwd()
category, duplicate_dict = duplicate_by_content(path)
display(category, duplicate_dict)
