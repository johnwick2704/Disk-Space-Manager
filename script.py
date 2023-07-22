import os
import shutil


def notify():
    from plyer import notification

    notification.notify(
        title="DISK MANAGEMENT",
        message="SPACE IS ALMOST FULL",
        timeout=10
    )


def get_space():
    path = os.getcwd()
    kb = 1024
    mb = 1024 * kb
    gb = 1024 * mb

    disk_usage = shutil.disk_usage("C:\\")

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

    if (used_space / total_space) > 0.2:
        notify()

get_space()