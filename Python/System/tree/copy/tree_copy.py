import os
import sys
from termcolor import colored
from colorama import Fore, Style

color = [ 'red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'grey', 'white' ]
attrib = ['bold']


#/---------------------------------------------------------------------------------------------------------------------------------------

def stampa_file(name, indent, last):
    indent = indent + 1
    #Stampa due righe di | colorati
    for i in range(2):
        a = 0
        b = 0
        for j in range(indent):
            if j == last and last != 0:
                print(" \t", end='')
                b = b + 1
                if b == 1:
                    b = 0
                    a = a + 1       
            else:
                text = colored("|", color[a], attrs=[attrib[b]])
                b = b + 1
                if b == 1:
                    b = 0
                    a = a + 1
                print(text + "\t", end='')
        print()
    
    indent = indent - 1

    #Stampa riga file colorata
    a = 0
    b = 0
    for j in range(indent):
        if j == last and last != 0:
            print(" \t", end='')    
            b = b + 1
            if b == 1:
                b = 0
                a = a + 1
            continue

        text = colored("|", color[a], attrs=[attrib[b]])
        b = b + 1
        if b == 1:
            b = 0
            a = a + 1
        print(text + "\t", end='')

    file_c = colored("|_______" + name, color[a], attrs=[attrib[b]])
    print(file_c)



#/---------------------------------------------------------------------------------------------------------------------------------------

def stampa_dir(name, indent):
    for n in range(2):
        a = 0
        b = 0
        for j in range(indent):
            text = colored("|", color[a], attrs=[attrib[b]])
            b = b + 1
            if b == 1:
                b = 0
                a = a + 1
            print(text + "\t", end='')
        print()
   
    indent = indent - 1

    #Stampa riga dir colorata
    a = 0
    b = 0
    for j in range(indent):
        text = colored("|", color[a], attrs=[attrib[b]])
        b = b + 1
        if b == 1:
            b = 0
            a = a + 1
        print(text + "\t", end='')

    file_c = colored(" --------->" + name, color[a], attrs=[attrib[b]])
    print(file_c)


# #/---------------------------------------------------------------------------------------------------------------------------------------

# #/ ALL TREE

def print_sub(path, indent, last):

    # Inizializzazione cartella
    os.chdir(path)
    files = os.listdir()
    dir = []

    #Stampa nome cartella
    if indent == 0:
        arr = path.split('/')
        text = colored(arr[-1], color[0], attrs=[attrib[0]])
        print(text)
    else:
        stampa_dir(path, indent)

    #Stampa file e crea lista dir
    for file in files:
        if os.path.isdir(file) == False and file[0] != '.':
            stampa_file(file, indent, last) 
        elif os.path.isdir(file) and file[0] != '.' and os.path.islink(file) == False:
            dir.append(file)

    #Uscita o ricorsione
    if len(dir) == 0:
        return
    else:
        i = 0 
        for d in dir:
            if i == len(dir) - 1:
                last = indent
            else:
                last = 0
            print_sub(d, indent+1, last)
            os.chdir("../")
            i = i + 1







print_sub(sys.argv[1], 0, 0)
# stampa_dir("Python", 3)



