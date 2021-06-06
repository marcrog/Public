import os
import sys
# from termcolor import colored

#/MAX TOTAL TIME 25/02/2021:  8.95 s


def check(n_dir, n_file):
    os.chdir(n_dir)
    start = os.getcwd()
    sys.stdout.write("\33[0;32m")
    print("Current dir: ", os.getcwd())

    files = os.listdir()
    dirs = []

    for file in files:
        if file == n_file:
            sys.stdout.write("\33[1;31m")
            print("FIND --------> " + os.getcwd() + "/" + file)
            return True
        elif os.path.isdir(file) and os.path.islink(file) == False:
            dirs.append(file)
    
    for dir in dirs:
        result = check(dir, n_file)
        if result:
            return True
        else:
            os.chdir(start)
            continue

    return False



n_dir = sys.argv[1]
n_file = sys.argv[2]

if check(n_dir, n_file) == False:
    sys.stdout.write("\033[;7m")
    print("XXX --- FILE NON TOVATO --- XXX")


