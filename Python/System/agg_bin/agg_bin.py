import os
import sys
from shutil import copyfile

def check(n_dir, n_file):
    os.chdir(n_dir)
    start = os.getcwd()
    print("Current dir: ", os.getcwd())

    files = os.listdir()

    for file in files:
        if file == n_file:
            print("FIND --------> " + os.getcwd() + "/" + file)
            return True
        elif os.path.isdir(file) and os.path.islink(file) == False:
            result = check(file, n_file)
            if result:
                return True
            else:
                os.chdir(start)
                continue
    return False


n_bin = sys.argv[1]
temp_name = "/usr/bin/" + n_bin + "_old"

if check("/usr/bin", n_bin):
    print("Presente")
    os.rename("/usr/bin/" + n_bin, "/usr/bin/" + temp_name)
    print("Renamed= /")
    copyfile(n_bin, "/usr/bin/" + n_bin)
    os.remove(temp_name)
