import os


def find_duplicate_files_by_name(path):
    # Dictionary to store file names and corresponding paths
    file_dict = {}
    duplicates = []

    # Traverse the directory and collect file names with their paths
    for root, _, files in os.walk(path):    
        for filename in files:
            file_path = os.path.join(root, filename)
            file_name = os.path.basename(filename)

            # If the file name is not already in the dictionary, add it
            if file_name not in file_dict:
                file_dict[file_name] = [file_path]
            else:
                # If the file name is already in the dictionary, it's a duplicate
                duplicates.append((file_name, file_path))
                file_dict[file_name].append(file_path)

    return duplicates

# Example usage:
path_to_scan = os.getcwd()
duplicates = find_duplicate_files_by_name(path_to_scan)

if duplicates:
    print("Duplicate files found:")
    for name, paths in duplicates:
        print(f"{name}:")
        for path in paths:
            print(f"   {path}")
else:
    print("No duplicate files found.")
