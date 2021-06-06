import os
import sys

# def check(n_dir, n_file):
#     os.chdir(n_dir)
#     start = os.getcwd()
#     # print("Current dir: ", os.getcwd())

#     files = os.listdir()

#     for file in files:
#         if file == n_file:
#             # print("FIND --------> " + os.getcwd() + "/" + file)
#             return os.path(file)
#         elif os.path.isdir(file) and os.path.islink(file) == False:
#             result = check(file, n_file)
#             if result != 0:
#                 return True
#             else:
#                 os.chdir(start)
#                 continue
#     return 0


def check_backup(path,name):
    os.chdir(path)
    files = os.listdir()
    for n in files:
        if n == name:
            return True
    return False

def confronto(actual_path, backup_path, name):
    os.chdir(actual_path)
    files = os.listdir()
    for file in files:
        if check_backup(backup_path, file) and file == name:
            return True
    return False










    
