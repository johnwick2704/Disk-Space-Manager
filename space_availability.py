import os
import shutil


def get_space():
    path = os.getcwd()
    kb = 1024
    mb = 1024 * kb
    gb = 1024 * mb

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

    print(f"DISK SPACE DETAILS: total = {total_space} {unit_total}, "
          f"used = {used_space} {unit_used}, free = {free_space} {unit_free}")


def file_type(file_name):
    vid_ex = ['mp4', 'mov', 'avi', 'mkv', 'wmv', 'webm']
    doc_ex = ['doc', 'docx', 'txt', 'pdf', 'rtf', 'xlsx', 'csv', 'py', 'ipynb', 'wps', 'java', 'cpp', 'pptx']
    img_ex = ['jpg', 'jpeg', 'png', 'gif']
    app_ex = ['exe']

    file_category = file_name.split('.')[-1]

    if file_category in vid_ex:
        return "Video"
    elif file_category in doc_ex:
        return "Document"
    elif file_category in img_ex:
        return "Image"
    elif file_category in app_ex:
        return "Application"
    else:
        return "Other"


def get_perc_distribution():
    path = os.getcwd()
    vid_sz, oth_sz, img_sz, app_sz, doc_sz = 0, 0, 0, 0, 0

    for (root, dirs, files) in os.walk(path):
        for file in files:
            ex = file_type(file)
            size = os.stat(os.path.join(root, file)).st_size / 1024
            unit = "KB"

            if ex == "Video":
                vid_sz = vid_sz + size
            elif ex == "Application":
                app_sz = app_sz + size
            elif ex == "Image":
                img_sz = img_sz + size
            elif ex == "Document":
                doc_sz = doc_sz + size
            else:
                oth_sz = oth_sz + size

    sum = vid_sz + app_sz + img_sz + doc_sz + oth_sz

    perc_vid = round(((vid_sz * 100) / sum), 2)
    perc_app = round(((app_sz * 100) / sum), 2)
    perc_doc = round(((doc_sz * 100) / sum), 2)
    perc_img = round(((img_sz * 100) / sum), 2)
    perc_oth = round(((oth_sz * 100) / sum), 2)

    print(f"Size of Current Directory = {round(sum, 2)} {unit}")

    print(f"Videos = {perc_vid}%, Images = {perc_img}%, Documents = {perc_doc}%, "
          f"Applications = {perc_app}%, Others = {perc_oth}%")

