import os
import sys

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

n_dir = sys.argv[1]
n_file = sys.argv[2]

check(n_dir, n_file)
