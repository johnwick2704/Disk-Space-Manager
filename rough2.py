import getpass
import os
USER_NAME = getpass.getuser()
print(USER_NAME)


def add_to_startup(file_path=r"C:\Users\Utkarsh\Desktop\Tally CodeBrewers\script.py"):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = fr"C:\Users\{USER_NAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(fr'start "" f"{USER_NAME}"' % file_path)