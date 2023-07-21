def main_method():
    menu = {'1': "Space Availability details", '2': "Detect Duplicate Files", '3': "Detect Large Files",
            '4': "Scan all files", '5': "Exit"}

    while True:
        options = list(menu.keys())
        options.sort()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")
        if selection == '1':
            from space_availability import get_space, get_perc_distribution
            get_space()
            get_perc_distribution()
        if selection == '2':
            from detect_duplicates import get_duplicate_files
            get_duplicate_files()
        elif selection == '3':
            from detect_large_files import identify_large_files
            identify_large_files()
        elif selection == '4':
            from scan_all_files import scan_files
            scan_files()
        elif selection == '5':
            break
        else:
            print("Unknown Option Selected!")


main_method()
