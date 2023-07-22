import os


def function(path):
    menu = {'1': "Space Availability details", '2': "Detect Duplicate Files", '3': "Detect Large Files",
            '4': "Scan all files", '5': "Delete Files and Folders", '6': "Exit"}

    while True:
        options = list(menu.keys())
        options.sort()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")
        if selection == '1':
            from space_availability import get_space, get_perc_distribution
            get_space()
            get_perc_distribution(path)
        elif selection == '2':
            from detect_duplicates import get_duplicate_files
            get_duplicate_files(path)
        elif selection == '3':
            from detect_large_files import identify_large_files
            identify_large_files(path)
        elif selection == '4':
            from scan_all_files import scan_files
            scan_files(path)
        elif selection == '5':
            from delete_files_folders import delete
            delete(path)
        elif selection == '6':
            break
        else:
            print("Unknown Option Selected!")


def main_method():
    select_path = {'1': "Current Directory", '2': "Current Drive", '3': "Exit"}
    while True:
        options_path = list(select_path.keys())
        options_path.sort()
        for entry in options_path:
            print(entry, select_path[entry])

        sel = input("Please Select: ")
        if sel == '1':
            path = os.getcwd()
            print(f"Selected path is : {path}")
            function(path)
        elif sel == '2':
            path = os.getcwd().split('\\')[0] + "\\"
            print(f"Selected path is : {path}")
            function(path)
        elif sel == '3':
            break
        else:
            print("Invalid Option Selected")


main_method()
