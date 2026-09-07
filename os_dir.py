import os
from os import makedirs

#os.mkdir('new_folder')
# makedirs(r"C:\Users\Windows\PycharmProjects\PY_1\new_folder\new1\new2", exist_ok=True)
# with open(r"C:\Users\Windows\PycharmProjects\PY_1\new_folder\base.txt", 'w',
#           encoding='utf-8') as file:
#     pass
# ps = os.path.join('path_new', 'nnn')
# print(ps)
# p = os.path.abspath('new_folder')
# print(p)
# print(os.path.exists(p))

def seek(target):
    size = 0
    folders = 0
    files = 0
    ps = os.path.join(target)
    p = os.path.abspath(ps)
    for i in os.listdir(p):
        ps = os.path.join(p, i)
        if os.path.isfile(ps):
            size += os.path.getsize(ps)
            files += 1
        else:
            folders += 1
            s, fs, f = seek(ps)
            size += s
            folders += fs
            files += f
    return size, folders, files

print(seek('new_folder'))