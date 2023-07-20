import os
import shutil


def get_space():
    path = os.getcwd()
    kb = 1024
    mb = 1024 * kb
    gb = 1024 * mb

    total_space, used_space, free_space = 0, 0, 0
    unit_total, unit_used, unit_free = 0, 0, 0

    disk_usage = shutil.disk_usage(path)

    if disk_usage[0] < gb:
        total_space = round((disk_usage[0] / mb), 2)
        unit_total = "MB"
    else:
        total_space = round((disk_usage[0] / gb), 2)
        unit_total = "GB"

    if disk_usage[1] < gb:
        used_space = round((disk_usage[1] / mb), 2)
        unit_used = "MB"
    else:
        used_space = round((disk_usage[1] / gb), 2)
        unit_used = "GB"

    if disk_usage[2] < gb:
        free_space = round((disk_usage[2] / mb), 2)
        unit_free = "MB"
    else:
        free_space = round((disk_usage[2] / gb), 2)
        unit_free = "GB"

    print(f"total = {total_space} {unit_total}, used = {used_space} {unit_used}, free = {free_space} {unit_free}")


get_space()
