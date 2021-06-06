import os
import sys
from termcolor import colored
# from colorama import Fore, Style

Reset = "\x1b[0m"
Hidden = "\x1b[8m"

# color = ["\033[38;5;9m" ,"\x1b[34m" , "\x1b[32m","\x1b[33m","\x1b[36m", "\x1b[35m", "\x1b[37m"]
color = ["\033[38;2;226;10;23m", "\033[38;2;238;67;11m", "\033[38;2;254;115;24m", "\033[38;2;255;166;0m", "\033[38;2;255;240;1m", "\033[38;2;109;175;25m", "\033[38;2;2;129;49m", "\033[38;2;0;131;213m",
        "\033[38;2;1;60;130m", "\033[38;2;1;45;118m", "\033[38;2;55;21;98m", "\033[38;2;155;7;101m", "\033[38;2;255;255;255m"]



#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def stampa(name, indent, serie, tipo):
    #Stampa prime due righe
    if tipo == "file":
        indent = indent + 1
    for x in range(0):
        a = 0
        # i parte da 0 e arriva a indent - 1 
        for i in range(indent):
            if i in serie:
                text = Hidden + "|"
            else:
                text =  color[a] + "|"
            a = a + 1
            if a >= len(color):
                a = len(color) - 1
            print(text + "\t", end='')
            print(Reset, end='')
        print()
    
    #Stampa riga file /dir colorata
    #Bisogna stamapare un indentazione in meno per fare spazio al nome del fil
    indent = indent - 1
    a = 0
    for i in range(indent):
        if i in serie:
            text = Hidden + "|"
        else:
            text = color[a] + "|"
        a = a + 1
        if a >= len(color):
            a = len(color) - 1
        print(text + "\t", end='')
        print(Reset, end='')
    
    if tipo == "file":
        file_c =  color[a] + "|______" + name
        print(file_c)
    else:
        file_c = color[a] + "|--------->" + name
        print(file_c)



# #/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def print_sub(path, indent, serie, last):
    os.chdir(path)
    files = os.listdir()
    dirs = []
    
    if indent == 0:
        arr = path.split('/')
        text = colored(arr[-1], 'red')
        print(text)
    else:
        stampa(path, indent,serie, "dir")
        if last :
            serie.append(indent - 1)

    #Stampa file e crea lista dir
    for file in files:
        if os.path.isdir(file) == False and file[0] != '.':
            stampa(file, indent, serie, "file")
        elif os.path.isdir(file) and file[0] != '.' and os.path.islink(file) == False:
            dirs.append(file)    

    if len(dirs) == 0:
        return 
    else:
        for cartella in dirs:
            if dirs.index(cartella) + 1 == len(dirs):
                last = True
            else:
                last = False
            print_sub(cartella, indent + 1, serie, last)
            if last == True:
                serie.pop(-1)
            os.chdir("../")
        last = False



#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Questo conteggio parte da 0
serie = []
last = False

print_sub(sys.argv[1], 0, serie, last)
# stampa_file("Python", 1,  serie)
# stampa_dir("Python", 2,  serie)
# print(2)
